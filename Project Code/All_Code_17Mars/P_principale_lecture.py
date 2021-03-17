#  @file   P_principale_lecture.py
#  @date   15 Fevrier 2021    
#  @author Simon Jourdenais
#  @brief  Programme principale du Raspberry Pi. Lecture de SEN0227, DS18B20 et lecture du port série.
#          La tramme recue contient les valeurs du CCS811. Les valeurs sont ensuites envoyées vers ThingSpeak
#          par URL(à chaque minute) et aussi envoyées au GUI MainGUI.py par MQTT sur le topic /test(+/- 2 secondes). Le programme écoute aussi le topic /test2. Lorsque le message reçoit la trame
#          contenant les consignes d'humiditées et les consignes de température, il "print" les deux valeurs. Ce programme montre que plusieurs parties du code finale sont terminées,
#          mais d'autres éléments vont y être ajoutés et ce code reste sujet a modification.
#  @material   Raspberry Pi 3 B, Arduino NANO, convertisseur 5V - 3.3V, Capteur CCS811, DS18B20, SEN0227

from time import time, sleep
import json
from urllib.request import urlopen
import sys
import serial
import paho.mqtt.client as mqtt #import the client1
import paho.mqtt.publish as publish

from sht20 import SHT20 #importation de la librairie du capteur
from w1thermsensor import W1ThermSensor


sht = SHT20(1, resolution=SHT20.TEMP_RES_14bit) #Instanciation d'un objet pour acceder aux donnees du capteur
DS18B20 = W1ThermSensor()   #Déclaration de l'objet pour accéder aux données du capteur.

#WRITE_API = "OTSESYSMRPRYTJFL" # Clé a Simon
WRITE_API = "F6AG8QMUBNAO57IL"  # Clé à William
BASE_URL = "https://api.thingspeak.com/update?api_key={}".format(WRITE_API) #Déclaration de l'URL sur lequel notre programme va communiqué avec ThingSpeak.
 
cont_temp = 0   #Variable globale pour les consignes de température
cont_hum = 0     # Variable pour les consignes d'humidité

SensorPrevSec = 0  # Variable qui prend le temps de référence pour délais d'envoie MQTT
SensorInterval = 5 # 2 secondes de délais 
ThingSpeakPrevSec = 0 #Variable qui prend le temps référence pour délais d'envoie ThingSpeak
ThingSpeakInterval = 60 # 60 secondes de délais entre uploads

#Fonction qui lit le port série. Port de lecture /dev/serial0. Données de la provenance du ARDUINO NANO. Reçoit une string contenant deux valeurs.
#Première valeur CO2, deuxième TVOC.
def read_Serial():
    global ser
    ret_Val = (-1, -1)  #Valeur mise par défault
    try:
        if ser.in_waiting > 0: 
            read_serial=ser.readline()   #lit ce qui a sur le port serie
            decoded_ser = read_serial.decode()  
            decoded_ser = decoded_ser.replace('\r\n', '')#enleve les saut de ligne
            data_CCS = decoded_ser.split(" ")#sépare les valeurs du CO2 et de TOVC

            ret_Val = (int(data_CCS[0]), int(data_CCS[1]))
            ser.flush() 
    except Exception as err:
        print(str(err))
        ser.close() #Ferme port série
    return ret_Val #Retourne les valeurs du capteur vers le main.

#Envoi les données vers ThingSpeak par URL. Contient: Température du DS18B20, Température et humidité du SEN0227, la concentartion de CO2 et le TVOC du CCS811.
#Données envoyées à la minute. ThingSpeak nous envoie le numéro de l'entré en retour si notre envoie c'est bien passé.
def save_To_Thingspeak(co2,tempDS,temp_Sol,humid_Sol, tvoc):
    try:
        thingspeakHttp = BASE_URL + "&field1={:.2f}&field2={:.1f}&field3={:.2f}&field4={:f}&field5={:f}".format(co2,tvoc,tempDS,temp_Sol,humid_Sol) #Fromattage de la string URL pour l'envoie vers ThingSpeak.
        print(thingspeakHttp)

        conn = urlopen(thingspeakHttp) #Envoie les infos vers ThingSpeak
        print("Response: {}".format(conn.read()))  #Reçoit réponse
        conn.close()

    except KeyboardInterrupt:
        conn.close()
    except Exception as err:
        print(str(err))
      
# Action lors de la connection au MQTT      
def on_connect(client, userdata, flags, rc):
    print("connected")  # Laisse savoir à l'usager qu'il est bien connecté

# Action à faire lorsqu'un message à été reçu sur /test2. 
def on_message(client, userdata, msg):
    global cont_temp, cont_hum #Fait le lien avec les variables globales
    print(msg.payload.decode())
    try:
        incomingMQTT = msg.payload  #prend le message reçu
        incomingMQTT = json.loads(incomingMQTT) #Formatte le message sous format JSON
        
        cont_temp = incomingMQTT["TEMP"]   #Constante Température changé
        cont_hum = incomingMQTT["HUM"]   #Constante d'humidité changé
        print(cont_temp)
        print(cont_hum)
    except Exception as err:
        print(err)

client = mqtt.Client("hell")   #Création du client MQTT
#Création des connections vers les fonctions des évênnements MQTT
client.on_connect = on_connect
client.on_message = on_message

client.connect("127.0.0.1") #connect to broker
client.subscribe("/test2")  #Écoute topic


client.loop_start()   

#Boucle principale
if __name__ == '__main__':
    tempDS = -1
    temp_Sol = -1
    humid_Sol = -1
    try:
        ser = serial.Serial('/dev/serial0', 9600)  #Initialise la connection avec le ARDUINO NANO
    except Exception as err:
        print(str(err))
        
    while True:

        if time()-SensorPrevSec > SensorInterval:  #Si + de deux secondes
            SensorPrevSec = time()
            
            if(ser.is_open == 0):
                ser.open()
                
            tup_Read= read_Serial()   #Lit port série
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
            
            #Section d'envoie MQTT pour le MainGUI.py
            try:
                json_data = json.loads('{"DS": {"temp": '+str(tempDS)+'}, "SHT": {"temp": '+str(temp_Sol)+', "hum": '+str(humid_Sol)+'}, "CSS811": {"CO2": '+str(co2)+', "TVOC": '+str(tvoc)+'}}')
                topic = "/test"
                client.publish(topic="/test", payload=json.dumps(json_data)) #Publie sur /test le JSON des valeurs de capteurs.
            except Exception as err:
                print(str(err))
            
        if time()-ThingSpeakPrevSec > ThingSpeakInterval:     #Si fait plus de une minute depuis la dernière transmission sur ThingSpeak.
            ThingSpeakPrevSec = time()
            save_To_Thingspeak(co2,tempDS,temp_Sol,humid_Sol, tvoc)
            
