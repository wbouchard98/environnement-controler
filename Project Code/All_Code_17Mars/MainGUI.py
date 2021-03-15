# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mqttbuttontest3.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from control import *
import paho.mqtt.client as mqtt #import the client1
import time
import json



class Ui_MainWindow(object):
    client = mqtt.Client("lol")
    client.connect("127.0.0.1") #connect to broker
    mqttMessageJSON = json.loads('{"DS": {"temp": "0"}, "SHT": {"temp": "0", "hum": "0"}, "CSS811": {"CO2": "0", "TVOC": "0"}}')
   
    dummyvalue = 0
    control_Temp = 25
    control_Hum = 60
    
    def initmqtt(self):
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect

        print("initmqtt")

    def on_disconnect(self, client, userdata, rc):
        print("disconnecting")


    def on_message(self, client, userdata, msg):

        try:
            self.dummyvalue = msg.payload

            print(self.dummyvalue)
            self.mqttMessageJSON = json.loads(self.dummyvalue)

            pad_DS_Temp = ("%.2f"%self.mqttMessageJSON["DS"]["temp"])
            pad_SENHUM = ("%.2f"%self.mqttMessageJSON["SHT"]["hum"])
            pad_SENTEMP = ("%.2f"%self.mqttMessageJSON["SHT"]["temp"])
            
            #self.lcdNumber_SENTEMP.display(self.mqttMessageJSON["SHT"]["temp"])
            #self.lcdNumber_DSB.display(self.mqttMessageJSON["DS"]["temp"])
            self.lcdNumber_DSB.display(pad_DS_Temp)
            self.lcdNumber_SENHUM.display(pad_SENHUM)
            self.lcdNumber_SENTEMP.display(pad_SENTEMP)
            #self.lcdNumber_SENHUM.display(self.mqttMessageJSON["SHT"]["hum"])
            self.lcdNumber_CCSCO.display(self.mqttMessageJSON["CSS811"]["CO2"])
            self.lcdNumber_CCSTVOC.display(self.mqttMessageJSON["CSS811"]["TVOC"])
            
            #self.lcdNumber.display(self.dummyvalue)
        except Exception as err:
            print(err)
    
    def on_connect(self, client, userdata, flags, rc):
        print("connected")
#        self.flagconnect = True
#        self.flagconnecting = False

    def connectmqtt(self):
        try:
#            self.flagconnecting = True
            self.client.connect("127.0.0.1")
            print("connecting????")
            self.client.subscribe("/test")

        except Exception as err:
            print(err)
    
    def returntocontrol(self):
        json_data = json.loads('{"TEMP": '+str(self.control_Temp)+',"HUM": '+str(self.control_Hum)+'}')
        self.client.publish(topic="/test2", payload=json.dumps(json_data)) 
    
    def receiver(self, num):
        print(num)
        #self.client.publish("/test2", num)
        self.control_Temp = num
        self.returntocontrol()
        self.writeConsigne()
        
    def receiverHum(self,num):
        print(num)
        #self.client.publish("/test2", num)
        self.control_Hum = num
        self.returntocontrol()
        self.writeConsigne()
        
    def writeConsigne(self):
        f= open("last_consigne.txt", "w")
        f.write(str(self.control_Temp) +" "+str(self.control_Hum))
        f.close()
        
    def testpls(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow1()
        self.ui.setup(self.window, self.control_Temp, 60)
        self.ui.objsignal.submitted.connect(self.receiver)

        self.window.show()
    
    def set_Hum(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow1()
        self.ui.setup(self.window, self.control_Hum, 100)
        self.ui.objsignal.submitted.connect(self.receiverHum)
        self.window.show()
        
    def get_consigne(self):
        #readfile
        f = open("last_consigne.txt", "r")
        valeurConsigne = f.read()
        f.close()
        if(valeurConsigne == ""):
            print("Aucune consigne trouver... Ajout de consigne de temperature et d'humidite 30")
            f= open("last_consigne.txt", "w")
            f.write("30 30")
            f.close()
            valeurConsigne = "30 30"

        splitted_ValCon = valeurConsigne.split(" ")
        self.control_Temp = int(splitted_ValCon[0])
        self.control_Hum = int(splitted_ValCon[1])
        self.returntocontrol()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1087, 663)
        
        self.initmqtt()
        self.connectmqtt()
        
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
                
        self.set_hum = QtWidgets.QAction(MainWindow)
        self.set_hum.setObjectName("set_hum")
        self.menuOption.addAction(self.set_hum)
        
        self.menubar.addAction(self.menuOption.menuAction())
        
        
        #self.statusbar.setStyleSheet("QStatusBar{padding-left:8px;color:red;font-weight:bold;}")
        #self.statusbar.showMessage("Heating")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.set_temp.triggered.connect(self.testpls)
        self.set_hum.triggered.connect(self.set_Hum)
        
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
        self.set_temp.setText(_translate("MainWindow", "Consigne de température"))
        self.set_hum.setText(_translate("MainWindow", "Consigne Humidité"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    time.sleep(2)
    MainWindow.show()
    ui.client.loop_start()
    sys.exit(app.exec_())
