#!/usr/bin/python

#print("90s")
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(36,GPIO.OUT)

GPIO.output(36,1)
time.sleep(5)
GPIO.cleanup()