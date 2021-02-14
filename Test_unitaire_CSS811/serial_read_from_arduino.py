'''Programme de lecture du port serie.
Recoit une string sur le port serial sur les pin 8(TX) et 10(RX)
Affiche cette string sur le terminal.
Sert a tester la fonctionnaliter de la communivcation entre le arduino (CCS811.c) et le RPi
'''
import serial

ser = serial.Serial('/dev/serial0', 9600)
#s = [0]

while 1:
    read_serial=ser.readline()
    
    #s[0] =str(int (ser.readline(), 16))
    #print(s[0])
    print(read_serial.decode())