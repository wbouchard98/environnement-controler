from sht20 import SHT20
from w1thermsensor import W1ThermSensor
from time import sleep
import json, paho.mqtt.client as mqtt


sensor = W1ThermSensor() #Declaration d'un objet de la classe W1ThermSensor pour recueillir les donnees du capteur
sht = SHT20(1, resolution=SHT20.TEMP_RES_14bit)

def msg_Received(client, userdata, message):
    topic = str(message.topic)
    message = str(message.payload.decode('utf-8'))
    print("Message In! Topic: "+topic+"\n\rMessage: "+message)

client = mqtt.Client("python") #create new instance
client.on_message=msg_Received
client.connect('127.0.0.1', 1883) #connect to broker   // Definit canal de communication avec broker
client.subscribe("/sensor/SHT20")#subscribe
client.loop_start() #start loop to process received messages


while(1):
    temp_DS = sensor.get_temperature() #lecture des donnes
    data = sht.read_all()
    temp = round(data[0],2)
    humid = round(data[1],2)
    
    json_Obj = 'tempSHT20 : '+str(temp).zfill(2)+', humidSHT20 : '+str(humid).zfill(2)
    client.publish("/sensors/SHT20",json_Obj)
    
    print("Temp Thermometre: %s C" % temp_DS) #Affichage de la lecture
    print("Temp Hygrometre : "+str(temp)+" C")
    print("Hum  : "+str(humid)+" %HR")
    sleep(1)
    
client.disconnect() #disconnect
client.loop_stop()