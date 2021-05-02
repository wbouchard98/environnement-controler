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
    TOPIC_SERRE ="/Projet_EC/Sensorblock_1/Readings"
    TOPIC_GUI_INPUT = "/Projet_EC/GUI"
    TOPIC_GUI_FLAGS = "/Projet_EC/GUI/Flags/#"
    TOPIC_GUI_FLAG_API = "/Projet_EC/GUI/Flags/API"
    TOPIC_PROJET = "/Projet_EC"
    BROKER_MQTT_ADDR = "127.0.0.1"
    #Fin de section de "Defines"

    Flag_Data_Error = False

    clientMQTTSerre = mqtt.Client("clientMQTTSerre") #client MQTT lié au échanges entre les données de la serre et l'affichage
    api_Key = ""
    
    setpoint_Temp = 0
    setpoint_Humid = 0
    setpoint_Name = "Preset"
    
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
        self.setup_GPIO()
        self.initSetpointList()
        self.getSetpoints()
        #self.connectMQTT()

    def setup_GPIO(self):
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
        elif(pin == self.PIN_EXT_LUM):
            self.state_Panel_DEL ^=1
            state_GPIO = self.state_Panel_DEL
        elif(pin == self.PIN_FAN_BOITIER):
            self.state_Fan_Boitier ^=1
            state_GPIO = self.state_Fan_Boitier           
        elif(pin == self.PIN_DEL_COB):
            self.state_DEL_COB ^=1
            state_GPIO = self.state_DEL_COB           
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

        #print("Num de pin : "+str(pin)+" Etat : "+str(state_GPIO))
        GPIO.output(pin,state_GPIO)

    def initSetpointList(self):
        file = open("Projet_EC_Setpoint_List.txt", "rt+")
        check = file.read()
        file.close()
        if(check == ""):
            file = open("Projet_EC_Setpoint_List.txt", "w")
            for x in range(1,11):
                if(x != 1):
                    file.write("\n")
                file.write("Preset_"+x+" 0 0")
            file.close
            
    # Fonction permettant d'aller chercher les dernières consignes connues du programme.
    def getSetpoints(self):
        try:
            file = open("Projet_EC_Current_Setpoint.txt", "rt+") 
            setpoints = file.read() 
            file.close()
            if(setpoints!=""):
                try:
                    split_Setpoints = setpoints.split(" ") #Sépare la string et mets à jour les valeurs des consignes
                    self.setpoint_Temp = int(split_Setpoints[1])
                    self.setpoint_Humid = int(split_Setpoints[2])
                except:
                    print(str(err))
            elif(setpoints == ""):  #Verifie si du texte a ete extrait 
                self.saveSetpoints()
        except:
            self.saveSetpoints()    #Si on tombe en exception, cest que le fichier nexiste pas. SaveSetPoints va le creer.
    

    # Écrit les nouvelles consignes dans le fichier texte Projec_EC_Setpoint_List.txt
    def saveSetpoints(self):
        file= open("Projet_EC_Current_Setpoint.txt", "w+")
        file.write("Preset_Actuel "+str(self.setpoint_Temp) +" "+str(self.setpoint_Humid)) # Esapce permettant l'identification des deux valeurs plus facilement.
        file.close()
    
    

