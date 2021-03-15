#  @file   P_principale_lecture.py
#  @date   15 Fevrier 2021    
#  @author Simon Jourdenais
#  @brief  Programme principale du Raspberry Pi. Lecture de SEN0227, DS18B20 et lecture du port serie.
#          La tramme recu contient les valeurs du CCS811. Les valeurs sont ensuites envoyees vers ThingSpeak
#          par URL et aussi envoy/ au GUI MainGUI.py par MQTT sur le topic /test. Le programme /coute aussi le topic /test2. Lorsque le message recoit la trame
#          contenant les consignes d<humidit/es et les consignes de temp/rature, il print les deux valeurs. Ce programme montre que plusieurs parties du code finale sont termin/,
#          mais d'autres /l/ments vont y etre ajout/ et ce code reste sujet a modification.
#  @material   Raspberry Pi 3 B

from time import time, sleep
import json
from urllib.request import urlopen
import sys
import serial
import paho.mqtt.client as mqtt #import the client1
import paho.mqtt.publish as publish

from sht20 import SHT20 #importation de la librairie du capteur
from w1thermsensor import W1ThermSensor


sht = SHT20(1, resolution=SHT20.TEMP_RES_14bit) #Instanciation d'un objet pour accederaux donnees du capteur
DS18B20 = W1ThermSensor()

#WRITE_API = "OTSESYSMRPRYTJFL" # Replace your ThingSpeak API key here
WRITE_API = "F6AG8QMUBNAO57IL"
BASE_URL = "https://api.thingspeak.com/update?api_key={}".format(WRITE_API)
 
cont_temp = 0
cont_hum = 0

SensorPrevSec = 0
SensorInterval = 5 # 2 secondes de délais 
ThingSpeakPrevSec = 0
ThingSpeakInterval = 60 # 60 secondes de délais entre uploads


def read_Serial():
    global ser
    ret_Val = (-1, -1)
    try:
        if ser.in_waiting > 0:
            read_serial=ser.readline()   #lit ce qui a sur le port serie
            decoded_ser = read_serial.decode()  
            decoded_ser = decoded_ser.replace('\r\n', '')#enleve les saut de ligne
            data_CCS = decoded_ser.split(" ")#separe les valeurs du CO2 et de TOVC

            ret_Val = (int(data_CCS[0]), int(data_CCS[1]))
            ser.flush()
    except Exception as err:
        print(str(err))
        ser.close()
    return ret_Val

def save_To_Thingspeak(co2,tempDS,temp_Sol,humid_Sol, tvoc):
    try:
        thingspeakHttp = BASE_URL + "&field1={:.2f}&field2={:.1f}&field3={:.2f}&field4={:f}&field5={:f}".format(co2,tvoc,tempDS,temp_Sol,humid_Sol)
        print(thingspeakHttp)

        conn = urlopen(thingspeakHttp)
        print("Response: {}".format(conn.read()))
        conn.close()

    except KeyboardInterrupt:
        conn.close()
    except Exception as err:
        print(str(err))
        
def on_connect(client, userdata, flags, rc):
    print("connected")
    
def on_message(client, userdata, msg):
    global cont_temp, cont_hum
    print(msg.payload.decode())
    try:
        incomingMQTT = msg.payload
        incomingMQTT = json.loads(incomingMQTT)
        
        cont_temp = incomingMQTT["TEMP"]
        cont_hum = incomingMQTT["HUM"]
        print(cont_temp)
        print(cont_hum)
    except Exception as err:
        print(err)

client = mqtt.Client("hell")
client.on_connect = on_connect
client.on_message = on_message

client.connect("127.0.0.1") #connect to broker
client.subscribe("/test2")


client.loop_start()

if __name__ == '__main__':
    tempDS = -1
    temp_Sol = -1
    humid_Sol = -1
    try:
        ser = serial.Serial('/dev/serial0', 9600)
    except Exception as err:
        print(str(err))
        
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
            
            try:
                json_data = json.loads('{"DS": {"temp": '+str(tempDS)+'}, "SHT": {"temp": '+str(temp_Sol)+', "hum": '+str(humid_Sol)+'}, "CSS811": {"CO2": '+str(co2)+', "TVOC": '+str(tvoc)+'}}')
                topic = "/test"
                client.publish(topic="/test", payload=json.dumps(json_data)) 
            except Exception as err:
                print(str(err))
            
        if time()-ThingSpeakPrevSec > ThingSpeakInterval:
            ThingSpeakPrevSec = time()
            save_To_Thingspeak(co2,tempDS,temp_Sol,humid_Sol, tvoc)
            
