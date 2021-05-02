README pour le fichier UTest_Thermo_DS18B20.py


BRANCHEMENT :

Le thermomêtre DS18B20 doit être alimenté avec 5 volts ou 3.3 Volts et le brancher sur l'entrée IO4, qui corresponds à la pin 1-Wire.
Ne pas oublier d'ajouter une pull-up de 4.7k sur le one-wire



PRÉALLABLES :

Pour exécuter ce programme de test unitaire, vous devez préallablement configurer votre Raspberry Pi. 
Exécuter la commande 'sudo raspi-config', puis dans la section 'Interfaces', activez l'interface '1-Wire'.

De plus, exécutez la ligne 'sudo pip3 install w1thermsensor' pour installer la librairie du thermomêtre dans le dossier contenant ce fichier.



EXÉCUTION : 

Une fois fait, ouvrez un terminal dans le dossier UTest_Thermo et exécutez la ligne 'python UTest_Thermo_DS18B20.py'.
La valeur lue du thermomêtre sera alors affichée dans le terminal si tout est bien branché et que les préallables on été faits et/ou installés.


