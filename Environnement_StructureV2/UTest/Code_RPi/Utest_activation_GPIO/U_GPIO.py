#!/usr/bin/python


#  @file   UTest_Thermo_DS18B20.py
#  @date   Fevrier 2021    
#  @brief  Permet de s'assurer du bon fonctionnement de la librairie RPi.GPIO.
#          Voir le Read_me pour plus de détails.
	
#  @material   Raspberry Pi 3 B

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(36,GPIO.OUT)

GPIO.output(36,1)
time.sleep(5)
GPIO.cleanup()