#  @file   test_tri_unitaire.py
#  @date   16 Fevrier 2021    
#  @author William Bouchard
#  @brief  Programme de test du thermometre DS18B20, capteur de CO2 et SEN0277.
#          Lecture des valeurs des capteurs et formattage en JSON.
#          Envoi des donnees sur InfluxDB en local.
#          Ce programme fait une boucle au 10 secondes.
#          Beaucoup de variable globale qui vont etre changer en objet dans le futur et le programme finale.
#  @material   Raspberry Pi 3 B, Arduino Nano, Capteur CCS811, Capteur SEN0277 et Capteur DS18B20.

import time
import serial
import json

from influxdb import InfluxDBClient
from w1thermsensor import W1ThermSensor
from sht20 import SHT20 #importation de la librairie du capteur


sensorDS = W1ThermSensor() #Declaration d'un objet de la classe W1ThermSensor pour recueillir les donnees du capteur
sht = SHT20(1, resolution=SHT20.TEMP_RES_14bit) #Instanciation d'un objet pour accederaux donnees du capteur
ser = serial.Serial('/dev/serial0', 9600)    #Set-up le port serie

#Declaration des variables globales
tempDS=0
tempSHT=0
humSHT=0
coCCS=0
tvocCCS=0

#Lecture des donnees du capteur DS18B20
def f_lecture_DS():
    global tempDS
    tempDS = sensorDS.get_temperature() #lecture des donnes

#Lecture des donnes ducapteur SEN0227
def f_lecture_sht():
    global tempSHT
    global humSHT
    data = sht.read_all() #Recueille les donnes
    tempSHT = round(data[0],2) # Isole la donnee de temperature
    humSHT = round(data[1],2) # Isole la donnee d' humidite

#Lecture des donnees du capteur CCS811
def f_lecture_CCS():
    global coCCS
    global tvocCCS
    read_serial=ser.readline()   #lit ce qui a sur le port serie
    decoded_ser = read_serial.decode()  
    decoded_ser = decoded_ser.replace('\r\n', '')#enleve les saut de ligne
    data_CCS = decoded_ser.split(" ")#separe les valeurs du CO2 et de TOVC
    coCCS = data_CCS[0]
    tvocCCS = data_CCS[1]
    
#Fonction test pour voir si les valeurs sont bonnes    
def f_print():
    global tempDS
    global tempSHT
    global humSHT
    global coCCS
    global tvocCCS
    print("Temp : %s C" % tempDS) #Affichage de la lecture
    print("Temperature : "+str(tempSHT)+" C")#Affichage
    print("Humidite : "+str(humSHT)+" %HR")
    print("CO2 : "+coCCS)
    print("TVOC : "+tvocCCS +"\n")

#Fonction test qui s'occupe de formatter les valeurs en JSON
def f_JSON():
    global tempDS, tempSHT, humSHT, coCCS, tvocCCS
    json_data = json.loads('{"DS": {"temp": '+str(tempDS)+'}, "SHT": {"temp": '+str(tempSHT)+', "hum": '+str(humSHT)+'}, "CSS811": {"CO2": '+str(coCCS)+', "TVOC": '+str(tvocCCS)+'}}')
    
    #tempdsb = json_data["DS"]["temp"]
    #print(tempdsb)
    print(json_data)
    
#Fonction qui sert a ecrire dans la base de donnees Influx.
def f_write_influx():
    global tempDS, tempSHT, humSHT, coCCS, tvocCCS
    #Formation du message d'envoie vers Influx
    try:
        json_body = [
            {
                "measurement": "testlol",
                "fields": {
                    "Temperature_DS": tempDS,
                    "Temperature_SHT": tempSHT,
                    "Humi_SHT": humSHT,
                    "CO2_CCS811": coCCS,
                    "TVOC_CCS811": tvocCCS
                    }
                }
            ]
        client = InfluxDBClient("127.0.0.1",8086,'bruce','iambatman','vroomvroom')  #connection
        client.write_points(json_body)
        client.close()
        print("data written")
    except Exception as ex:
        print(str(ex))
#Boucle principale du programme      
while(1):
    f_lecture_DS()
    f_lecture_sht()
    f_lecture_CCS()
    #f_print()
    f_JSON()
    f_write_influx()
    time.sleep(10)   
    
