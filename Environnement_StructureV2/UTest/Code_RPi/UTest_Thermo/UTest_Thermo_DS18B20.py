#  @file   UTest_Thermo_DS18B20.py
#  @date   15 Fevrier 2021    
#  @author Simon Jourdenais
#  @brief  Programme de test du thermometre DS18B20
#  Le programme fait imprimer la température en degrés celsius, si tout est bien branché. Voir
#  le fichier README.md qui est inclus dans le dossier contenant ce fichier.
#  @material   Raspberry Pi 3 B, DS18B20

import time
from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor() #Declaration d'un objet de la classe W1ThermSensor pour recueillir les donnees du capteur

while(1):
    temperature = sensor.get_temperature() #lecture des donnes
    print("Temp : %s C" % temperature) #Affichage de la lecture
    time.sleep(0.25)