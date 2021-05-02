README pour le fichier UTest_Hygro_SEN0227.py


BRANCHEMENT :

L'hygromètre SEN0227 doit être alimenté avec 3.3 Volts, son 'SDA' branché dans l'entrée IO2 et le 'SCL' dans l'entrée IO3.


PRÉALLABLES :

Pour executer ce programme de test unitaire, vous devez préallablement configurer votre Raspberry Pi. 
Éxecuter la commande 'sudo raspi-config', puis dans la section 'Interfaces', activez l'interface 'I2C'.

De plus, executez la ligne 'sudo pip3 install sht20' pour installer la librairie du capteur.


EXÉCUTION : 

Une fois fait, ouvrez un terminal dans le dossier UTest_Hygro et exécutez la ligne 'python UTest_Hygro_SEN0227.py'.
Les valeurs lues du capteur seront alors affichées dans le terminal si tout est bien branché et que les préallables on été faits et/ou installés.
