# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mqttbuttontest3.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
# 
#
# Programme principale pour l'affichage des données des capteurs sur l'écran. Permet d'ouvrir une fenêtre qui permet de choisir la consigne de température et une autre pour l'humidité.(control.py)
# Reçoit les informations des capteurs par MQTT du programme P_principale_lecture.py sur le topic /test. Les données reçues sont les suivantes:
# Température du capteur DS18B20, Température et humidité du SEN0227 et concentration de CO2 et de particules organiques dans l'air du capteur CSS811.
# Le programme reçoit par signal de la part du programme control.py les nouvelles consignes de température et humidité qui sont par la suite envoyées par MQTT au programme P_principale_lecture.py.
# Le programme écrit aussi chaque nouvelle consigne dans last_consigne.txt pour pouvoir recommencer le contrôle de l'environnement avec les mêmes limites si le Raspberry Pi n'est plus alimenté.

from PyQt5 import QtCore, QtGui, QtWidgets
from controlV2_2 import *   #importe la fenêtre qui sert à régler les consignes
import paho.mqtt.client as mqtt #import the client
import time
import json


# Classe contenant le code servant à la communication MQTT, l'affichage et la communication avec la fenêtre control.py
class Ui_MainWindow(object):
    client = mqtt.Client("lol") #nouveau client MQTT
    client.connect("127.0.0.1") #connect to broker
    mqttMessageJSON = json.loads('{"DS": {"temp": "0"}, "SHT": {"temp": "0", "hum": "0"}, "CSS811": {"CO2": "0", "TVOC": "0"}}') #création du squelette du message MQTT reçu de P_principale_lecture.py
   
    messMQTT = 0  #Variable qui reçoit le message par MQTT
    control_Temp = 25 #Consigne de base de température
    control_Hum = 60 #Consigne de base pour l'humidité
    
    #Initialisation des évênnements MQTT certain de ces évênnements ont des utilités de DEBUG seulemnt pour l'instant.
    def initmqtt(self):
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect

        print("init mqtt")

    def on_disconnect(self, client, userdata, rc):
        print("disconnecting")

    # Action effectué lorsqu'un message est envoyé sur le topic /test
    # Affichage des nouvelles valeurs des capteurs
    def on_message(self, client, userdata, msg):

        try:
            self.messMQTT = msg.payload #prend le msg MQTT

            print(self.messMQTT) #Montre le message reçu en console (DEBUG)
            self.mqttMessageJSON = json.loads(self.messMQTT) #transforme le message en JSON
            
            #Fait en sorte que les valeurs comme 24 s'affichent en tant que 24.00 pour rendre l'affichage plus uniforme.
            pad_DS_Temp = ("%.2f"%self.mqttMessageJSON["DS"]["temp"])   
            pad_SENHUM = ("%.2f"%self.mqttMessageJSON["SHT"]["hum"])
            pad_SENTEMP = ("%.2f"%self.mqttMessageJSON["SHT"]["temp"])
            
            
            #Mise en affichage des valeurs reçu par MQTT
            self.lcdNumber_DSB.display(pad_DS_Temp)
            self.lcdNumber_SENHUM.display(pad_SENHUM)
            self.lcdNumber_SENTEMP.display(pad_SENTEMP)
            self.lcdNumber_CCSCO.display(self.mqttMessageJSON["CSS811"]["CO2"])
            self.lcdNumber_CCSTVOC.display(self.mqttMessageJSON["CSS811"]["TVOC"])
            
        except Exception as err:
            print(err)
    
    
    def on_connect(self, client, userdata, flags, rc):
        print("connected")

    # Fonction qui permet de se connecter au topic /test pour recevoir les informations de P_principale_lecture.py
    def connectmqtt(self):
        try:
            self.client.connect("127.0.0.1")
            print("connecting... ...")
            self.client.subscribe("/test")

        except Exception as err:
            print(err)
    
    # Fonction permettant de formatter les consignes en JSON et d'envoyer un message MQTT sur /test2 pour que P_principale_lecture.py puisse lire les nouvelles consignes.
    def returntocontrol(self):
        json_data = json.loads('{"TEMP": '+str(self.control_Temp)+',"HUM": '+str(self.control_Hum)+'}')
        self.client.publish(topic="/test2", payload=json.dumps(json_data)) 
    
    # Fonction qui permet de gérer les signAUX que la fenêtre control.py envoie. Gère la température.
    #def receiver(self, num):
    #    print(num)
    #    self.control_Temp = num #prend la nouvelle valeur de la consigne.
    #    self.returntocontrol()
    #    self.writeConsigne()
        
    # Fonction qui permet de gérer les signAUX que la fenêtre control.py envoie. Gère l'humidité.
    #def receiverHum(self,num):
    #    print(num)
    #    self.control_Hum = num
    #    self.returntocontrol()
    #    self.writeConsigne()
    
    # Écrit les nouvelles consignes dans le fichier texte last_consigne.txt. Écrase les anciennes.
    def writeConsigne(self):
        f= open("last_consigne.txt", "w")
        f.write(str(self.control_Temp) +" "+str(self.control_Hum)) # Esapce permettant l'identification des deux valeurs plus facilement.
        f.close()
    
   # Permet d'ouvrir la fenêtre de contrôle pour la température. Création du signal entre la fenêtre présente et control.py (Nom de fonction à modifier dans les prochains Push)   
   # def testpls(self):
   #     self.window=QtWidgets.QMainWindow() #Création de l'objet contenant les propriétés de fenêtre.
   #     self.ui=Ui_MainWindow1() #Création de l'objet contenant la classe d'objet graphique
   #     self.ui.setup(self.window, self.control_Temp, 60) #Envoie de la consigne présente et de la limite haute de de la consigne à la nouvelle fenêtre. Création des différents objets graphiques.
   #     self.ui.objsignal.submitted.connect(self.receiver) #Création du lien entre le signal du control.py et du Slot de ce programme.

    #    self.window.show() # Affiche la fenêtre control.py
    
    # Permet d'ouvrir la fenêtre de contrôle pour l'humidité. Création du signal entre la fenêtre présente et control.py    
    #def set_Hum(self):
    #    self.window=QtWidgets.QMainWindow()
    #    self.ui=Ui_MainWindow1()
    #    self.ui.setup(self.window, self.control_Hum, 100)
    #    self.ui.objsignal.submitted.connect(self.receiverHum)
    #    self.window.show()
    
    def set_Consigne(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow1()
        self.ui.setup(self.window, self.control_Temp, self.control_Hum)
        self.ui.objsignal.submitted.connect(self.receiverSign)
        self.window.show()
    
     # Fonction qui permet de gérer les signAUX que la fenêtre control.py envoie. Gère l'humidité.
    def receiverSign(self, Temp, Hum):
        print(Temp)
        print(Hum)
        self.control_Hum = Hum
        self.control_Temp = Temp
        self.returntocontrol()
        self.writeConsigne()
    
    # Fonction permettant d'aller chercher les dernières consignes connues du programme.
    def get_consigne(self):
        f = open("last_consigne.txt", "r") 
        valeurConsigne = f.read() 
        f.close()
        if(valeurConsigne == ""):  #regarde si fichier last_consigne.txt
            #Si vide mets des consignes de base de 30 pour l'humidité et la température dans le fichier last_consigne.txt
            print("Aucune consigne trouver... Ajout de consigne de temperature et d'humidite 30") 
            f= open("last_consigne.txt", "w")
            f.write("30 30")
            f.close()
            valeurConsigne = "30 30"
        # Sépare la string et mets à jour les valeurs des consignes.
        splitted_ValCon = valeurConsigne.split(" ")
        self.control_Temp = int(splitted_ValCon[0])
        self.control_Hum = int(splitted_ValCon[1])
        self.returntocontrol()
        
    # Créateur des différents objets graphiques. Contient aussi l'initialisation de la connection MQTT.    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1087, 663)
        
        self.initmqtt()     #Initialisation de l'objet MQTT
        self.connectmqtt()  # Connection au topic /test
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lcdNumber_DSB = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_DSB.setObjectName("lcdNumber_DSB")
        self.verticalLayout.addWidget(self.lcdNumber_DSB)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.lcdNumber_SENHUM = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_SENHUM.setObjectName("lcdNumber_SENHUM")
        self.verticalLayout_3.addWidget(self.lcdNumber_SENHUM)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 2, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.lcdNumber_CCSTVOC = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_CCSTVOC.setObjectName("lcdNumber_CCSTVOC")
        self.verticalLayout_5.addWidget(self.lcdNumber_CCSTVOC)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_5.addWidget(self.label_10)
        self.gridLayout.addLayout(self.verticalLayout_5, 1, 1, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.lcdNumber_CCSCO = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_CCSCO.setObjectName("lcdNumber_CCSCO")
        self.verticalLayout_4.addWidget(self.lcdNumber_CCSCO)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.gridLayout.addLayout(self.verticalLayout_4, 1, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.lcdNumber_SENTEMP = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_SENTEMP.setObjectName("lcdNumber_SENTEMP")
        self.verticalLayout_2.addWidget(self.lcdNumber_SENTEMP)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_6.addWidget(self.label_11)
        self.lcdNumber_humsol = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_humsol.setObjectName("lcdNumber_humsol")
        self.verticalLayout_6.addWidget(self.lcdNumber_humsol)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_6.addWidget(self.label_12)
        self.gridLayout.addLayout(self.verticalLayout_6, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1087, 29))
        self.menubar.setObjectName("menubar")
        self.menuOption = QtWidgets.QMenu(self.menubar)
        self.menuOption.setObjectName("menuOption")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.set_temp = QtWidgets.QAction(MainWindow)
        self.set_temp.setObjectName("set_temp")
        self.menuOption.addAction(self.set_temp)
                
        #self.set_hum = QtWidgets.QAction(MainWindow)
        #self.set_hum.setObjectName("set_hum")
        #self.menuOption.addAction(self.set_hum)
        
        self.menubar.addAction(self.menuOption.menuAction())
        
        
        #self.statusbar.setStyleSheet("QStatusBar{padding-left:8px;color:red;font-weight:bold;}")
        #self.statusbar.showMessage("Heating")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
       # Création d'évênement lorsque l'usager clique sur les onglets d'option permettant de changer les consignes de température.
        self.set_temp.triggered.connect(self.set_Consigne)
        #self.set_hum.triggered.connect(self.set_Hum)
        
        #Regarde le fichier last_consigne.txt
        self.get_consigne()
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "DS18B20 Température"))
        self.label_2.setText(_translate("MainWindow", "Celcius"))
        self.label_5.setText(_translate("MainWindow", "SEN0227 Humidité"))
        self.label_6.setText(_translate("MainWindow", "%"))
        self.label_9.setText(_translate("MainWindow", "CCS811 TVOC"))
        self.label_10.setText(_translate("MainWindow", "mg/m3"))
        self.label_7.setText(_translate("MainWindow", "CCS811 Co2"))
        self.label_8.setText(_translate("MainWindow", "ppm"))
        self.label_4.setText(_translate("MainWindow", "SEN0227 Température"))
        self.label_3.setText(_translate("MainWindow", "Celcius"))
        self.label_11.setText(_translate("MainWindow", "Humidité du sol"))
        self.label_12.setText(_translate("MainWindow", "Unité par unité"))
        self.menuOption.setTitle(_translate("MainWindow", "Option"))
        self.set_temp.setText(_translate("MainWindow", "Changement de consigne"))
        #self.set_hum.setText(_translate("MainWindow", "Consigne Humidité"))

#Permet de construire la fenêtre du programme GUI principale
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    time.sleep(2) #Laisse le temps à l'objet MQTT de bien faire sa connection avant de partir la loop d'écoute.
    MainWindow.show()
    ui.client.loop_start()
    sys.exit(app.exec_())
