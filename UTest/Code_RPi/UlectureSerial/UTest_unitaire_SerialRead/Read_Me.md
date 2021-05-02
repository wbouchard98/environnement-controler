Test unitaire pour la lecture du port série.
Le faire marcher avec le code CCS811.c du Arduino Nano permet de vérifier si la communication série est bien établie et si le capteur CCS811 est fonctionnel.
Permet aussi de s'assurer que la configuration du port série du Raspberry Pi à bien été faite.

Matériel:
	ARDUINO NANO
	CONVERTISSEUR 5v -> 3.3V
	RASPBERRY PI 3B

Connexion:

		ARDUINO NANO -> CONVERTISSEUR(HIGH/LOW) -> RASPBERRY PI 3B
			GND  ->  	GND <-> GND    	<-  GND		#Connection du GND entre le RPi et le ARDUINO direct + connexion au GND du convertisseur
			5V   ->		HV  :  LV       <-  3.3V
			RX0  ->         HV3 :  LV3      <-  TX(Pin8)
			TX1  ->         HV1 :  LV1      <-  RX(Pin10)


Le programme suivant devrait lire ce qui est sur le port série et afficher le résultat en console.
