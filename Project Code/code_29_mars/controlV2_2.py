#controlV2_2.py

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'control_redesign_x2_V2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

# Programme permettant d'afficher la fenêtre de changement de consigne. Cette fenêtre est ouverte par le programme MainGUI.py.
# Lorsque cette fenêtre est construite, elle reçoit la consigne courante de temp/rature et d<humidit/.
# Envoie les nouvelles consignes créés par Signal vers MainGUI.py

from PyQt5 import QtCore, QtGui, QtWidgets

# Classe pour l'objet Signal. Cette classe existe car si je déclarais mon signal è l'intérieur de Ui_Mainwindow1(), le Signal ne marchais pas.
class Calc(QtCore.QObject):
    submitted = QtCore.pyqtSignal(int, int) #Création de l'objet Signal pouvant envoyer la temo/rature et l<humidit/

# Création des objets graphiques de la fenêtre de controle.
class Ui_MainWindow1(object):
    lim_Temp = 60
    lim_Hum = 100
    
    def setup(self, MainWindow, control_Temp, control_Hum):
        self.MainWindow = MainWindow
        self.control_Temp = control_Temp       
        self.control_Hum = control_Hum
        
        #D/but du code g/n/r/ automatiquement par le designer
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(948, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lcdNumber_Hum = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_Hum.setObjectName("lcdNumber_Hum")
        self.gridLayout_2.addWidget(self.lcdNumber_Hum, 0, 1, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.pushButton_Submit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Submit.setObjectName("pushButton_Submit")
        self.verticalLayout_6.addWidget(self.pushButton_Submit)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.gridLayout_2.addLayout(self.verticalLayout_6, 2, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_Hum_UP = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Hum_UP.setObjectName("pushButton_Hum_UP")
        self.horizontalLayout_4.addWidget(self.pushButton_Hum_UP)
        self.pushButton_Hum_DOWN = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Hum_DOWN.setObjectName("pushButton_Hum_DOWN")
        self.horizontalLayout_4.addWidget(self.pushButton_Hum_DOWN)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_Hum = QtWidgets.QLabel(self.centralwidget)
        self.label_Hum.setObjectName("label_Hum")
        self.verticalLayout_2.addWidget(self.label_Hum)
        self.label_Hum.setAlignment(QtCore.Qt.AlignCenter)               # ajout/ manuellement pour centrer label
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        
        self.horizontalSlider_Hum = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_Hum.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_Hum.setSizePolicy(sizePolicy)
        self.horizontalSlider_Hum.setStyleSheet("\n"
"QSlider::groove:horizontal {\n"
"      background-color: black;\n"
"    border: 0px solid #424242; \n"
"    height: 10px; \n"
"    border-radius: 30px;\n"
"    }\n"
"QSlider::handle:horizontal {\n"
"    background: qradialgradient(spread:pad, cx:0.5, cy:0.511, radius:1.695, fx:0.5, fy:0.5, stop:0 rgba(133, 133, 133, 255), stop:0.555556 rgba(229, 229, 229, 255));\n"
"    border: 1px solid;\n"
"    border-color: rgb(202, 202, 202);\n"
"    height: 30px;\n"
"    width: 30px;\n"
"    margin: -10px 0px;\n"
"    border-radius: 10px;\n"
"    }\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"border-color: rgb(19, 192, 255);\n"
"}\n"
"\n"
"QSlider::sub-page\n"
"{\n"
"    background: rgb(19, 192, 255);\n"
"}\n"
"QSlider::add-page \n"
"{\n"
"    background: rgb(204, 204, 204);\n"
"}")
        self.horizontalSlider_Hum.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_Hum.setObjectName("horizontalSlider_Hum")
        self.gridLayout_3.addWidget(self.horizontalSlider_Hum, 2, 0, 1, 1)
        
        #self.horizontalSlider_Hum = QtWidgets.QSlider(self.centralwidget)
        #self.horizontalSlider_Hum.setOrientation(QtCore.Qt.Horizontal)
        #self.horizontalSlider_Hum.setObjectName("horizontalSlider_Hum")
        #self.gridLayout_3.addWidget(self.horizontalSlider_Hum, 2, 0, 1, 1)
        
        self.gridLayout_2.addLayout(self.gridLayout_3, 1, 1, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.pushButton_Cancel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        self.verticalLayout_7.addWidget(self.pushButton_Cancel)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.gridLayout_2.addLayout(self.verticalLayout_7, 2, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_Temp = QtWidgets.QLabel(self.centralwidget)
        self.label_Temp.setObjectName("label_Temp")
        self.verticalLayout.addWidget(self.label_Temp)
        self.label_Temp.setAlignment(QtCore.Qt.AlignCenter)    # ajout/ manuellement pour centrer label
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_Temp_UP = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Temp_UP.setObjectName("pushButton_Temp_UP")
        self.horizontalLayout_2.addWidget(self.pushButton_Temp_UP)
        self.pushButton_Temp_DOWN = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Temp_DOWN.setObjectName("pushButton_Temp_DOWN")
        self.horizontalLayout_2.addWidget(self.pushButton_Temp_DOWN)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        
        self.horizontalSlider_Temp = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_Temp.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_Temp.setSizePolicy(sizePolicy)
        self.horizontalSlider_Temp.setStyleSheet("\n"
"QSlider::groove:horizontal {\n"
"      background-color: black;\n"
"    border: 0px solid #424242; \n"
"    height: 10px; \n"
"    border-radius: 30px;\n"
"    }\n"
"QSlider::handle:horizontal {\n"
"    background: qradialgradient(spread:pad, cx:0.5, cy:0.511, radius:1.695, fx:0.5, fy:0.5, stop:0 rgba(133, 133, 133, 255), stop:0.555556 rgba(229, 229, 229, 255));\n"
"    border: 1px solid;\n"
"    border-color: rgb(202, 202, 202);\n"
"    height: 30px;\n"
"    width: 30px;\n"
"    margin: -10px 0px;\n"
"    border-radius: 10px;\n"
"    }\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"border-color: rgb(19, 192, 255);\n"
"}\n"
"\n"
"QSlider::sub-page\n"
"{\n"
"    background: rgb(19, 192, 255);\n"
"}\n"
"QSlider::add-page \n"
"{\n"
"    background: rgb(204, 204, 204);\n"
"}")
        self.horizontalSlider_Temp.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_Temp.setObjectName("horizontalSlider_Temp")
        self.gridLayout.addWidget(self.horizontalSlider_Temp, 2, 0, 1, 1)
        
        #self.horizontalSlider_Temp = QtWidgets.QSlider(self.centralwidget)
        #self.horizontalSlider_Temp.setOrientation(QtCore.Qt.Horizontal)
        #self.horizontalSlider_Temp.setObjectName("horizontalSlider_Temp")
        #self.gridLayout.addWidget(self.horizontalSlider_Temp, 2, 0, 1, 1)
        
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.lcdNumber_Temp = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_Temp.setObjectName("lcdNumber_Temp")
        self.gridLayout_2.addWidget(self.lcdNumber_Temp, 0, 0, 1, 1)
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 948, 29))
        self.menubar.setObjectName("menubar")
        self.MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)
        #Fin du code g/n/r/ automatiquement
        
        self.lcdNumber_Temp.display(self.control_Temp)  #affiche le set temp de temp courrant
        self.lcdNumber_Hum.display(self.control_Hum)    # affiche le set hum courrant
        
        self.objsignal = Calc() #Création du Signal
        
        # Donne les options des sliders
        self.horizontalSlider_Hum.setMinimum(0)
        self.horizontalSlider_Hum.setMaximum(self.lim_Hum)
        self.horizontalSlider_Hum.setSingleStep(1)
        self.horizontalSlider_Hum.setValue(self.control_Hum)
        self.horizontalSlider_Hum.sliderMoved.connect(self.change_Hum_Val)
        
        self.horizontalSlider_Temp.setMinimum(0)
        self.horizontalSlider_Temp.setMaximum(self.lim_Temp)
        self.horizontalSlider_Temp.setSingleStep(1)
        self.horizontalSlider_Temp.setValue(self.control_Temp)
        self.horizontalSlider_Temp.sliderMoved.connect(self.change_Temp_Val)
                
        #Création des évênnement de fenêtre.
        self.pushButton_Submit.clicked.connect(self.on_click_submit)
        self.pushButton_Cancel.clicked.connect(self.on_click_cancel)
        
        self.pushButton_Temp_UP.clicked.connect(self.on_click_temp_up)
        self.pushButton_Temp_DOWN.clicked.connect(self.on_click_temp_down)
        
        self.pushButton_Hum_UP.clicked.connect(self.on_click_hum_up)
        self.pushButton_Hum_DOWN.clicked.connect(self.on_click_hum_down)
        
        
        #G/n/r/ automatiquemment
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Submit.setText(_translate("MainWindow", "Submit"))
        self.pushButton_Hum_UP.setText(_translate("MainWindow", "Up"))
        self.pushButton_Hum_DOWN.setText(_translate("MainWindow", "Down"))
        self.label_Hum.setText(_translate("MainWindow", "Humidité"))
        self.pushButton_Cancel.setText(_translate("MainWindow", "Cancel"))
        self.label_Temp.setText(_translate("MainWindow", "Température"))
        self.pushButton_Temp_UP.setText(_translate("MainWindow", "Up"))
        self.pushButton_Temp_DOWN.setText(_translate("MainWindow", "Down"))
    
    # Change l<affichage lcd de la temp/rature selon la valeur du slider
    def change_Temp_Val(self):
        self.control_Temp = self.horizontalSlider_Temp.value()
        self.lcdNumber_Temp.display(self.control_Temp)
    
    # Change l<affichage lcd de l>humidit/ selon la valeur du slider
    def change_Hum_Val(self):
        self.control_Hum = self.horizontalSlider_Hum.value()
        self.lcdNumber_Hum.display(self.control_Hum)
    
    # Ferme la fenêtre et envoie les nouvelles consignes par Signal vers MainGUI.py.
    def on_click_submit(self):
        self.objsignal.submitted.emit(self.control_Temp, self.control_Hum) #Envoie de la valeur
        self.MainWindow.close() #ferme fenêtre
    
    # Ferme la fenêtre control.py sans modifier les valeurs de consigne.
    def on_click_cancel(self):
        self.MainWindow.close()
        
    # Augmente la valeur de 1 pour la consigne de temp/rature    
    def on_click_temp_up(self):
        if(self.control_Temp < self.lim_Temp):
            self.control_Temp = self.control_Temp +1
            self.lcdNumber_Temp.display(self.control_Temp)
            self.horizontalSlider_Temp.setValue(self.control_Temp)  
            
    # Diminue la valeur de consigne de temp/rature de 1    
    def on_click_temp_down(self):
        if(self.control_Temp > 0):
            self.control_Temp = self.control_Temp -1
            self.lcdNumber_Temp.display(self.control_Temp)
            self.horizontalSlider_Temp.setValue(self.control_Temp)  
            
    # Augmente la valeur de 1 pour la consigne d>humidit/       
    def on_click_hum_up(self):
        if(self.control_Hum < self.lim_Hum):
            self.control_Hum = self.control_Hum +1
            self.lcdNumber_Hum.display(self.control_Hum)
            self.horizontalSlider_Hum.setValue(self.control_Hum)
            
    # Diminue la valeur de consigne d>humidit/ de 1
    def on_click_hum_down(self):
        if(self.control_Hum > 0):
            self.control_Hum = self.control_Hum -1
            self.lcdNumber_Hum.display(self.control_Hum)
            self.horizontalSlider_Hum.setValue(self.control_Hum)        
        
'''if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setup(MainWindow, 30, 50)
    MainWindow.show()
    sys.exit(app.exec_())'''

