#  @file   UTest_Thermo_DS18B20.py
#  @date   15 Fevrier 2021    
#  @author Simon Jourdenais
#  @brief  Programme de lecture du port serie.
#	   Recoit une string sur le port serial sur les pin 8(TX) et 10(RX)
#          Affiche cette string sur le terminal.
#          Sert a tester la fonctionnaliter de la communivcation entre le arduino (CCS811.c) et le RPi
#	   Voir le Read_me avant son utilistaion.
#  @material   Raspberry Pi 3 B

import serial

ser = serial.Serial('/dev/ttyAMA0', 9600)


while 1:
    read_serial=ser.readline()

    print(read_serial.decode())