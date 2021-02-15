#!/usr/bin/python

import time
import RPi.GPIO as GPIO
from w1thermsensor import W1ThermSensor

GPIO.cleanup()
sensor=W1ThermSensor()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(36,GPIO.OUT)  #simule lactivation du bye bye chaud
GPIO.output(36,0)
chaud_actif=False
while True:
    temperature = sensor.get_temperature()
    print("Temp = %s" % temperature)
    if (temperature > 26):
        GPIO.output(36,1)
        chaud_actif=True
    elif (temperature <24 and chaud_actif==True):
        GPIO.output(36,0)
        chaud_actif==False
    
    time.sleep(1)