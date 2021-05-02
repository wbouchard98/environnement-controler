#  @file   UTest_Hygro_SEN0227.py
#  @date   15 Fevrier 2021    
#  @author Simon Jourdenais
#  @brief  Programme de test du capteur SEN0227
#  Le programme fait imprimer la temperature en degres celsius et le pourcentage d'humidite ambiante a l'ecran, si tout
#  est bien branche. Voir le fichier README.md qui est inclus dans le dossier contenant ce fichier.
#  @material   Raspberry Pi 3 B

from sht20 import SHT20 #importation de la librairie du capteur
from time import sleep

sht = SHT20(1, resolution=SHT20.TEMP_RES_14bit) #Instanciation d'un objet pour accederaux donnees du capteur

while(1):
    data = sht.read_all() #Recueille les donnes
    temp = round(data[0],2) # Isole la donnee de temperature
    humid = round(data[1],2) # Isole la donnee d' humidite
    
    print("Temperature : "+str(temp)+" C")#Affichage
    print("Humidite : "+str(humid)+" %HR")
    sleep(1)
