# coding=utf-8
#  @file   Project_EC_GUI.py
#  @date   1 Mai 2021    
#  @author Simon Jourdenais
#  @brief  Ce programme gère l'affichage de l'interface utilisateur du moniteur/contrôleur de serre du projet Environnement Contrôlé
#          Attention : Un instance du programme "Projet_EC_Logic.py" doit avoir été préallablement au lancement de celui-ci .
#
#          Dans ce programme, 4 grandes classes majeures sont a noter:
#
#           1- WindowMonitor
#               Cette classe utilise le fichier "GUI_PEC_Monitor.ui" pour charger la fenetre à créer. Les fichier .ui sont des fichiers contenant du code généré par le programme QT
#               Designer. Ce programme ne lie cependant pas le code au différents évènement, contrairement à Visual Studio et le C#, où la fenêtre et le code sont créé et écrit dans
#               un seul et même programme.
#               Donc ce que l'on retrouve dans la fonction d'initialisation de cette classe et celle des 3 autres de cette liste, est l'attachement des évènements des boutons de 
#               navigation du menu au fonctions permettant l'affichage des différentes pages.
#        
#               Lorsque le programme fonctionne, il est possible de voir les données des provenant du bloc de capteurs sur cette fenêtre.
#               #Il serait interressant d'y voir aussi si le chauffage est activé du au PID, même chose pour l'humidité
#
#           2- WindowControl
#               La fenetre que gère cette classe consiste à la fenêtre de contrôle des consignes de température et d'humidité. La plupart des fonctions de la classe WindowControl sont liés
#               à l'ouverture, la lecture et l'enregistrement de valeurs de consignes. 
#
#           3- WindowConfig
#               Cette fenêtre est séparée en 3 parties. La première est dédiée a la connexion a ThingSpeak, pour l'enregistrement des données en ligne, la section du millieu permettrait 
#               normalement de se connecter au réseaux wifi, mais puisque le temps manque, cette partie a été omise, et la dernière partie affiche des données utiles, soit pour débogger 
#               ou pour configurer.
#               La configuration du compte ThingSpeak dans le programme nécessite forcement au moins une connection à distance ou de brancher un clavier sur le Raspberry Pi.
#               En appuyant sur "Valider" lors de la configuration du ThingSpeak, ce programme envoi la clé par MQTT sur le topic /Projet_EC/GUI au programme de contrôle "Projet_EC_Logic.py" 
#               pour qu'il puisse tester la connexion puis ce dernier envoi une confirmation sur le topic /Projet_EC/GUI/Flags/API
#               
#           4- WindowAdmin
#               La dernière fenêtre permet de tester chacune des sorties controlées par le programme. Encore une fois dût au manque de temps, nous n'avons pas réussi a tout implementer les
#               fonctionalité voulues et certaines sont désactivées (en grise) sur cette page de l'interface utilisateur.
#
#          Dans ces 4 classes se trouvent la fonction loadUi, qui permet de charger
#          Chacune de ces classes fonctionnent en accedant a un objet commun d'une classe clé dans ce programme, la classe gestionSerre. Elle est définie dans son propre fichier distinct,
#          ce dernier nommé "Projet_EC_Class_Serre.py".             
#           
#          De plus, ce programme utilise MQTT pour communiquer entre le programme de contrôle "Projet_EC_Logic.py" pour échanger les valeurs lues des capteurs,
#          
#          Comme indiqué ci dessus, pour assurer le bon fonctionnement du programme, assurez vous que ce fichier se trouve dans le meme dossier que "Projet_EC_Class_Serre.py","Projet_EC_Logic.py",
#          "GUI_PEC_Monitor.ui", "GUI_PEC_Control.ui", "GUI_PEC_Config.ui" et "GUI_PEC_Admin.ui".
#
#  @matériel   Raspberry Pi 4 B, Écran 7" Touchscreen 



import sys, RPi.GPIO as GPIO, json
import paho.mqtt.client as mqtt #import the client
from time import sleep
from Projet_EC_Class_Serre import gestionSerre
from subprocess import check_output
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QDialog


  


WindowMonitor_Index = 0
WindowControl_Index = 1
WindowParam_Index = 2
WindowAdmin_Index = 3

def goto_Monitor():
    screenWidget.setCurrentIndex(WindowMonitor_Index)
def goto_Setpoints():
    controlWindow.updateSetpointsLCD()
    screenWidget.setCurrentIndex(WindowControl_Index)
def goto_Param():
    screenWidget.setCurrentIndex(WindowParam_Index)
def goto_Outils():
    screenWidget.setCurrentIndex(WindowAdmin_Index)


class WindowMonitor(QMainWindow):
    

    def __init__(self):
        super(WindowMonitor,self).__init__()
        loadUi("GUI_PEC_Monitor.ui",self)
        self.btn_Monitor_Menu.setStyleSheet("background-color:#c5c5c6")
        self.btn_Outils_Menu.clicked.connect(goto_Outils)
        self.btn_Setpoints_Menu.clicked.connect(goto_Setpoints)
        self.btn_Param_Menu.clicked.connect(goto_Param)
        self.lcd_Temp.display("0.00")
        self.lcd_Humid.display("0.00")
        self.lcd_Dioxide.display("0.00")
        self.lcd_TVOC.display("0.00")



class WindowControl(QMainWindow):
    
    def __init__(self):
        super(WindowControl,self).__init__()
        loadUi("GUI_PEC_Control.ui",self)
        self.getPresets()
        self.btn_Setpoints_Menu.setStyleSheet("background-color:#c5c5c6")
        self.btn_Outils_Menu.clicked.connect(goto_Outils)
        self.btn_Monitor_Menu.clicked.connect(goto_Monitor)
        self.btn_Param_Menu.clicked.connect(goto_Param)

        self.btn_Save_Set.clicked.connect(self.btn_Save_Set_Clicked)
        self.Btn_Load_Saved_Set.clicked.connect(self.btn_Load_Saved_Set_Clicked)
        self.btn_Augment_Temp.clicked.connect(self.btn_Augment_Temp_Clicked)
        self.btn_Augment_Humid.clicked.connect(self.btn_Augment_Humid_Clicked)
        self.btn_Decrement_Temp.clicked.connect(self.btn_Decrement_Temp_Clicked)
        self.btn_Decrement_Humid.clicked.connect(self.btn_Decrement_Humid_Clicked)
    
    def btn_Augment_Temp_Clicked(self):
        if(serre.setpoint_Temp <=29):
            serre.setpoint_Temp += 1
        self.lcd_Temp_Set.display(str(serre.setpoint_Temp))
        serre.saveSetpoints()

    def btn_Decrement_Temp_Clicked(self):
        if(serre.setpoint_Temp >=1):
            serre.setpoint_Temp -= 1
        self.lcd_Temp_Set.display(str(serre.setpoint_Temp))
        serre.saveSetpoints()

    def btn_Augment_Humid_Clicked(self):
        if(serre.setpoint_Humid <=90):       #Max de 95 % humidité
            serre.setpoint_Humid += 5
        self.lcd_Humid_Set.display(str(serre.setpoint_Humid))
        serre.saveSetpoints()

    def btn_Decrement_Humid_Clicked(self):
        if(serre.setpoint_Humid >=5):
            serre.setpoint_Humid -= 5
        self.lcd_Humid_Set.display(str(serre.setpoint_Humid))
        serre.saveSetpoints()
    
    def btn_Save_Set_Clicked(self):
        file = open("Projet_EC_Setpoint_List.txt", "rt+")
        contenuFichier = file.read()
        contenuFichier = contenuFichier.rstrip()
        setpointLines = contenuFichier.split("\n")
        file.close()
        file = open("Projet_EC_Setpoint_List.txt", "w")
        for x in range(0,len(setpointLines)):
            if(x != 0):
                file.write("\n")
            setpointLineSplit=setpointLines[x].split(" ")
            if(setpointLineSplit[0] == self.cb_Saved_Set.currentText()):
                presetString = "{preset} {set_temp} {set_humid}".format(preset = setpointLineSplit[0],set_temp = serre.setpoint_Temp,set_humid = serre.setpoint_Humid)
                setpointLines[x] = presetString
            file.write(setpointLines[x])
        

    def btn_Load_Saved_Set_Clicked(self):
        file = open("Projet_EC_Setpoint_List.txt", "rt")
        contenuFichier = file.read()
        setpointLines = contenuFichier.split("\n")
        for lines in setpointLines:
            setpointLineSplit=lines.split(" ")
            if(setpointLineSplit[0] == self.cb_Saved_Set.currentText()):
                serre.setpoint_Name=setpointLineSplit[0]
                serre.setpoint_Temp=int(setpointLineSplit[1])
                serre.setpoint_Humid=int(setpointLineSplit[2])
        self.updateSetpointsLCD()
        serre.saveSetpoints()

    def getPresets(self):
        file = open("Projet_EC_Setpoint_List.txt", "rt")
        contenuFichier = file.read()
        setpointLines = contenuFichier.split("\n")
        for lines in setpointLines:
            setpointLineSplit=lines.split(" ")
            if(setpointLineSplit[0] != ""):
                self.cb_Saved_Set.addItem(setpointLineSplit[0])
        
    def updateSetpointsLCD(self):
        #Affichage des valeurs
        self.lcd_Temp_Set.display(str(serre.setpoint_Temp))
        self.lcd_Humid_Set.display(str(serre.setpoint_Humid))
        


class WindowConfig(QMainWindow):
    def __init__(self):
        super(WindowConfig,self).__init__()
        loadUi("GUI_PEC_Config.ui",self)
        self.btn_Param_Menu.setStyleSheet("background-color:#c5c5c6")
        self.btn_Outils_Menu.clicked.connect(goto_Outils)
        self.btn_Setpoints_Menu.clicked.connect(goto_Setpoints)
        self.btn_Monitor_Menu.clicked.connect(goto_Monitor)
        self.lbl_Info_Erreurs.takeItem(0)
        self.lbl_Info_Erreurs.insertItem(0,("Addresse IP : " +str(check_output(['hostname', '-I']),'utf-8')))
        self.btn_Thingspeak_Cle.clicked.connect(self.btn_Thingspeak_Cle_Clicked)

    def btn_Thingspeak_Cle_Clicked(self):

        api_String = '{"api_key":""}'
        json_Data = json.loads(api_String)
        json_Data["api_key"]=self.tb_Thingspeak_Cle.text()
        clientMQTT.publish(topic=serre.TOPIC_GUI_INPUT, payload=json.dumps(json_Data)) #Publie sur /test le JSON des valeurs de capteurs.
        print("Key Sent")
        

class WindowAdmin(QMainWindow):
    def __init__(self):
        super(WindowAdmin,self).__init__()
        loadUi("GUI_PEC_Admin.ui",self)
        self.btn_Outils_Menu.setStyleSheet("background-color:#c5c5c6")
        self.btn_Monitor_Menu.clicked.connect(goto_Monitor)
        self.btn_Setpoints_Menu.clicked.connect(goto_Setpoints)
        self.btn_Param_Menu.clicked.connect(goto_Param)

        self.btn_DEL_Panel.clicked.connect(self.btn_DEL_Panel_Clicked)
        self.btn_Fan_Boitier.clicked.connect(self.btn_Fan_Boitier_Clicked)
        self.btn_Chauffage.clicked.connect(self.btn_Chauffage_Clicked)
        self.btn_Aeration.clicked.connect(self.btn_Aeration_Clicked)
        self.btn_LED.clicked.connect(self.btn_LED_Clicked)
        self.btn_Fan_DEL.clicked.connect(self.btn_Fan_DEL_Clicked)
        self.btn_Vidange.clicked.connect(self.btn_Vidange_Clicked)
        self.btn_Humid.clicked.connect(self.btn_Humid_Clicked)
        self.slider_int_Fan_DEL.valueChanged.connect(self.slider_int_Fan_DEL_Changed)
        self.slider_int_Fan_Boitier.valueChanged.connect(self.slider_int_Fan_Boitier_Changed)
        
        self.lbl_int_Humid.setText("N/A")
        self.lbl_int_Vidange.setText("N/A")
        self.lbl_int_Aeration.setText("N/A")
        self.lbl_int_Chauffage.setText("N/A")
        self.lbl_int_Fan_DEL.setText("50")
        self.lbl_int_Fan_Boitier.setText("50")
        self.lbl_int_Unused.setText("N/A")
    
    def btn_DEL_Panel_Clicked(self):
        serre.toggle(serre.PIN_EXT_LUM)
        if(serre.state_Panel_DEL==1):
            self.btn_DEL_Panel.setText("Off")
        elif serre.state_Panel_DEL==0:
            self.btn_DEL_Panel.setText("On")
    def btn_Fan_Boitier_Clicked(self):
        serre.toggle(serre.PIN_FAN_BOITIER)
        if(serre.state_Fan_Boitier==1):
            self.btn_Fan_Boitier.setText("Off")
        elif serre.state_Fan_Boitier==0:
            self.btn_Fan_Boitier.setText("On")
    def btn_Chauffage_Clicked(self):
        serre.toggle(serre.PIN_CHAUFFAGE)
        if(serre.state_Chauffage==1):
            self.btn_Chauffage.setText("Off")
        elif serre.state_Chauffage==0:
            self.btn_Chauffage.setText("On")
    def btn_Aeration_Clicked(self):
        serre.toggle(serre.PIN_FAN_CONDUIT)
        if(serre.state_Fan_Conduit==1):
            self.btn_Aeration.setText("Off")
        elif serre.state_Fan_Conduit==0:
            self.btn_Aeration.setText("On")
    def btn_LED_Clicked(self):
        serre.toggle(serre.PIN_DEL_COB)
        if(serre.state_DEL_COB==1):
            self.btn_LED.setText("Off")
        elif serre.state_DEL_COB==0:
            self.btn_LED.setText("On")
    def btn_Fan_DEL_Clicked(self):
        serre.toggle(serre.PIN_LED_FAN)
        if(serre.state_DEL_Fan==1):
            self.btn_Fan_DEL.setText("Off")
        elif serre.state_DEL_Fan==0:
            self.btn_Fan_DEL.setText("On")
    def btn_Vidange_Clicked(self):
        serre.toggle(serre.PIN_DESHUMID)
        if(serre.state_Vidangeur==1):
            self.btn_Vidange.setText("Off")
        elif serre.state_Vidangeur==0:
            self.btn_Vidange.setText("On")
    def btn_Humid_Clicked(self):
        serre.toggle(serre.PIN_HUMID)
        if(serre.state_Humid==1):
            self.btn_Humid.setText("Off")
        elif serre.state_Humid==0:
            self.btn_Humid.setText("On")     
    def slider_int_Fan_DEL_Changed(self):
        try:
            self.lbl_int_Fan_DEL.setText(str(self.slider_int_Fan_DEL.value()))
        except Exception as err:
            print(str(err))
    def slider_int_Fan_Boitier_Changed(self):
        try:
            self.lbl_int_Fan_Boitier.setText(str(self.slider_int_Fan_Boitier.value()))
        except Exception as err:
            print(str(err))

def meanTempShowLCD(mqttMessageJSON):
    mean_Temp = 0.0
    if(int(mqttMessageJSON["SHT"]["temp"]) != -1 and int(mqttMessageJSON["DS"]["temp"]) != -1 ):
        mean_Temp =(float(mqttMessageJSON["SHT"]["temp"])+float(mqttMessageJSON["DS"]["temp"]))/2
    elif(int(mqttMessageJSON["SHT"]["temp"]) == -1):
        mean_Temp = float(mqttMessageJSON["DS"]["temp"])
    elif(int(mqttMessageJSON["DS"]["temp"]) == -1):
        mean_Temp = float(mqttMessageJSON["SHT"]["temp"])
    else:
        mean_Temp = -1
        serre.Flag_Data_Error = True        #Set le flag d'erreur de données a vrai dans l'objet serre, est réutilisé pour indiquer a l'utilisateur l'erreur potentielle dans la page de parametres (config)
    #Affichage des valeurs reçu par MQTT
    monitorWindow.lcd_Temp.display("%0.2f"%mean_Temp)
    monitorWindow.lcd_Humid.display(mqttMessageJSON["SHT"]["hum"])
    monitorWindow.lcd_Dioxide.display(mqttMessageJSON["CSS811"]["CO2"])
    monitorWindow.lcd_TVOC.display(mqttMessageJSON["CSS811"]["TVOC"])
    

def on_message(client, userdata, msg):
    try:
        dataMQTT = msg.payload 
        mqttMessageJSON = json.loads(dataMQTT) #transforme le message en JSON
        #print(msg.topic)
        if (msg.topic==serre.TOPIC_GUI_FLAG_API):
            #print(mqttMessageJSON['api_ok'])
            if(mqttMessageJSON['api_ok']) == True:
                configWindow.lbl_Info_Erreurs.takeItem(1)
                configWindow.lbl_Info_Erreurs.insertItem(1,("Clé Thingspeak valide"))
            elif(mqttMessageJSON['api_ok']) == False:
                configWindow.lbl_Info_Erreurs.takeItem(1)
                configWindow.lbl_Info_Erreurs.insertItem(1,("Clé Thingspeak invalide "))
        elif(msg.topic == serre.TOPIC_SERRE):
            meanTempShowLCD(mqttMessageJSON)
    except Exception as err:
        print(err)


clientMQTT = mqtt.Client("clientMQTT") #client MQTT lié au échanges entre les données de la serre et l'affichage

        

if __name__ == "__main__":   #Debut du "Main"
    #Init
    serre = gestionSerre() #Instanciation d'un objet de Controle D'environnement. Elle est la classe majeure du programm
    clientMQTT.connect(serre.BROKER_MQTT_ADDR)
    clientMQTT.subscribe([(serre.TOPIC_SERRE,0),(serre.TOPIC_GUI_FLAGS,0)])
    clientMQTT.on_message = on_message
    #Setup GUI
    app = QApplication(sys.argv)
    screenWidget = QtWidgets.QStackedWidget() #Widget qui contient toutes les fenetres et permet de switcher entre fenetres
    monitorWindow = WindowMonitor() #Instanciation d'un objet de chaque type de fenetres    
    controlWindow = WindowControl()
    configWindow = WindowConfig()
    adminWindow = WindowAdmin()
    screenWidget.addWidget(monitorWindow)   #Ajoute les fenetres au Gestionnaire screenWidget
    screenWidget.addWidget(controlWindow)
    screenWidget.addWidget(configWindow)
    screenWidget.addWidget(adminWindow)


    clientMQTT.loop_start()  
    
    #screenWidget.showFullScreen()         #Affiche en plein ecran ( PROJET MODE )
    screenWidget.showMaximized()         #Affiche le GUI en maximizé ( Bloquant )

    GPIO.cleanup()
    
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")





