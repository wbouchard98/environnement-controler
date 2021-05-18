# coding=utf-8
#  @file   Project_EC_Class_Serre.py
#  @date   1 Mai 2021    
#  @author Simon Jourdenais
#  @brief  Ce programme gère l'affichage de l'interface utilisateur du moniteur/contrôleur de serre du projet Environnement Contrôlé
#          Attention : Un instance du programme "Projet_EC_Logic.py" doit avoir été préallablement au lancement de celui-ci .
#

#          Comme indiqué ci dessus, pour assurer le bon fonctionnement du programme, assurez vous que ce fichier se trouve dans le meme dossier que "Projet_EC_Class_Serre.py","Projet_EC_Logic.py",
#          "GUI_PEC_Monitor.ui", "GUI_PEC_Control.ui", "GUI_PEC_Config.ui" et "GUI_PEC_Admin.ui".
#
#  @matériel   Raspberry Pi 4 B 

import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt #import the client


class gestionSerre():
    #Section de "Defines"
    PIN_HUMID = 5
    PIN_EXT_LUM = 6
    PIN_FAN_BOITIER = 12
    PIN_DEL_COB = 13
    PIN_CHAUFFAGE = 17
    PIN_LED_FAN= 18
    PIN_EXT_FAN = 19
    PIN_DESHUMID = 22
    PIN_FAN_CONDUIT = 27
    NB_PRESETS = 10
    TOPIC_DATA_SERRE ="/Projet_EC/Sensorblock_1/Readings"
    TOPIC_GUI_INPUT_SET = "/Projet_EC/GUI/Setpoints"
    TOPIC_GUI_INPUT_CYCLE = "/Projet_EC/GUI/Cycle"
    TOPIC_GUI_API = "/Projet_EC/GUI/API"
    TOPIC_GUI_API_INIT = "/Projet_EC/GUI/API/Init"
    TOPIC_GUI_FLAGS = "/Projet_EC/GUI/Flags/#"
    TOPIC_GUI_FLAG_API = "/Projet_EC/GUI/Flags/API"
    TOPIC_PROJET = "/Projet_EC/#"
    BROKER_MQTT_ADDR = "127.0.0.1"
    #Fin de section de "Defines"

    Flag_Data_Error = False
    Flag_Thingspeak_Connected = False

    cle_API = ""
    base_url_ThingSpeak = ""
    
    setpoint_Temp = 0
    setpoint_Humid = 0
    setpoint_Int_Vid = 0
    setpoint_Dioxide = 0

    setpoint_Name = "Preset"
    cycle_Name = "Cycle 1"

    cycle_Heure_Dep = 0
    cycle_Minute_Dep = 0
    cycle_Heure_Fin = 0
    cycle_Minute_Fin = 0
    cycle_DEL_COB_Used = False
    cycle_DEL_Panel_Used = False

    current_Temp_DS = 66
    current_Temp_SHT = -1
    current_Humid = 33
    current_Dioxide = -1
    current_Tvoc = -1
    
    state_Humid = 0
    state_Panel_DEL = 0
    state_Fan_Boitier = 0
    state_DEL_COB = 0
    state_Chauffage = 0
    state_DEL_Fan = 0
    state_Ext_Fan = 0
    state_Vidangeur = 0
    state_Fan_Conduit = 0
    
    def __init__(self):
        self.getSetpoints()

    def setup_GPIO(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PIN_HUMID,GPIO.OUT)
        GPIO.setup(self.PIN_EXT_LUM,GPIO.OUT)
        GPIO.setup(self.PIN_FAN_BOITIER,GPIO.OUT)
        GPIO.setup(self.PIN_DEL_COB,GPIO.OUT)
        GPIO.setup(self.PIN_CHAUFFAGE,GPIO.OUT)
        GPIO.setup(self.PIN_LED_FAN,GPIO.OUT)
        GPIO.setup(self.PIN_EXT_FAN,GPIO.OUT)
        GPIO.setup(self.PIN_DESHUMID,GPIO.OUT)
        GPIO.setup(self.PIN_FAN_CONDUIT,GPIO.OUT)    


    def toggle(self, pin):
        self.setup_GPIO()
        
        state_GPIO = 0xFF
        
        if(pin == self.PIN_HUMID):
            self.state_Humid ^=1
            state_GPIO = self.state_Humid
            GPIO.output(self.PIN_EXT_FAN,state_GPIO)    #Allume la fan de lhumidificateur lorsque il est demarre
        elif(pin == self.PIN_EXT_LUM):
            self.state_Panel_DEL ^=1
            state_GPIO = self.state_Panel_DEL
        elif(pin == self.PIN_FAN_BOITIER):
            self.state_Fan_Boitier ^=1
            state_GPIO = self.state_Fan_Boitier           
        elif(pin == self.PIN_DEL_COB):
            self.state_DEL_COB ^=1
            state_GPIO = self.state_DEL_COB           
            GPIO.output(self.PIN_LED_FAN,state_GPIO)    #Allume la fan de la DEL lorsque elle demarre et l'éteint en meme temps
        elif(pin == self.PIN_CHAUFFAGE):
            self.state_Chauffage ^=1
            state_GPIO = self.state_Chauffage           
        elif(pin == self.PIN_LED_FAN):
            self.state_DEL_Fan ^=1
            state_GPIO = self.state_DEL_Fan           
        elif(pin == self.PIN_EXT_FAN):
            self.state_Ext_Fan ^=1
            state_GPIO = self.state_Ext_Fan           
        elif(pin == self.PIN_DESHUMID):
            self.state_Vidangeur ^=1
            state_GPIO = self.state_Vidangeur           
        elif(pin == self.PIN_FAN_CONDUIT):
            self.state_Fan_Conduit ^=1
            state_GPIO = self.state_Fan_Conduit             

        GPIO.output(pin,state_GPIO)

    #Fonction qui créé une table de presets de consignes

            
    # Fonction permettant d'aller chercher les dernières consignes connues du programme.
    def getSetpoints(self):
        try:
            file = open("Projet_EC_Current_Setpoint.txt", "rt") 
            setpoints = file.read() 
            file.close()
            if(setpoints!=""):
                try:
                    split_Setpoints = setpoints.split(" ") #Sépare la string et mets à jour les valeurs des consignes
                    self.setpoint_Temp = int(split_Setpoints[1])
                    self.setpoint_Humid = int(split_Setpoints[2])
                    self.setpoint_Dioxide = int(split_Setpoints[3])
                    self.setpoint_Int_Vid = int(split_Setpoints[4])
                except Exception as err:
                    print(str(err))
            elif(setpoints == ""):  #Verifie si du texte a ete extrait 
                self.saveSetpoints()
        except:
            self.saveSetpoints()    #Si on tombe en exception, cest que le fichier nexiste pas. SaveSetPoints va le creer.
    

    # Écrit les nouvelles consignes dans le fichier texte Projec_EC_Setpoint_List.txt
    def saveSetpoints(self):
        file= open("Projet_EC_Current_Setpoint.txt", "wt")
        file.write("Preset_Actuel "+str(self.setpoint_Temp) +" "+str(self.setpoint_Humid)+" "+str(self.setpoint_Dioxide)+" "+str(self.setpoint_Int_Vid)) #
        file.close()
    
    def getAPI(self):
        try:
            file = open("Projet_EC_API_ThingSpeak.txt", "rt") 
            cle_API_Read = file.read() 
            file.close()
            cle_API_Split = cle_API_Read.split(" ") #Isole la clé qui est forcémment bonne si elle est dans le fichier
            if(cle_API_Split[1] != ""):
                self.cle_API=cle_API_Split[1] #"F6AG8QMUBNAO57IL"  # Clé à William || "OTSESYSMRPRYTJFL" # Clé a Simon
                self.base_url_ThingSpeak="https://api.thingspeak.com/update?api_key={}".format(self.cle_API) 
                self.Flag_Thingspeak_Connected=True
        except:
            self.saveAPI()#Si on tombe en exception, cest que le fichier existe pas et saveApi le creera

    def saveAPI(self):
        file= open("Projet_EC_API_ThingSpeak.txt", "wt")
        file.write("Write_API_Actuel "+str(self.cle_API)) #Créé un fichier Template
        file.close()

    # Fonction permettant d'aller chercher les dernières consignes connues du programme.
    def getCycle(self):
        try:
            file = open("Projet_EC_Current_Cycle.txt", "rt") 
            cyclesContent = file.read() 
            file.close()
            if(cyclesContent!=""):
                try:
                    split_Cycle = cyclesContent.split(";") #Sépare la string et mets à jour les valeurs des consignes
                    self.cycle_Name = split_Cycle[0]
                    split_Cycle_Heure = split_Cycle[1].split("h")
                    self.cycle_Heure_Dep = int(split_Cycle_Heure[0])
                    self.cycle_Minute_Dep = int(split_Cycle_Heure[1])
                    split_Cycle_Heure = split_Cycle[2].split("h")
                    self.cycle_Heure_Fin = int(split_Cycle_Heure[0])
                    self.cycle_Minute_Fin = int(split_Cycle_Heure[1])
                except Exception as err:
                    print(str(err))
            elif(cyclesContent == ""):  #Verifie si du texte a ete extrait 
                self.saveSetpoints()
        except:
            self.saveSetpoints()    #Si on tombe en exception, cest que le fichier nexiste pas. SaveSetPoints va le creer.
    

    # Écrit les nouvelles consignes dans le fichier texte Projec_EC_Setpoint_List.txt
    def saveCycle(self):
        file= open("Projet_EC_Current_Cycle.txt", "wt")
        presetString = "{preset};{heure_Dep}h{minute_Dep};{heure_Fin}h{minute_Fin}".format(preset = self.cycle_Name,heure_Dep = self.cycle_Heure_Dep, minute_Dep = self.cycle_Minute_Dep,heure_Fin = self.cycle_Heure_Fin, minute_Fin=self.cycle_Minute_Fin)
        file.write(presetString) #
        file.close()