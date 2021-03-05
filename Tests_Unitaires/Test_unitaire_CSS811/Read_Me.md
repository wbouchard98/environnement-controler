Test unitaire pour le fonctionnement du capteur CCS811. 
IMPORTANT!!!!!! Le capteur de CO2 nécessite 48H de marche, après chaque mise a l'arrêt avant de donner des donées précises.

Matériel:
	ARDUINO NANO
	CONVERTISSEUR 5v -> 3.3V
	RASPBERRY PI 3B
	CAPTEUR CCS811

Connexion:
	Pour que le test du capteur CCS811 fonctionne, les connexions suivantes doivent être éffectuées:

		ARDUINO NANO -> CC811:
			GND  ->  GND
			5V   ->  VCC
			A4   ->  SDA
			A5   ->  SCL
			GND  ->  WAKE
			N.C. ->  RST, INT

		ARDUINO NANO -> CONVERTISSEUR(HIGH/LOW) -> RASPBERRY PI 3B
			GND  ->  	GND <-> GND    	<-  GND		#Connection du GND entre le RPi et le ARDUINO direct + connexion au GND du convertisseur
			5V   ->		HV  :  LV       <-  3.3V
			RX0  ->         HV3 :  LV3      <-  TX(Pin8)
			TX1  ->         HV1 :  LV1      <-  RX(Pin10)

Prérequis:
	Programme Arduino:
		Pour le bon fonctionnement du programme Arduino, la librairie "Adafruit_CCS811" est nécessaire.
		Pour l'installer dans l'IDE ARDUINO:
			1) Ouvrir l'IDE ARDUINO
			2) Cliquer sur 'Croquis' dans la barre d'outils.
			3) Sélectionner 'Inclure une bibliothèque', puis 'Gérer les bibliothèque'.
			4) Dans la nouvelle fenêtre, assurez-vous que 'Type' et 'Sujet' sois a 'Tout'.
			5) Dans le filtre de recherche, tapez 'CCS811' et une librairie Adafruit devrait être disponible. Cliquer sur 'Installer'.
			6) Redémarrez l'IDE.


			
Transfert du code ARDUINO (CCS881.c):
	1) Assurez-vous que les options de téleversement soient les bonnes. (Carte: "Arduino Duemilanove", Processeur: "ATmega328p", PORT: Choisir le bon, Programmateur: "AVR ISP")
	2) Avant de téléverser le code, débrancher les connections rx/tx du ARDUINO NANO pour que le port série communique bien avec celui de l'ordinateur.
	3) Une fois le code téléverser, refaire les connections RX/TX.


Démarrage du code du RASPBERRY PI (serial_read_from_arduino.py):
	1) Une fois le transfert du code ARDUINO fait, simplement ouvrir l'IDE Thonny et partir le programme python.
	2) Les messages devraient s'afficher dans le terminal. 			
