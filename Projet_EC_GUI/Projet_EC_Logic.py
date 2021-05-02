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


import json, serial, threading
from enum import IntEnum
from time import time, sleep
from urllib.request import urlopen
import paho.mqtt.client as mqtt #import the client1
import paho.mqtt.publish as publish
#from simple_pid import PID

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

class LogicControl():
    #Defines 
    API_KEY_LENGTH = 16
    BROKER_ADDR = "127.0.0.1"
    TOPIC_SERRE = "/Projet_EC/Sensorblock_1/Readings"
    TOPIC_GUI_INPUT = "/Projet_EC/GUI"
    TOPIC_GUI_FLAGS = "/Projet_EC/GUI/Flags/#"
    TOPIC_GUI_FLAG_API = "/Projet_EC/GUI/Flags/API"
    TOPIC_PROJET = "/Projet_EC/#"
    #EndDefines
    Flag_Thingspeak_Connected = False

    temp_DS=0
    temp_SHT=0
    humid_SHT=0
    dioxide_CCS =0
    tvoc_CCS =0

    time_Lights_Off = "" #strptime() et strftime
    time_Lights_On = ""
    setpoint_Humid = 0xFF
    setpoint_Temp = 0xFF
    #pid_HeatMat = PID(2,1,5, setpoint=self.setpoint_Temp)
    #pid_HeatMat.output_limits = (0, 255)

    WRITE_API = ""
    BASE_URL = ""

    SensorPrevSec = 0  # Variable qui prend le temps de référence pour délais d'envoie MQTT
    SensorInterval = 2 # 2 secondes de délais 
    ThingSpeakPrevSec = 0 #Variable qui prend le temps référence pour délais d'envoie ThingSpeak
    ThingSpeakInterval = 15 # 15 secondes de délais entre uploads

    serialHandle = serial.Serial('/dev/ttyUSB0', 9600)  #Initialise la connection avec le ARDUINO NANO

    def __init__(self):
        pass

    def setAPI_URL(self, api_key):
        self.WRITE_API=api_key #"F6AG8QMUBNAO57IL"  # Clé à William || "OTSESYSMRPRYTJFL" # Clé a Simon
        self.BASE_URL="https://api.thingspeak.com/update?api_key={}".format(self.WRITE_API) 

    def resetAPI_URL(self):
        self.WRITE_API="" #"F6AG8QMUBNAO57IL"  # Clé à William || "OTSESYSMRPRYTJFL" # Clé a Simon
        self.BASE_URL="https://api.thingspeak.com/update?api_key={}".format(self.WRITE_API) 
    
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
                decodedDataSerial = decodedDataSerial.replace('\r', '') #enleve les saut de ligne
                decodedDataSerial = decodedDataSerial.replace('\0', '') #enleve les saut de ligne
                splitDataSerial = decodedDataSerial.split(" ")
                for split_Byte in splitDataSerial: 
                    if(split_Byte.rstrip() != "" ):
                        bytes_List.append(split_Byte)
                        
                if(self.verifyTrame(bytes_List)==True):
                    self.temp_DS = float((bytes_List[e_bytes.temp_DS_MSB]+"."+bytes_List[e_bytes.temp_DS_LSB]))
                    self.temp_SHT = float((bytes_List[e_bytes.temp_SEN_MSB]+"."+bytes_List[e_bytes.temp_SEN_LSB]))
                    self.humid_SHT = float((bytes_List[e_bytes.humid_SEN_MSB]+"."+bytes_List[e_bytes.humid_SEN_LSB]))
                    self.dioxide_CCS = int((bytes_List[e_bytes.ppm_Dioxide_MSB]+bytes_List[e_bytes.ppm_Dioxide_LSB]))
                    self.tvoc_CCS = int((bytes_List[e_bytes.ppb_TVOC_MSB]+bytes_List[e_bytes.ppb_TVOC_LSB]))
                    publishDataToGUI()
                self.serialHandle.flushInput()
                

        except Exception as err:
            print(str(err))
            self.serialHandle.close() #Ferme port série




    def saveAPI(self):
        file= open("Projet_EC_API_ThingSpeak.txt", "w+")
        file.write("Write_API_Actuel "+str(self.WRITE_API)) # Esapce permettant l'identification des deux valeurs plus facilement.
        file.close()

    def sendAPI_Key(self, key):
        api_String = '{"serre_GUI_api_key":""}'
        json_Data = json.loads(api_String)
        json_Data["serre_GUI_api_key"] = key
        clientMQTT.publish(topic=self.TOPIC_SERRE, payload=json.dumps(json_Data)) 

    def getAPI(self):
        try:
            file = open("Projet_EC_API_ThingSpeak.txt", "rt") 
            cle_API_Read = file.read() 
            print(cle_API_Read)
            file.close()
            cle_API_Split = setpoints.split(" ") #Sépare la string et mets à jour les valeurs des consignes
            
            self.setAPI_URL(cle_API_Split[1])
            self.Flag_Thingspeak_Connected=True
            self.sendAPI_Key(cle_API_Split[1])
            print(cle_API_Read)
        except:
            self.saveAPI()#Si on tombe en exception, cest que le fichier existe pas et saveApi le creera
    
#Envoi les données vers ThingSpeak par URL. Contient: Température du DS18B20, Température et humidité du SEN0227, la concentartion de CO2 et le TVOC du CCS811.
#Données envoyées à la minute. ThingSpeak nous envoie le numéro de l'entré en retour si notre envoie c'est bien passé.
    def save_To_Thingspeak(self):
        try:
            thingspeakHttp = self.BASE_URL + "&field1={:.2f}&field2={:.2f}&field3={:.2f}&field4={:f}&field5={:f}".format(self.temp_DS,self.temp_SHT,self.humid_SHT,self.dioxide_CCS,self.tvoc_CCS,) #Formatage de la string URL pour l'envoie vers ThingSpeak.
            conn = urlopen(thingspeakHttp) #Envoie les infos vers ThingSpeak
            code_Retour = conn.read()
            print("Saved to ThingSpeak API ",self.WRITE_API + " - Confirmation : Entry # "+ str(code_Retour))
            if(self.Flag_Thingspeak_Connected != True):
                self.Flag_Thingspeak_Connected = True
                self.saveAPI()
                sendFlagThingspeakConnected(obj_Control.Flag_Thingspeak_Connected)#Envoi le flag True sur le channel MQTT /Projet_EC/GUI/Flags/API
            conn.close()
        except Exception as err:
            self.Flag_Thingspeak_Connected = False
            sendFlagThingspeakConnected(self.Flag_Thingspeak_Connected) #Send code erreur au GUI si Fail URLRequest
            try:
                conn.close()
            except:
                pass
            print(str(err))

    def verifyTempPID(self):
        if(self.temp_DS != -1):
            #control = self.pid_HeatMat(self.temp_DS)
            #print(control)
            pass
        else:
            pass
            #print("TEMP CONTROL ERROR")

def sendFlagThingspeakConnected(bool_Api):
    api_String = '{"api_ok":""}'
    json_Data = json.loads(api_String)
    if(bool_Api == True):
        json_Data["api_ok"] = True
    elif(bool_Api == False):
        json_Data["api_ok"] = False
    clientMQTT.publish(topic=obj_Control.TOPIC_GUI_FLAG_API, payload=json.dumps(json_Data)) #Publie sur /test le JSON des valeurs de capteurs.
    print("Flag Validité TS Sent : "+ str(bool_Api))   

def publishDataToGUI():
    try:
        json_data = json.loads('{"DS": {"temp": '+str(obj_Control.temp_DS)+'}, "SHT": {"temp": '+str(obj_Control.temp_SHT)+', "hum": '+str(obj_Control.humid_SHT)+'}, "CSS811": {"CO2": '+str(obj_Control.dioxide_CCS)+', "TVOC": '+str(obj_Control.tvoc_CCS)+'}}')
        clientMQTT.publish(topic=obj_Control.TOPIC_SERRE, payload=json.dumps(json_data)) #Publie sur /Projet_EC/Sensorblock_1/Readings le JSON des valeurs lues des capteurs
        
    except Exception as err:
        print(str(err))

def on_message(client, userdata, msg):
    try:
        incomingMQTT = msg.payload.decode()  #prend le message reçu #'{"DS": {"temp": 25}}'
        incomingMQTT = json.loads(incomingMQTT) #Formatte le message sous format JSON
        if(msg.topic == obj_Control.TOPIC_GUI_INPUT):
            try:
                if len(incomingMQTT['api_key']) != obj_Control.API_KEY_LENGTH:
                    raise Exception()
                print("Clé API reçue : "+str(incomingMQTT['api_key']))
                obj_Control.setAPI_URL(str(incomingMQTT['api_key']))
            except Exception as err:
                print("Clé API fautive")
                obj_Control.resetAPI_URL()
                obj_Control.Flag_Thingspeak_Connected=False
                sendFlagThingspeakConnected(obj_Control.Flag_Thingspeak_Connected) #Envoi le flag False sur le channel MQTT /Projet_EC/GUI/Flags/API
                print(str(err))
        if(msg.topic == obj_Control.TOPIC_SERRE):
            pass
    except Exception as err:
        print(err)



#"F6AG8QMUBNAO57IL"  # Clé à William "OTSESYSMRPRYTJFL" # Clé a Simon

if __name__ == "__main__":   #Debut du "Main"
    obj_Control = LogicControl()
    obj_Control.getAPI()
    clientMQTT = mqtt.Client("clientMQTTLogicControl")   #Création du client MQTT
    clientMQTT.on_message = on_message #Création des connections vers les fonctions des évênnements MQTT
    clientMQTT.connect(obj_Control.BROKER_ADDR) 
    clientMQTT.subscribe(obj_Control.TOPIC_PROJET)
    clientMQTT.loop_start()

    while True:
        if time()-obj_Control.SensorPrevSec > obj_Control.SensorInterval:  #Si + de deux secondes
            obj_Control.SensorPrevSec = time()
            if(obj_Control.serialHandle.is_open == 0):
                obj_Control.serialHandle.open()
            try:
                obj_Control.read_Serial()   #Lit port série
            except Exception as e:
                pass

            #self.verifyTempPID()
            
        if time()-obj_Control.ThingSpeakPrevSec > obj_Control.ThingSpeakInterval:     #Si fait plus de une minute depuis la dernière transmission sur ThingSpeak.
            obj_Control.ThingSpeakPrevSec = time()
            if(obj_Control.WRITE_API != ""):
                obj_Control.save_To_Thingspeak()
                

        sleep(0.05)