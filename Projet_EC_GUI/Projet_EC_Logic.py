# coding=utf-8
#  @file   Project_EC_Logic.py
#  @date   1 Mai 2021    
#  @author Simon Jourdenais
#  @brief  Ce programme gère l'affichage de l'interface utilisateur du moniteur/contrôleur de serre du projet Environnement Contrôlé
#          Attention : Un instance du programme "Projet_EC_Logic.py" doit avoir été préallablement au lancement de celui-ci .
#
#          Comme indiqué ci dessus, pour assurer le bon fonctionnement du programme, assurez vous que ce fichier se trouve dans le meme dossier que "Projet_EC_Class_Serre.py","Projet_EC_Logic.py",
#          "GUI_PEC_Monitor.ui", "GUI_PEC_Control.ui", "GUI_PEC_Config.ui" et "GUI_PEC_Admin.ui".
#
#  @matériel   Raspberry Pi 4 B, Écran 7" Touchscreen 


import json, serial, RPi.GPIO as GPIO
from Projet_EC_Class_Serre import gestionSerre
from enum import IntEnum
from time import time, sleep
from datetime import datetime
from datetime import timedelta
from urllib.error import URLError
from urllib.request import urlopen
import paho.mqtt.client as mqtt 
from simple_pid import PID

class e_bytes(IntEnum):   # Pour avoir ordre des bytes
    SOH=0,
    temp_SEN_MSB=1,
    temp_SEN_LSB=2,
    humid_SEN_MSB=3,
    humid_SEN_LSB=4,
    ppm_Dioxide_MSB=5,
    ppm_Dioxide_LSB=6,
    ppb_TVOC_MSB=7,
    ppb_TVOC_LSB=8,
    temp_DS_MSB=9,
    temp_DS_LSB=10,
    checksum=11,
    maxBytes=12




class LogicControl(gestionSerre):
    #Defines pour ce programme
    DEGRE_ATTENUATION = 5   #Macro pour attenuation des valeurs/ moyenne des valeurs lues
    FLUSH_TIME = 3  #Macro de duree de temps de Vidange d<air REMETTRE A PLUS QUE 0!!!!!
    CO2_FLUSH_TIME = 1
    PERIOD_HEAT = 5
    PERIOD_HUMIDITY = 30
    API_KEY_LENGTH = 16
    #End defines

    serialHandle = serial.Serial('/dev/ttyUSB0', 9600)  #Initialise la connection avec le ARDUINO NANO

    current_Temp_DS=0
    current_Temp_SHT=0
    current_Humid=0
    dioxide_CCS =0
    current_Tvoc =0

    past_Temp = [0,0,0,0,0]
    past_Humid = [0,0,0,0,0]
    past_Dioxide = [0,0,0,0,0]

    good_Temp_Val_Streak = 0
    good_Humid_Val_Streak = 0
    good_Dioxide_Val_Streak = 0

    cycle_Int_Vid_Next = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    flush_End_Time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    dioxide_Checkup = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    dioxide_OL_Minute_Tick = 0
    heat_On_Time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    heat_Off_Time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    humid_On_Time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    humid_Off_Time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    flushing_On = False
    force_Flushing_On = False
    heating_On = False
    humidity_On = False

    TimeCyclePrevSec = 0  # 
    TimeCycleInterval = 2 #
    ThingSpeakPrevSec = 0 #Variable qui prend le temps référence pour délais d'envoie ThingSpeak
    ThingSpeakInterval = 15 # 15 secondes de délais entre uploads

    def __init__(self):
        super().__init__()
  
    def setAPI_URL(self, api_key):
        self.cle_API=api_key #"F6AG8QMUBNAO57IL"  # Clé à William || "OTSESYSMRPRYTJFL" # Clé a Simon
        self.base_url_ThingSpeak="https://api.thingspeak.com/update?api_key={}".format(self.cle_API) 
        self.save_To_Thingspeak()

    def resetAPI_URL(self):
        self.cle_API="" #"F6AG8QMUBNAO57IL"  # Clé à William || "OTSESYSMRPRYTJFL" # Clé a Simon
        self.base_url_ThingSpeak="https://api.thingspeak.com/update?api_key={}".format(self.cle_API) 
    
    def verifyTrame(self, bytes_List):
        calc_Chksum=0
        checksum_Rx = 0
        byte_Count =0
        soh_Present =False
        verif_Ok = False
        for byte_Count in range(0,len(bytes_List)): #Commence a 1 pour skip le SOH et fini a 10 pour ne pas prendre le checksum en compte.
            if(byte_Count != 0):
                if(byte_Count != e_bytes.checksum ):
                    calc_Chksum+=int(bytes_List[byte_Count],16)
                else:
                    checksum_Rx = int(bytes_List[byte_Count],16)
                    calc_Chksum%=256
                    if(checksum_Rx == calc_Chksum and byte_Count == (e_bytes.maxBytes-1) and soh_Present == True):
                        verif_Ok = True
            else:
                if(bytes_List[byte_Count] == "1"):
                    soh_Present = True
            bytes_List[byte_Count] = str(int(bytes_List[byte_Count],16))  #Change lentree Hexadecimael en decimale dans la liste de bytes
            byte_Count +=1
        return verif_Ok
        
    
    #Fonction qui lit le port série. Port de lecture /dev/serial0. Données de la provenance du ARDUINO NANO. Reçoit une string contenant deux valeurs.
    #Première valeur CO2, deuxième TVOC.   
    def read_Serial(self):
        bytes_List = []
        try:
            if self.serialHandle.in_waiting > 0: 
                serial_Line=self.serialHandle.readline()   #lit ce qui a sur le port serie
                decodedDataSerial = serial_Line.decode()  
                decodedDataSerial = decodedDataSerial.replace('\n', '') #enleve les saut de ligne
                decodedDataSerial = decodedDataSerial.replace('\r', '') 
                decodedDataSerial = decodedDataSerial.replace('\0', '') #enleve le byte NUL
                splitDataSerial = decodedDataSerial.split(" ")
                for split_Byte in splitDataSerial: 
                    if(split_Byte.rstrip() != "" ):
                        bytes_List.append(split_Byte)
                        
                if(self.verifyTrame(bytes_List)==True):
                    self.current_Temp_DS = float((bytes_List[e_bytes.temp_DS_MSB]+"."+bytes_List[e_bytes.temp_DS_LSB]))
                    self.current_Temp_SHT = float((bytes_List[e_bytes.temp_SEN_MSB]+"."+bytes_List[e_bytes.temp_SEN_LSB]))
                    self.current_Humid = float((bytes_List[e_bytes.humid_SEN_MSB]+"."+bytes_List[e_bytes.humid_SEN_LSB]))
                    self.current_Dioxide = (((int(bytes_List[e_bytes.ppm_Dioxide_MSB])*256)+int(bytes_List[e_bytes.ppm_Dioxide_LSB])))
                    self.current_Tvoc = (((int(bytes_List[e_bytes.ppb_TVOC_MSB])*256)+int(bytes_List[e_bytes.ppb_TVOC_LSB])))
                    meanDataLog()
                    publishDataToGUI()
                self.serialHandle.flushInput()
                

        except Exception as err:
            print(str(err))
            self.serialHandle.close() #Ferme port série


    
    #Envoi les données vers ThingSpeak par URL. Contient: Température du DS18B20, Température et humidité du SEN0227, la concentartion de CO2 et le TVOC du CCS811.
    #Données envoyées à la minute. ThingSpeak nous envoie le numéro de l'entré en retour si notre envoie c'est bien passé.
    def save_To_Thingspeak(self):
        try:
            thingspeakHttp = self.base_url_ThingSpeak + "&field1={:.2f}&field2={:.2f}&field3={:.2f}&field4={:f}&field5={:f}".format(self.current_Temp_DS,self.current_Temp_SHT,self.current_Humid,self.current_Dioxide,self.current_Tvoc,) #Formatage de la string URL pour l'envoie vers ThingSpeak.
            conn = urlopen(thingspeakHttp) #Envoie les infos vers ThingSpeak
            code_Retour = conn.read()
            print("Saved to ThingSpeak API ",self.cle_API + " - Confirmation : Entry # "+ str(code_Retour))
            if(self.Flag_Thingspeak_Connected != True):
                self.Flag_Thingspeak_Connected = True
                self.saveAPI()
                sendFlagThingspeakConnected(obj_Control.Flag_Thingspeak_Connected)#Envoi le flag True sur le channel MQTT /Projet_EC/GUI/Flags/API
            conn.close()
        except URLError as err:
            print(err.__str__)
        except Exception as err:
            self.Flag_Thingspeak_Connected = False
            sendFlagThingspeakConnected(self.Flag_Thingspeak_Connected) #Send code erreur au GUI si Fail URLRequest
            try:
                conn.close()
            except:
                pass
            print(str(err))




def sendFlagThingspeakConnected(bool_Api):
    api_String = '{"api_ok":""}'
    json_Data = json.loads(api_String)
    if(bool_Api == True):
        json_Data["api_ok"] = True
    elif(bool_Api == False):
        json_Data["api_ok"] = False
    clientMQTT_Logic.publish(topic=obj_Control.TOPIC_GUI_FLAG_API, payload=json.dumps(json_Data)) #Publie sur /test le JSON des valeurs de capteurs.
    print("Flag Validité TS Sent : "+ str(bool_Api))   

def publishDataToGUI():
    try:
        json_data = json.loads('{"DS": {"temp": '+str(obj_Control.current_Temp_DS)+
        '}, "SHT": {"temp": '+str(obj_Control.current_Temp_SHT)+', "hum": '+str(obj_Control.current_Humid)+'}, "CSS811": {"CO2": '+str(obj_Control.current_Dioxide)+', "TVOC": '+str(obj_Control.current_Tvoc)+'}}')
        clientMQTT_Logic.publish(topic=obj_Control.TOPIC_DATA_SERRE, payload=json.dumps(json_data)) #Publie sur /Projet_EC/Sensorblock_1/Readings le JSON des valeurs lues des capteurs
        
    except Exception as err:
        print(str(err))

def on_message(client, userdata, msg):
    try:
        incomingMQTT = msg.payload.decode()  #prend le message reçu #'{"DS": {"temp": 25}}'
        incomingMQTT = json.loads(incomingMQTT) #Formatte le message sous format JSON
    except Exception as err:
        print(err)
        
    if(msg.topic == obj_Control.TOPIC_GUI_API):
        try:
            if len(incomingMQTT['api_key']) != obj_Control.API_KEY_LENGTH:
                print("Mauvaise longueur de clé API")
                raise Exception()
            print("Clé API reçue : "+str(incomingMQTT['api_key']))
            obj_Control.setAPI_URL(str(incomingMQTT['api_key']))
        except Exception as err:
            print("Clé API fautive")
            obj_Control.resetAPI_URL()
            obj_Control.Flag_Thingspeak_Connected=False
            sendFlagThingspeakConnected(obj_Control.Flag_Thingspeak_Connected) #Envoi le flag False sur le channel MQTT /Projet_EC/GUI/Flags/API
    elif(msg.topic == obj_Control.TOPIC_GUI_API_INIT):
        obj_Control.setAPI_URL(str(incomingMQTT['api_key']))
        obj_Control.Flag_Thingspeak_Connected=True
        sendFlagThingspeakConnected(obj_Control.Flag_Thingspeak_Connected) #Envoi le flag False sur le channel MQTT /Projet_EC/GUI/Flags/API
    elif(msg.topic == obj_Control.TOPIC_GUI_INPUT_SET):
        try:
            obj_Control.setpoint_Temp = incomingMQTT["Setpoints"]["Temp"]
            obj_Control.setpoint_Humid = incomingMQTT["Setpoints"]["Humid"]
            obj_Control.setpoint_Dioxide = incomingMQTT["Setpoints"]["Dioxide"]
            obj_Control.setpoint_Int_Vid = incomingMQTT["Setpoints"]["Int_Vide"]
            obj_Control.cycle_Int_Vid_Next =  (datetime.now() + timedelta(hours = obj_Control.setpoint_Int_Vid)).strftime("%m/%d/%Y, %H:%M:%S")
            print("Consignes reçues : {} degres, {} % HR, {} ppm CO2, intervalles de {} h ".format(obj_Control.setpoint_Temp, obj_Control.setpoint_Humid, obj_Control.setpoint_Dioxide, obj_Control.setpoint_Int_Vid))
            if(obj_Control.setpoint_Int_Vid>0):
                print("Prochaine flush configurée pour {}".format(datetime.strptime(obj_Control.cycle_Int_Vid_Next,"%m/%d/%Y, %H:%M:%S")))
            else:
                print("Vidanges automatiques désactivées ")
        except:
            print("Erreur lors de la réception des consignes!") #Un flag d'erreur/code devrait être envoyé au programme de GUI pour réenvoyer ou indiquer l'erreur
    elif(msg.topic == obj_Control.TOPIC_GUI_INPUT_CYCLE):
        try:
            obj_Control.cycle_Name =incomingMQTT["Cycle"]["Nom"]
            obj_Control.cycle_DEL_COB_Used=incomingMQTT["Cycle"]["Lumiere"]["DEL_COB"] 
            obj_Control.cycle_DEL_Panel_Used=incomingMQTT["Cycle"]["Lumiere"]["DEL_Panel"] 
            obj_Control.cycle_Heure_Dep=incomingMQTT["Cycle"]["Temps"]["Depart"]["Heure"]
            obj_Control.cycle_Minute_Dep=incomingMQTT["Cycle"]["Temps"]["Depart"]["Minute"]
            obj_Control.cycle_Heure_Fin=incomingMQTT["Cycle"]["Temps"]["Fin"]["Heure"]
            obj_Control.cycle_Minute_Fin=incomingMQTT["Cycle"]["Temps"]["Fin"]["Minute"]
            print("Cycle reçu : {}, Départ {}h{}, Fermeture {}h{} | Lumières :  DEL {}, Panel {}".format(obj_Control.cycle_Name, obj_Control.cycle_Heure_Dep, obj_Control.cycle_Minute_Dep, obj_Control.cycle_Heure_Fin, obj_Control.cycle_Minute_Fin, obj_Control.cycle_DEL_COB_Used, obj_Control.cycle_DEL_Panel_Used))
        except:
            print("Erreur lors de la réception du cycle!") #Un flag d'erreur/code devrait être envoyé au programme de GUI pour réenvoyer ou indiquer l'erreur
    

def toggleLighting(state):
    if(obj_Control.cycle_DEL_COB_Used == True or obj_Control.cycle_DEL_Panel_Used == True):

        if(obj_Control.cycle_DEL_COB_Used == True):
            GPIO.output(obj_Control.PIN_DEL_COB, state)
        else:
            GPIO.output(obj_Control.PIN_DEL_COB, False)

        if(obj_Control.cycle_DEL_Panel_Used == True):
            GPIO.output(obj_Control.PIN_EXT_LUM, state)
        else:
            GPIO.output(obj_Control.PIN_EXT_LUM, False)

def meanTemperature():
    mean_Temp = -1
    if(int(obj_Control.current_Temp_DS) != -1 and int(obj_Control.current_Temp_SHT) != -1 ):
        mean_Temp =(float(obj_Control.current_Temp_DS)+float(obj_Control.current_Temp_SHT))/2
    elif(int(obj_Control.current_Temp_SHT) == -1):
        mean_Temp = float(obj_Control.current_Temp_DS)
    elif(int(obj_Control.current_Temp_DS) == -1):
        mean_Temp = float(obj_Control.current_Temp_SHT)
    else:
        obj_Control.Flag_Data_Error = True
    return mean_Temp

def meanDataLog():
    
    mean_Temp = meanTemperature ()  #Fonction retourne une moyenne des deux valeur de température lue, sil y a lieu. sinon retourne la valeur lue.
    mean_Humid = 0
    mean_Dioxide = 0
    try:
        #Mini logging de données pour faire une moyenne afin d'atténuer les pics indésirables (soit erreurs ou manipulations)
        if(mean_Temp != -1):
            if(len(obj_Control.past_Temp)>int(obj_Control.DEGRE_ATTENUATION)):
                obj_Control.past_Temp.pop(0) #Si la liste contient plus de 5 elements, on pop le dernier
            obj_Control.past_Temp.append(mean_Temp) #Insere la deniere entree dans le tableau
            obj_Control.good_Temp_Val_Streak+=1
        elif(mean_Temp == -1):
            obj_Control.good_Temp_Val_Streak =0
            obj_Control.past_Temp.clear()
        try:
            mean_Temp = 0.0
            for x in range(0,obj_Control.DEGRE_ATTENUATION):
                mean_Temp += float(obj_Control.past_Temp[x])
            mean_Temp/=float(obj_Control.DEGRE_ATTENUATION)
        except:
            pass
    except Exception as err:
        print ("erreur Logging Temp"+str(err))

    try:
        if(obj_Control.current_Humid != -1):
            if(len(obj_Control.past_Humid)>obj_Control.DEGRE_ATTENUATION):
                obj_Control.past_Humid.pop(0) #Si la liste contient plus de 5 elements, on pop le dernier
            obj_Control.past_Humid.append(obj_Control.current_Humid) #Insere la deniere entree dans le tableau
            obj_Control.good_Humid_Val_Streak +=1
        elif(obj_Control.current_Humid == -1):
            obj_Control.good_Humid_Val_Streak = 0
            obj_Control.past_Humid.clear()
        try:
            for x in range(0,obj_Control.DEGRE_ATTENUATION):
                mean_Humid += obj_Control.past_Humid[x]
            mean_Humid/=obj_Control.DEGRE_ATTENUATION
        except:
            pass
    except Exception as err:
        print ("erreur Logging Humid"+str(err))

    try:
        if(obj_Control.current_Dioxide != -1):
            if(len(obj_Control.past_Dioxide)>obj_Control.DEGRE_ATTENUATION):
                obj_Control.past_Dioxide.pop(0) #Si la liste contient plus de 5 elements, on pop le dernier
            obj_Control.past_Dioxide.append(obj_Control.current_Dioxide) #Insere la deniere entree dans le tableau
            obj_Control.good_Dioxide_Val_Streak +=1
        elif(obj_Control.current_Dioxide == -1):
            obj_Control.good_Dioxide_Val_Streak = 0
            obj_Control.past_Dioxide.clear()
        try:
            for x in range(0,obj_Control.DEGRE_ATTENUATION):
                mean_Dioxide += obj_Control.past_Dioxide[x]
            mean_Dioxide/=obj_Control.DEGRE_ATTENUATION
        except:
            pass
    except Exception as err:
        print ("Erreur Logging Dioxide"+str(err))

    return mean_Temp, mean_Humid, mean_Dioxide


def controlTemp(mean_Temp):
    if(mean_Temp>0):
        datetime_Now = datetime.strptime(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),"%m/%d/%Y, %H:%M:%S")    #Fait comme ca pour avoir la meme forme que les autres datetimes. Sinon des erreurs de precisions arrivent.
        datetime_On_Heat = datetime.strptime(obj_Control.heat_On_Time,"%m/%d/%Y, %H:%M:%S")
        datetime_Off_Heat = datetime.strptime(obj_Control.heat_Off_Time,"%m/%d/%Y, %H:%M:%S")
        if(datetime_Now > datetime_Off_Heat and datetime_Now > datetime_On_Heat):
            obj_Control.heat_On_Time = datetime_Now.strftime("%m/%d/%Y, %H:%M:%S")
            obj_Control.heat_Off_Time = (datetime_Now+timedelta(seconds = obj_Control.PERIOD_HEAT)).strftime("%m/%d/%Y, %H:%M:%S")
        elif(datetime_Now >= datetime_Off_Heat):  #Lorsque tempsoff est depassé, allume et set le temps max On
            try:
                pid_Heating = PID(10,5,3, setpoint=obj_Control.setpoint_Temp)
                pid_Heating.output_limits = (0, obj_Control.PERIOD_HEAT)   #Fait un output de 0 a 5 qui sera changé en secondes
                temp_Control = pid_Heating(mean_Temp)
            except:
                print("Erreur Heating Control")
            if(obj_Control.heating_On == False):
                obj_Control.heating_On = True
                obj_Control.heat_On_Time = (datetime_Off_Heat + timedelta(seconds = (int(temp_Control)), milliseconds=(temp_Control*1000)%1000)).strftime("%m/%d/%Y, %H:%M:%S")
                obj_Control.heat_Off_Time = (datetime_Off_Heat + timedelta(seconds = obj_Control.PERIOD_HEAT)).strftime("%m/%d/%Y, %H:%M:%S")
                obj_Control.toggle(obj_Control.PIN_CHAUFFAGE)
                #print("Heating On - Time : {} -> Heat Shutoff : {} - New Cycle : {}".format(datetime_Now.strftime("%m/%d/%Y, %H:%M:%S"),obj_Control.heat_On_Time, obj_Control.heat_Off_Time))
        elif(datetime_Now>=datetime_On_Heat):
            if(obj_Control.heating_On == True):
                #print("Shutting off Heat. - Time : {}".format(datetime_Now.strftime("%m/%d/%Y, %H:%M:%S")))
                obj_Control.heating_On = False
                obj_Control.toggle(obj_Control.PIN_CHAUFFAGE)

    


def controlHumid(mean_Humid):

    if(mean_Humid>0 and obj_Control.force_Flushing_On == False and obj_Control.flushing_On == False):
        try:
            datetime_Now = datetime.strptime(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),"%m/%d/%Y, %H:%M:%S")    #Fait comme ca pour avoir la meme forme que les autres datetimes. Sinon des erreurs de precisions arrivent.
            datetime_On_Humid = datetime.strptime(obj_Control.humid_On_Time,"%m/%d/%Y, %H:%M:%S")
            datetime_Off_Humid = datetime.strptime(obj_Control.humid_Off_Time,"%m/%d/%Y, %H:%M:%S")
            if(datetime_Now > datetime_Off_Humid and datetime_Now > datetime_On_Humid):
                obj_Control.humid_On_Time = datetime_Now.strftime("%m/%d/%Y, %H:%M:%S")
                obj_Control.humid_Off_Time = (datetime_Now+timedelta(seconds = obj_Control.PERIOD_HUMIDITY)).strftime("%m/%d/%Y, %H:%M:%S")
            elif(datetime_Now >= datetime_Off_Humid):  #Lorsque tempsoff est depassé, allume et set le temps max On
                try:
                    pid_Humid = PID(5,4,1, setpoint=obj_Control.setpoint_Humid)
                    pid_Humid.output_limits = (0, obj_Control.PERIOD_HUMIDITY)  #Limites sont 0 a 60, puisque l<humidificateur prends ~5 secondes avant de commencer a humidifier. donc minimum On time = 5 secondes, maximum 55 secondes genre
                    humid_Control = pid_Humid(mean_Humid)
                except:
                    print("Erreur Humidity Control")
                if(obj_Control.humidity_On == False and humid_Control>=6):
                    obj_Control.humidity_On = True
                    obj_Control.humid_On_Time = (datetime_Off_Humid + timedelta(seconds = (int(humid_Control)))).strftime("%m/%d/%Y, %H:%M:%S")
                    obj_Control.humid_Off_Time = (datetime_Off_Humid + timedelta(seconds = obj_Control.PERIOD_HUMIDITY)).strftime("%m/%d/%Y, %H:%M:%S")
                    obj_Control.toggle(obj_Control.PIN_HUMID)
                    print("Humidity On - Time : {} -> Humidity Shutoff : {} - New Cycle : {}".format(datetime_Now.strftime("%m/%d/%Y, %H:%M:%S"),obj_Control.humid_On_Time, obj_Control.humid_Off_Time))
            elif(datetime_Now>=datetime_On_Humid):
                if(obj_Control.humidity_On == True):
                    print("Shutting off Humidity. - Time : {}".format(datetime_Now.strftime("%m/%d/%Y, %H:%M:%S")))
                    obj_Control.humidity_On = False
                    obj_Control.toggle(obj_Control.PIN_HUMID)
        except Exception as err:
            print(str(err))



def controlDioxide(mean_Dioxide):
    datetime_Now = datetime.strptime(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),"%m/%d/%Y, %H:%M:%S")    #Fait comme ca pour avoir la meme forme que les autres datetimes. Sinon des erreurs de precisions arrivent.
    time_Check_CO2 = datetime.strptime(obj_Control.dioxide_Checkup,"%m/%d/%Y, %H:%M:%S")
    if(datetime_Now>=time_Check_CO2):
        if(mean_Dioxide>=obj_Control.setpoint_Dioxide):
            obj_Control.dioxide_OL_Minute_Tick +=1  
        elif(mean_Dioxide<obj_Control.setpoint_Dioxide):
            if(obj_Control.dioxide_OL_Minute_Tick >0):
                obj_Control.dioxide_OL_Minute_Tick -=1  
        obj_Control.dioxide_Checkup = (time_Check_CO2 + timedelta(minutes = 1)).strftime("%m/%d/%Y, %H:%M:%S")
    if(obj_Control.dioxide_OL_Minute_Tick >= 10):
        obj_Control.dioxide_OL_Minute_Tick = 0
        forceFlush()
        
        

def checkInterVidange():
    datetime_Now = datetime.strptime(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),"%m/%d/%Y, %H:%M:%S")    #Fait comme ca pour avoir la meme forme que les autres datetimes. Sinon des erreurs de precisions arrivent.
    if(obj_Control.flushing_On == True):
        datetime_Flush_End = datetime.strptime(obj_Control.flush_End_Time,"%m/%d/%Y, %H:%M:%S")
        if(datetime_Now >= datetime_Flush_End):
            if(obj_Control.flushing_On == True):
                print("End of Flush")
                obj_Control.flushing_On = False
                obj_Control.toggle(obj_Control.PIN_FAN_CONDUIT)
                obj_Control.toggle(obj_Control.PIN_DESHUMID)
    datetime_Flush_Next = datetime.strptime(obj_Control.cycle_Int_Vid_Next,"%m/%d/%Y, %H:%M:%S")
    if(datetime_Now >= datetime_Flush_Next):
        if(obj_Control.flushing_On != True):
            obj_Control.flush_End_Time = (datetime_Now + timedelta(minutes = obj_Control.FLUSH_TIME)).strftime("%m/%d/%Y, %H:%M:%S")
            obj_Control.flushing_On = True
            obj_Control.toggle(obj_Control.PIN_FAN_CONDUIT)
            obj_Control.toggle(obj_Control.PIN_DESHUMID)
            obj_Control.cycle_Int_Vid_Next = (datetime_Now + timedelta(hours = obj_Control.setpoint_Int_Vid)).strftime("%m/%d/%Y, %H:%M:%S")
            print("Flushing. | Next Flush : {}".format( datetime.strptime(obj_Control.cycle_Int_Vid_Next,"%m/%d/%Y, %H:%M:%S")))

def forceFlush():
    datetime_Now = datetime.strptime(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),"%m/%d/%Y, %H:%M:%S")    #Fait comme ca pour avoir la meme forme que les autres datetimes. Sinon des erreurs de precisions arrivent.
    if(obj_Control.Flushing_On != True):
        if(obj_Control.force_Flushing_On == True):
            datetime_Flush_End = datetime.strptime(obj_Control.flush_End_Time,"%m/%d/%Y, %H:%M:%S")
            if(datetime_Now >= datetime_Flush_End):
                print("Stopping force flush.")
                if(obj_Control.force_Flushing_On == True):
                    obj_Control.force_Flushing_On = False
                    obj_Control.toggle(obj_Control.PIN_DESHUMID)
        if(obj_Control.force_Flushing_On != True):
            obj_Control.flush_End_Time = (datetime_Now + timedelta(minutes = obj_Control.CO2_FLUSH_TIME)).strftime("%m/%d/%Y, %H:%M:%S")
            obj_Control.force_Flushing_On = True
            obj_Control.toggle(obj_Control.PIN_DESHUMID)
            print("Force flushing CO2")


def controlSerre(mean_Values):
    if(obj_Control.setpoint_Int_Vid>0):
        checkInterVidange()

    if(obj_Control.good_Temp_Val_Streak >= obj_Control.DEGRE_ATTENUATION and mean_Values[0]>0): #Si plus de 5 valeurs sont accumulées, et que leur valeur moyenne est plus que 0, on fait le control avec ces valeurs
        if(obj_Control.setpoint_Temp>0):
            controlTemp(mean_Values[0])
        elif(obj_Control.setpoint_Temp==0 and obj_Control.heating_On == True):
            obj_Control.heating_On = False
            obj_Control.toggle(obj_Control.PIN_CHAUFFAGE)
            
    if(obj_Control.good_Humid_Val_Streak >= obj_Control.DEGRE_ATTENUATION and mean_Values[1]>0):
        if(obj_Control.setpoint_Humid>0):
            controlHumid(mean_Values[1])
        elif(obj_Control.setpoint_Humid==0 and obj_Control.humidity_On == True):
            obj_Control.humidity_On = False
            obj_Control.toggle(obj_Control.PIN_HUMID)

    if(obj_Control.good_Dioxide_Val_Streak >= obj_Control.DEGRE_ATTENUATION and mean_Values[2]>0):
        if(obj_Control.setpoint_Dioxide>0):
            controlDioxide(mean_Values[2])

def checkTimeCycle():
    current_Time = datetime.now()
    current_Hour = current_Time.strftime("%H")
    current_Minute = current_Time.strftime("%M")
    lighting_State = False
    heure_Fin_Mod = obj_Control.cycle_Heure_Fin
    if(int(heure_Fin_Mod) == 0):
        heure_Fin_Mod = 24  #Pour simplifier les comparaisons, le 0 de minuit est mis a 24
    #print ("now {}:{} Start {}:{} End {}:{}".format(current_Hour,current_Minute,str(obj_Control.cycle_Heure_Dep),str(obj_Control.cycle_Minute_Dep),str(heure_Fin_Mod),str(obj_Control.cycle_Minute_Fin)))
    if(int(current_Hour) > int(obj_Control.cycle_Heure_Dep) and int(current_Hour) < int(heure_Fin_Mod)):
        lighting_State = True
    elif(int(current_Hour) == int(heure_Fin_Mod) and int(current_Minute) < int(obj_Control.cycle_Minute_Fin)):
        lighting_State = True
    elif(int(current_Hour) == int(obj_Control.cycle_Heure_Dep) and int(current_Minute) >= int(obj_Control.cycle_Minute_Dep) and int(current_Hour) < int(heure_Fin_Mod)):
        lighting_State = True
    elif(int(current_Hour) == int(obj_Control.cycle_Heure_Dep) and int(current_Minute) >= int(obj_Control.cycle_Minute_Dep) and int(current_Hour) == int(heure_Fin_Mod) and int(current_Minute) < int(obj_Control.cycle_Minute_Fin) ):
        lighting_State = True
    else:
        lighting_State = False

    toggleLighting(lighting_State)


if __name__ == "__main__":   #Debut du "Main"
    valeur_Moyennes = tuple
    obj_Control = LogicControl()
    obj_Control.getAPI()
    clientMQTT_Logic = mqtt.Client("clientMQTTLogicControl")   #Instanciation du client MQTT
    clientMQTT_Logic.on_message = on_message #Connections vers fonction callback MQTT
    clientMQTT_Logic.connect(obj_Control.BROKER_MQTT_ADDR) 
    print("Connecting to broker : " + obj_Control.BROKER_MQTT_ADDR)
    clientMQTT_Logic.subscribe(obj_Control.TOPIC_PROJET)
    print("Subscribing to topic : " + obj_Control.TOPIC_PROJET)
    clientMQTT_Logic.loop_start()
    obj_Control.setup_GPIO()


    while True:

        if(time()-obj_Control.TimeCyclePrevSec > obj_Control.TimeCycleInterval):
            obj_Control.TimeCyclePrevSec = time()
            data_Moyennes = meanDataLog()
            checkTimeCycle()

        try:
            if(obj_Control.serialHandle.is_open == 0):
                obj_Control.serialHandle.open()
                print("Port série ouvert avec succès")
            try:
                obj_Control.read_Serial()   #Tente de lire le port série
                controlSerre(data_Moyennes)

            except Exception as e:
                print("Erreur lors de la lecture du port série")
        except Exception as e:
            print("Erreur lors de l'ouverture du port série")

        if time()-obj_Control.ThingSpeakPrevSec > obj_Control.ThingSpeakInterval:     #Si fait plus de une minute depuis la dernière transmission sur ThingSpeak.
            obj_Control.ThingSpeakPrevSec = time()
            if(obj_Control.cle_API != "" and obj_Control.Flag_Thingspeak_Connected!=False):
                obj_Control.save_To_Thingspeak()
                

        sleep(0.05)