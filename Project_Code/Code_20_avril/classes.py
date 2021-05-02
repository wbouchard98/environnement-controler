from simple_pid import PID
import RPi.GPIO as GPIO
import serial

class c_Control():
    def __init__(self):
        self.cont_temp = 0   #Variable globale pour les consignes de température
        self.cont_hum = 0     # Variable pour les consignes d'humidité
        self.pid_HeatMat = PID(2,1,5, setpoint=self.cont_temp)
        self.pid_HeatMat.output_limits = (0, 255)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(40, GPIO.OUT)
        self.soft_pwm = GPIO.PWM(40,500)
        self.soft_pwm.start(50)
        
        
    
    def pidTemp(self, tempDS):        
        if(tempDS != -1):
            control = self.pid_HeatMat(tempDS)

            print(control)
            controlcent = control*100/255
            print(controlcent)
            self.soft_pwm.ChangeDutyCycle(controlcent)
            
        else:
            print("TEMP CONTROL ERROR")
            
class c_Mesure:
    def __init__(self):
        self.tempRPI = -1
        self.co2 = -1
        self.tvoc = -1
        self.tempSEN = -1
        self.humSEN = -1
        self.tempDS = -1
        try:
            self.ser = serial.Serial('/dev/serial0', 9600, timeout=2)  #Initialise la connection avec le ARDUINO NANO
        except Exception as err:
            print(str(err))
        
    def updateValue(self):
        if(self.ser.is_open == 0):
            self.ser.open()
            
        tup_Read = self.read_Serial()   #Lit port série
        self.tempRPI = -1
        self.co2 = tup_Read[0]
        self.tvoc = tup_Read[1]
        self.tempSEN = tup_Read[2]
        self.humSEN = tup_Read[3]
        self.tempDS = tup_Read[4]
        
    def read_Serial(self):
        ret_Val = (-1, -1, -1, -1, -1)  #Valeur mise par défault
        try:
            if self.ser.in_waiting > 0: 
                read_serial=self.ser.readline()   #lit ce qui a sur le port serie
                decoded_ser = read_serial.decode()  
                decoded_ser = decoded_ser.replace('\r\n', '')#enleve les saut de ligne
                data_CCS = decoded_ser.split(";")#sépare les valeurs du CO2 et de TOVC
                print(data_CCS[0]+" "+data_CCS[1]+" "+ data_CCS[2] +" "+ data_CCS[3]+" "+data_CCS[4])
                ret_Val = (int(data_CCS[2]), int(data_CCS[3]), float(data_CCS[0]), float(data_CCS[1]), float(data_CCS[4]))
                self.ser.flushInput() 
        except Exception as err:
            print(str(err))
            self.ser.close() #Ferme port série
        return ret_Val #Retourne les valeurs du capteur vers le main.

        
        