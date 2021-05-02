#  @file   UTest_Hygro_SEN0227.py
#  @date   15 Fevrier 2021    
#  @author Simon Jourdenais
#  @brief  Programme de test du capteur SEN0227
#  Le programme fait imprimer la temperature en degres celsius et le pourcentage d'humidite ambiante a l'ecran, si tout
#  est bien branche. Voir le fichier README.md qui est inclus dans le dossier contenant ce fichier.
#  @material   Raspberry Pi 3 B

from time import time, sleep
from urllib.request import urlopen
import sys
import serial
from sht20 import SHT20 #importation de la librairie du capteur
from w1thermsensor import W1ThermSensor


sht = SHT20(1, resolution=SHT20.TEMP_RES_14bit) #Instanciation d'un objet pour accederaux donnees du capteur
DS18B20 = W1ThermSensor()

'''
while(1):
    
    print("Temp LED : " + str(tempDS)+" °C")
    print("Temp Sol : "+str(temp)+" °C")#Affichage
    print("Humid. Sol : "+str(humid)+" %HR")
    sleep(2.5)
'''

WRITE_API = "OTSESYSMRPRYTJFL" # Replace your ThingSpeak API key here
BASE_URL = "https://api.thingspeak.com/update?api_key={}".format(WRITE_API)
 
 

SensorPrevSec = 0
SensorInterval = 5 # 2 secondes de délais 
ThingSpeakPrevSec = 0
ThingSpeakInterval = 60 # 60 secondes de délais entre uploads

def read_Serial():
    ret_Val = (-1, -1)
    try:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            if "ppm" in line:
                    ret_Val = (int(line[5:line.index("ppm")]), int(line[line.index("TVOC: ")+6:len(line)]))
            #print(line)
            ser.flush()
    except Exception as err:
        print(str(err))
        ser.close()
    return ret_Val

def save_To_Thingspeak(co2,tempDS,temp_Sol,humid_Sol, tvoc):
    try:
        thingspeakHttp = BASE_URL + "&field1={:.2f}&field2={:.1f}&field3={:.2f}&field4={:f}&field5={:f}".format(tempDS,humid_Sol,temp_Sol,co2,tvoc)
        print(thingspeakHttp)

        conn = urlopen(thingspeakHttp)
        print("Response: {}".format(conn.read()))
        conn.close()

    except KeyboardInterrupt:
        conn.close()
    except Exception as err:
        print(str(err))
        
        
if __name__ == '__main__':
    tempDS = -1
    temp_Sol = -1
    humid_Sol = -1
    try:
        ser = serial.Serial('/dev/ttyUSB0', 9600)
    except Exception as err:
        print(str(err))
        #sleep(5)
    while True:

        if time()-SensorPrevSec > SensorInterval:
            SensorPrevSec = time()
            
            if(ser.is_open == 0):
                ser.open()
                
            tup_Read= read_Serial()
            co2 = tup_Read[0]
            tvoc = tup_Read[1]
            try:
                tempDS = DS18B20.get_temperature()
            except Exception as err:
                print(str(err))
            try:
                data = sht.read_all() #Recueille les donnes
                temp_Sol = round(data[0],2) # Isole la donnee de temperature
                humid_Sol = round(data[1],2) # Isole la donnee d' humidite
            except Exception as err:
                print(str(err))
            print("CO2 (ppm) : " + str(co2))
            print("TVOC : " + str(tvoc))
            print("Temp LED (°C) : " + str(tempDS))
            print("Humid Sol (%RH) : " + str(humid_Sol))
            print("Temp Sol (°C) : " + str(temp_Sol))
            
            
        if time()-ThingSpeakPrevSec > ThingSpeakInterval:
            ThingSpeakPrevSec = time()
            save_To_Thingspeak(co2,tempDS,temp_Sol,humid_Sol, tvoc)`
            