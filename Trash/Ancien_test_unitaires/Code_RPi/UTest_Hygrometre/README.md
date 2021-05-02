README pour le fichier UTest_Hygro_SEN0227.py


BRANCHEMENT :

L'hygrometre SEN0227 doit etre alimente avec 3.3 Volts, son 'SDA' branche dans l'entree IO2 et le 'SCL' dans l'entree IO3.


PREALLABLES :

Pour executer ce programme de test unitaire vous devez preallablement configurer votre Raspberry Pi. 
Executer la commande 'sudo raspi-config', puis dans la section 'Interfaces', activez l'interface 'I2C'.

De plus, executez la ligne 'sudo pip3 install sht20' pour installer la librairie du capteur.


EXECUTION : 

Une fois fait, ouvrez un terminal dans le dossier UTest_Hygro et executez la ligne 'python UTest_Hygro_SEN0227.py'.
Les valeur lues du capteur seront alors affichees dans le terminal si tout est bien branche et que les preallables on ete faits et/ou installes.