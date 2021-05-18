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
from Projet_EC_Class_Serre import gestionSerre
from subprocess import check_output
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication 


WindowMonitor_Index = 0 #defines d'index pour les fenetres
WindowControl_Index = 1
WindowParam_Index = 2
WindowAdmin_Index = 3
WindowLightTimer_Index = 4

def goto_Monitor(): #fonctions pour changer de fenêtres
    screenWidget.setCurrentIndex(WindowMonitor_Index)
def goto_Setpoints():
    controlWindow.updateSetpointsLCD()
    screenWidget.setCurrentIndex(WindowControl_Index)
def goto_Param():
    screenWidget.setCurrentIndex(WindowParam_Index)
def goto_Outils():
    screenWidget.setCurrentIndex(WindowAdmin_Index)
def goto_LightTimer():
    screenWidget.setCurrentIndex(WindowLightTimer_Index)

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
        self.btn_Monitor_Menu.clicked.connect(goto_Monitor)
        self.btn_Config_Light.clicked.connect(goto_LightTimer)

        self.btn_Save_Set.clicked.connect(self.btn_Save_Set_Clicked)
        self.Btn_Load_Saved_Set.clicked.connect(self.btn_Load_Saved_Set_Clicked)
        self.btn_Augment_Temp.clicked.connect(self.btn_Increment_Temp_Clicked)
        self.btn_Augment_Humid.clicked.connect(self.btn_Increment_Humid_Clicked)
        self.btn_Decrement_Temp.clicked.connect(self.btn_Decrement_Temp_Clicked)
        self.btn_Decrement_Humid.clicked.connect(self.btn_Decrement_Humid_Clicked)


        self.btn_Augment_Int_Vid.clicked.connect(self.btn_Augment_Int_Vid_Clicked)
        self.btn_Decrement_Int_Vid.clicked.connect(self.btn_Decrement_Int_Vid_Clicked)
        self.btn_Augment_Dioxide.clicked.connect(self.btn_Augment_Dioxide_Clicked)
        self.btn_Decrement_Dioxide.clicked.connect(self.btn_Decrement_Dioxide_Clicked)


    def btn_Increment_Temp_Clicked(self):
        if(serre.setpoint_Temp <=29):
            serre.setpoint_Temp += 1
        self.lcd_Temp_Set.display(str(serre.setpoint_Temp))
        serre.saveSetpoints()
        sendSetpoints()

    def btn_Decrement_Temp_Clicked(self):
        if(serre.setpoint_Temp >=1):
            serre.setpoint_Temp -= 1
        self.lcd_Temp_Set.display(str(serre.setpoint_Temp))
        serre.saveSetpoints()
        sendSetpoints()

    def btn_Increment_Humid_Clicked(self):
        if(serre.setpoint_Humid <=90):       #Max de 95 % humidité
            serre.setpoint_Humid += 5
        self.lcd_Humid_Set.display(str(serre.setpoint_Humid))
        serre.saveSetpoints()
        sendSetpoints()

    def btn_Decrement_Humid_Clicked(self):
        if(serre.setpoint_Humid >=5):
            serre.setpoint_Humid -= 5
        self.lcd_Humid_Set.display(str(serre.setpoint_Humid))
        serre.saveSetpoints()
        sendSetpoints()
    
    def btn_Augment_Int_Vid_Clicked(self):
        if(serre.setpoint_Int_Vid<24):
            serre.setpoint_Int_Vid+=1
        self.lcd_Inter_Vid_Set.display(str(serre.setpoint_Int_Vid))
        serre.saveSetpoints()
        sendSetpoints()

    def btn_Decrement_Int_Vid_Clicked(self):
        if(serre.setpoint_Int_Vid>0):
            serre.setpoint_Int_Vid-=1
        self.lcd_Inter_Vid_Set.display(str(serre.setpoint_Int_Vid))
        serre.saveSetpoints()
        sendSetpoints()

    def btn_Augment_Dioxide_Clicked(self):
        if(serre.setpoint_Dioxide<16000):
            serre.setpoint_Dioxide+=1000
        self.lcd_Dioxide_Set.display(str(serre.setpoint_Dioxide))
        serre.saveSetpoints()
        sendSetpoints()

    def btn_Decrement_Dioxide_Clicked(self):
        if(serre.setpoint_Dioxide>0):
            serre.setpoint_Dioxide-=1000
        self.lcd_Dioxide_Set.display(str(serre.setpoint_Dioxide))
        serre.saveSetpoints()
        sendSetpoints()

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
                presetString = "{preset} {set_temp} {set_humid} {set_dioxide} {set_int_vide}".format(preset = setpointLineSplit[0],set_temp = serre.setpoint_Temp,set_humid = serre.setpoint_Humid, set_dioxide = serre.setpoint_Dioxide, set_int_vide=serre.setpoint_Int_Vid)
                setpointLines[x] = presetString
            file.write(setpointLines[x])


    def btn_Load_Saved_Set_Clicked(self):
        file = open("Projet_EC_Setpoint_List.txt", "rt")
        contenuFichier = file.read()
        setpointLines = contenuFichier.split("\n")
        for lines in setpointLines:
            setpointLineSplit=lines.split(" ")
            try:
                if(setpointLineSplit[0] == self.cb_Saved_Set.currentText()):
                    serre.setpoint_Name=setpointLineSplit[0]
                    serre.setpoint_Temp=int(setpointLineSplit[1])
                    serre.setpoint_Humid=int(setpointLineSplit[2])
                    serre.setpoint_Dioxide=int(setpointLineSplit[3])
                    serre.setpoint_Int_Vid=int(setpointLineSplit[4])
            except:
                pass
        self.updateSetpointsLCD()
        serre.saveSetpoints()
        sendSetpoints()

    #Fonction qui peuple le combobox des congsignes avec la table de consignes préenregistrées du fichier Projet_EC_Setpoint_List.txt
    def getPresets(self):
        try:
            file = open("Projet_EC_Setpoint_List.txt", "rt")
            contenuFichier = file.read()
            setpointLines = contenuFichier.split("\n")
            for lines in setpointLines:
                setpointLineSplit=lines.split(" ")
                if(setpointLineSplit[0] != ""):
                    self.cb_Saved_Set.addItem(setpointLineSplit[0])
        except:
            file = open("Projet_EC_Setpoint_List.txt", "wt")
            for x in range(1,serre.NB_PRESETS+1):
                if(x != 1):
                    file.write("\n")
                file.write("Preset_"+str(x)+" 0 0 0 0")
                self.cb_Saved_Set.addItem("Preset_"+str(x))
            file.close
        

    #Fonction qui update l'affichage des valeurs des consignes
    def updateSetpointsLCD(self):
        self.lcd_Temp_Set.display(str(serre.setpoint_Temp))
        self.lcd_Humid_Set.display(str(serre.setpoint_Humid))
        self.lcd_Inter_Vid_Set.display(str(serre.setpoint_Int_Vid))
        self.lcd_Dioxide_Set.display(str(serre.setpoint_Dioxide))
        


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
        clientMQTT_GUI.publish(topic=serre.TOPIC_GUI_API, payload=json.dumps(json_Data)) #Publie sur /test le JSON des valeurs de capteurs.
        

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


class WindowMinuteur(QMainWindow):
    def __init__(self):
        super(WindowMinuteur,self).__init__()
        loadUi("GUI_PEC_LightTimer.ui",self)
        self.btn_Setpoints_Menu.setStyleSheet("background-color:#c5c5c6")
        self.btn_Setpoints_Menu.clicked.connect(goto_Setpoints)
        self.btn_Monitor_Menu.clicked.connect(goto_Monitor)
        self.btn_Param_Menu.clicked.connect(goto_Param)
        self.btn_Outils_Menu.clicked.connect(goto_Outils)
        self.getPresetCycles()
        
        self.chkB_DEL_Panel.stateChanged.connect(self.chkBox_DEL_Panel_Changed)
        self.chkB_DEL_COB.stateChanged.connect(self.chkBox_DEL_COB_Changed)

        self.btn_Augment_Heure_Dep.clicked.connect(self.btn_Augment_Heure_Dep_Clicked)
        self.btn_Augment_Minute_Dep.clicked.connect(self.btn_Augment_Minute_Dep_Clicked)
        self.btn_Decrement_Heure_Dep.clicked.connect(self.btn_Decrement_Heure_Dep_Clicked)
        self.btn_Decrement_Minute_Dep.clicked.connect(self.btn_Decrement_Minute_Dep_Clicked)

        self.btn_Augment_Heure_Fin.clicked.connect(self.btn_Augment_Heure_Fin_Clicked)
        self.btn_Augment_Minute_Fin.clicked.connect(self.btn_Augment_Minute_Fin_Clicked)
        self.btn_Decrement_Heure_Fin.clicked.connect(self.btn_Decrement_Heure_Fin_Clicked)
        self.btn_Decrement_Minute_Fin.clicked.connect(self.btn_Decrement_Minute_Fin_Clicked)

        self.btn_Save_Cycle.clicked.connect(self.btn_Save_Cycle_Clicked)
        self.Btn_Load_Saved_Cycle.clicked.connect(self.btn_Load_Saved_Cycle_Clicked)

    def chkBox_DEL_Panel_Changed(self):
        if(self.chkB_DEL_Panel.isChecked()==True):
            serre.cycle_DEL_Panel_Used = True
        elif(self.chkB_DEL_Panel.isChecked()==False):
            serre.cycle_DEL_Panel_Used = False
        sendCycle()

    def chkBox_DEL_COB_Changed(self):
        if(self.chkB_DEL_COB.isChecked()==True):
            serre.cycle_DEL_COB_Used = True
        elif(self.chkB_DEL_COB.isChecked()==False):
            serre.cycle_DEL_COB_Used = False
        sendCycle()

    def btn_Augment_Heure_Dep_Clicked(self):
        heure_Depart = int(self.lbl_Heure_Dep.text())
        if(heure_Depart<12) :
            heure_Depart+=1
        if(heure_Depart == 12):
            self.lbl_Minute_Dep.setText("00")
            serre.cycle_Minute_Dep = 0
        showTime = "{:02d}".format(heure_Depart)
        self.lbl_Heure_Dep.setText(showTime)
        serre.cycle_Heure_Dep = heure_Depart
        sendCycle()

    def btn_Augment_Minute_Dep_Clicked(self):
        minute_Depart = int(self.lbl_Minute_Dep.text())
        if(int(self.lbl_Heure_Dep.text()) < 12):
            if(minute_Depart<55) :
                minute_Depart+=5
            elif(minute_Depart == 55):
                minute_Depart = 0
        showTime = "{:02d}".format(minute_Depart)
        self.lbl_Minute_Dep.setText(showTime)
        serre.cycle_Minute_Dep = minute_Depart
        sendCycle()

    def btn_Decrement_Heure_Dep_Clicked(self):
        heure_Depart = int(self.lbl_Heure_Dep.text())
        if(heure_Depart>0) :
            heure_Depart-=1
        showTime = "{:02d}".format(heure_Depart)
        self.lbl_Heure_Dep.setText(showTime)
        serre.cycle_Heure_Dep = heure_Depart
        sendCycle()

    def btn_Decrement_Minute_Dep_Clicked(self):
        minute_Depart = int(self.lbl_Minute_Dep.text())
        if(int(self.lbl_Heure_Dep.text()) < 12):
            if(minute_Depart>0) :
                minute_Depart-=5
            elif(minute_Depart == 0):
                minute_Depart = 55
        showTime = "{:02d}".format(minute_Depart)
        self.lbl_Minute_Dep.setText(showTime)
        serre.cycle_Minute_Dep = minute_Depart
        sendCycle()

    def btn_Augment_Heure_Fin_Clicked(self):
        heure_Fin = int(self.lbl_Heure_Fin.text())
        if(heure_Fin<24 and heure_Fin) :
            heure_Fin+=1
        if(heure_Fin == 24):
            heure_Fin = 0
            self.lbl_Minute_Fin.setText("00")
            serre.cycle_Minute_Fin = 0
        showTime = "{:02d}".format(heure_Fin)
        self.lbl_Heure_Fin.setText(showTime)
        serre.cycle_Heure_Fin = heure_Fin
        sendCycle()

    def btn_Augment_Minute_Fin_Clicked(self):
        minute_Fin = int(self.lbl_Minute_Fin.text())
        if(int(self.lbl_Heure_Fin.text())!=0): 
            if(minute_Fin<55) :
                minute_Fin+=5
            elif(minute_Fin == 55):
                minute_Fin = 0
        showTime = "{:02d}".format(minute_Fin)
        self.lbl_Minute_Fin.setText(showTime)
        serre.cycle_Minute_Fin = minute_Fin
        sendCycle()

    def btn_Decrement_Heure_Fin_Clicked(self):
        heure_Fin = int(self.lbl_Heure_Fin.text())
        if(heure_Fin>12) :
            heure_Fin-=1
        elif(heure_Fin == 0):
            heure_Fin = 23
        showTime = "{:02d}".format(heure_Fin)
        self.lbl_Heure_Fin.setText(showTime)
        serre.cycle_Heure_Fin = heure_Fin
        sendCycle()

    def btn_Decrement_Minute_Fin_Clicked(self):    
        minute_Fin = int(self.lbl_Minute_Fin.text())
        if(int(self.lbl_Heure_Fin.text())!=0): 
            if(minute_Fin>0) :
                minute_Fin-=5
            elif(minute_Fin == 0):
                minute_Fin = 55
        showTime = "{:02d}".format(minute_Fin)
        self.lbl_Minute_Fin.setText(showTime)
        serre.cycle_Minute_Fin = minute_Fin
        sendCycle()

    def getPresetCycles(self):
        list_Cycles = ["24:0", "18:6", "12:12", "Cycle 1", "Cycle 2"]
        try:
            file = open("Projet_EC_Cycles_List.txt", "rt")
            contenuFichier = file.read()
            cyclesLines = contenuFichier.split("\n")
            for lines in cyclesLines:
                cyclesLinesSplit=lines.split(";")
                if(cyclesLinesSplit[0] != ""):
                    self.cb_Saved_Cycle.addItem(cyclesLinesSplit[0])
        except:
            file = open("Projet_EC_Cycles_List.txt", "wt")
            for x in range(1,len(list_Cycles)+1):
                if(x != 1): 
                    file.write("\n")# Le newline est ici pour ne pas mettre de newline a la fin et avoir une ligne vide
                if(x == 1):
                    heure_Dep = "00h00"
                    heure_Fin = "00h00"
                elif(x == 2):
                    heure_Dep = "04h00"
                    heure_Fin = "22h00"  
                elif(x == 3):
                    heure_Dep = "8h00"
                    heure_Fin = "20h00"  
                else:
                    heure_Dep = "00h00"
                    heure_Fin = "00h00"  

                file.write("{};{};{}".format(list_Cycles[x-1], heure_Dep, heure_Fin))
                self.cb_Saved_Cycle.addItem(list_Cycles[x-1])
            file.close


    def btn_Save_Cycle_Clicked(self):
        file = open("Projet_EC_Cycles_List.txt", "rt")
        contenuFichier = file.read()
        contenuFichier = contenuFichier.rstrip()
        setpointLines = contenuFichier.split("\n")
        file.close()
        file = open("Projet_EC_Cycles_List.txt", "w")
        for x in range(0,len(setpointLines)):
            if(x != 0):
                file.write("\n")
            setpointLineSplit=setpointLines[x].split(";")
            if(setpointLineSplit[0] == self.cb_Saved_Cycle.currentText()):
                presetString = "{preset};{heure_Dep}h{minute_Dep};{heure_Fin}h{minute_Fin}".format(preset = setpointLineSplit[0],heure_Dep = serre.cycle_Heure_Dep, minute_Dep = serre.cycle_Minute_Dep,heure_Fin = serre.cycle_Heure_Fin, minute_Fin=serre.cycle_Minute_Fin)
                setpointLines[x] = presetString
            file.write(setpointLines[x])


    def btn_Load_Saved_Cycle_Clicked(self):
        try:
            file = open("Projet_EC_Cycles_List.txt", "rt")
            contenuFichier = file.read()
            setpointLines = contenuFichier.split("\n")
            for lines in setpointLines:
                setpointLineSplit=lines.split(";")
                if(setpointLineSplit[0] == self.cb_Saved_Cycle.currentText()):
                    try:
                        serre.cycle_Name=setpointLineSplit[0]
                        split_Cycle_Heure = setpointLineSplit[1].split("h")
                        serre.cycle_Heure_Dep=int(split_Cycle_Heure[0])
                        serre.cycle_Minute_Dep=int(split_Cycle_Heure[1])
                        split_Cycle_Heure = setpointLineSplit[2].split("h")
                        serre.cycle_Heure_Fin=int(split_Cycle_Heure[0])
                        serre.cycle_Minute_Fin=int(split_Cycle_Heure[1])
                        self.lbl_Heure_Dep.setText("{:02d}".format(serre.cycle_Heure_Dep))
                        self.lbl_Minute_Dep.setText("{:02d}".format(serre.cycle_Minute_Dep))
                        self.lbl_Heure_Fin.setText("{:02d}".format(serre.cycle_Heure_Fin))
                        self.lbl_Minute_Fin.setText("{:02d}".format(serre.cycle_Minute_Fin))
                    except Exception as err:
                        print(err)
            sendCycle()
        except:
            print("Erreur de lecture du fichier des cycles.")


def sendCycle():
    serre.saveCycle()
    
    cycle_String = '{"Cycle":{"Nom": "", "Lumiere": { "DEL_COB" : 0, "DEL_Panel" : 0 }, "Temps": { "Depart" : { "Heure" : 0, "Minute" : 0 }, "Fin": { "Heure" : 0, "Minute" : 0  } } } }'
    json_Data = json.loads(cycle_String)
    json_Data["Cycle"]["Nom"]=serre.cycle_Name
    json_Data["Cycle"]["Lumiere"]["DEL_COB"] = serre.cycle_DEL_COB_Used
    json_Data["Cycle"]["Lumiere"]["DEL_Panel"] = serre.cycle_DEL_Panel_Used
    json_Data["Cycle"]["Temps"]["Depart"]["Heure"]=serre.cycle_Heure_Dep
    json_Data["Cycle"]["Temps"]["Depart"]["Minute"]=serre.cycle_Minute_Dep
    json_Data["Cycle"]["Temps"]["Fin"]["Heure"]=serre.cycle_Heure_Fin
    json_Data["Cycle"]["Temps"]["Fin"]["Minute"]=serre.cycle_Minute_Fin
    clientMQTT_GUI.publish(topic=serre.TOPIC_GUI_INPUT_CYCLE, payload=json.dumps(json_Data)) #Publie sur /test le JSON des valeurs de capteurs.


def sendSetpoints():
    setpoints_String = '{"Setpoints":{"Temp": 0, "Humid": 0, "Dioxide": 0, "Int_Vide": 0} }'
    json_Data = json.loads(setpoints_String)
    json_Data["Setpoints"]["Temp"]=serre.setpoint_Temp
    json_Data["Setpoints"]["Humid"]=serre.setpoint_Humid
    json_Data["Setpoints"]["Dioxide"]=serre.setpoint_Dioxide
    json_Data["Setpoints"]["Int_Vide"]=serre.setpoint_Int_Vid
    clientMQTT_GUI.publish(topic=serre.TOPIC_GUI_INPUT_SET, payload=json.dumps(json_Data)) #Publie sur /test le JSON des valeurs de capteurs.
        

def meanTempShowLCD(mqttMessageJSON):
    global monitorWindow
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
        mqttMessageJSON = json.loads(dataMQTT) #Load le message en JSON ( de dict)
        if (msg.topic==serre.TOPIC_GUI_FLAG_API):
            updateThingspeakValidity(mqttMessageJSON['api_ok'])
        elif(msg.topic == serre.TOPIC_DATA_SERRE):
            meanTempShowLCD(mqttMessageJSON)
    except Exception as err:
        print(err)

def updateThingspeakValidity(state):
    configWindow.lbl_Info_Erreurs.takeItem(1)
    if state == True:
        configWindow.lbl_Info_Erreurs.insertItem(1,("Clé Thingspeak valide"))
    elif state == False:
        configWindow.lbl_Info_Erreurs.insertItem(1,("Clé Thingspeak invalide "))

if __name__ == "__main__":   #Debut du "Main"
    serre = gestionSerre() #Instanciation d'un objet de la classe gestionSerre Elle serre a storer les données de la serre
    serre.setup_GPIO()
    serre.getAPI()
    
    clientMQTT_GUI = mqtt.Client("clientMQTT_GUI") #client MQTT lié au échanges entre les données de la serre et l'affichage
    clientMQTT_GUI.connect(serre.BROKER_MQTT_ADDR)
    clientMQTT_GUI.subscribe(serre.TOPIC_PROJET)
    clientMQTT_GUI.on_message = on_message
    clientMQTT_GUI.loop_start()  


    #Setup GUI
    app = QApplication(sys.argv)
    screenWidget = QtWidgets.QStackedWidget() #Widget qui contient toutes les fenetres et permet de switcher entre fenetres
    monitorWindow = WindowMonitor() #Instanciation d'un objet de chaque type de fenetres    
    controlWindow = WindowControl()
    configWindow = WindowConfig()
    adminWindow = WindowAdmin()
    timerWindow = WindowMinuteur()
    screenWidget.addWidget(monitorWindow)   #Ajoute les fenetres au Gestionnaire screenWidget
    screenWidget.addWidget(controlWindow)
    screenWidget.addWidget(configWindow)
    screenWidget.addWidget(adminWindow)
    screenWidget.addWidget(timerWindow)
    
    if(serre.cle_API != ""):
        api_String = '{"api_key":""}'
        json_Data = json.loads(api_String)
        json_Data["api_key"]=serre.cle_API
        clientMQTT_GUI.publish(topic=serre.TOPIC_GUI_API_INIT, payload=json.dumps(json_Data)) #Publie sur /test le JSON des valeurs de capteurs.
        configWindow.tb_Thingspeak_Cle.setText(str(serre.cle_API))

    updateThingspeakValidity(serre.Flag_Thingspeak_Connected)

    #screenWidget.showFullScreen()         #Affiche en plein ecran ( PROJET MODE )
    screenWidget.showMaximized()         #Affiche le GUI en maximizé ( Bloquant )
    GPIO.cleanup()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")




