# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'control.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

# Programme permettant d'afficher la fenêtre de changement de consigne. Cette fenêtre est ouverte par le programme MainGUI.py.
# Lorsque cette fenêtre est construite, elle reçoit la consigne courante et la limite de la consigne.
# Envoie la nouvelle consigne créé par Signal vers MainGUI.py

from PyQt5 import QtCore, QtGui, QtWidgets

# Classe pour l'objet Signal. Cette classe existe car si je déclarais mon signal è l'intérieur de Ui_Mainwindow1(), le Signal ne marchais pas.
class Calc(QtCore.QObject):
    submitted = QtCore.pyqtSignal(int) #Création de l'objet Signal
    def sendpls(self):   # Plus nécessaire au programme, je vais devoir l'enlever au prochain PUSH.
        print("send")
        self.submitted.emit("1")
        
# Création des objets graphiques de la fenêtre de controle.
class Ui_MainWindow1(object):
    def setup(self, MainWindow, controlTemp, limit):
        self.MainWindow = MainWindow
        
        self.limit = limit        
        self.control_Temp = controlTemp
        self.new_Temp = controlTemp
        
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(948, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.but_Val_down = QtWidgets.QPushButton(self.centralwidget)
        self.but_Val_down.setObjectName("but_Val_down")
        self.gridLayout_2.addWidget(self.but_Val_down, 0, 1, 1, 1)
        self.but_Cancel = QtWidgets.QPushButton(self.centralwidget)
        self.but_Cancel.setObjectName("but_Cancel")
        self.gridLayout_2.addWidget(self.but_Cancel, 2, 1, 1, 1)
        self.but_Val_up = QtWidgets.QPushButton(self.centralwidget)
        self.but_Val_up.setObjectName("but_Val_up")
        self.gridLayout_2.addWidget(self.but_Val_up, 0, 0, 1, 1)
        self.but_Submit = QtWidgets.QPushButton(self.centralwidget)
        self.but_Submit.setObjectName("but_Submit")
        self.gridLayout_2.addWidget(self.but_Submit, 2, 0, 1, 1)
        self.lcd_New = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_New.setObjectName("lcd_New")
        self.gridLayout_2.addWidget(self.lcd_New, 1, 1, 1, 1)
        self.lcd_Current = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_Current.setObjectName("lcd_Current")
        self.gridLayout_2.addWidget(self.lcd_Current, 1, 0, 1, 1)
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 948, 29))
        self.menubar.setObjectName("menubar")
        self.MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)
        
        self.lcd_Current.display(self.control_Temp)  #affiche le set temp de temp courrant
        self.lcd_New.display(self.new_Temp)
        
        self.objsignal = Calc() #Création du Signal
        
        #Création des évênnement de fenêtre.
        self.but_Submit.clicked.connect(self.on_click_submit)
        self.but_Cancel.clicked.connect(self.on_click_Cancel)
        self.but_Val_up.clicked.connect(self.on_click_up)
        self.but_Val_down.clicked.connect(self.on_click_Down)
        
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.but_Val_down.setText(_translate("MainWindow", "DOWN"))
        self.but_Cancel.setText(_translate("MainWindow", "Cancel"))
        self.but_Val_up.setText(_translate("MainWindow", "UP"))
        self.but_Submit.setText(_translate("MainWindow", "Submit"))
    
    # Ferme la fenêtre control.py sans modifier les valeurs de consigne.
    def on_click_Cancel(self):
        self.MainWindow.close()
    
    # Ferme la fenêtre et envoie la nouvelle consigne par Signal vers MainGUI.py. 
    def on_click_submit(self):
        self.objsignal.submitted.emit(self.new_Temp) #Envoie de la valeur
        self.MainWindow.close() #ferme fenêtre
    
    # Augmente la valeur de 1
    def on_click_up(self):
        if(self.new_Temp < self.limit):
            self.new_Temp = self.new_Temp +1
            self.lcd_New.display(self.new_Temp)
            
    # Diminue la valeur de 1    
    def on_click_Down(self):
        if(self.new_Temp > 0):
            self.new_Temp = self.new_Temp -1
            self.lcd_New.display(self.new_Temp)
