README pour le fichier UTest_Thermo_DS18B20.py


BRANCHEMENT :

Le thermometre DS18B20 doit etre alimente avec 5 volts ou 3.3 Volts et le brancher sur l'entree IO4, qui corresponds a la pin 1-Wire.
Ne pas oublier d'ajouter une pull-up de 4.7k sur le one-wire



PREALLABLES :

Pour executer ce programme de test unitaire vous devez preallablement configurer votre Raspberry Pi. 
Executer la commande 'sudo raspi-config', puis dans la section 'Interfaces', activez l'interface '1-Wire'.

De plus, executez la ligne 'sudo pip3 install w1thermsensor' pour installer la librairie du thermometre dans le dossier contenant ce fichier.



EXECUTION : 

Une fois fait, ouvrez un terminal dans le dossier UTest_Thermo et executez la ligne 'python UTest_Thermo_DS18B20.py'.
La valeur lue du thermometre sera alors affiche dans le terminal si tout est bien branche et que les preallables on ete faits et/ou installes.


