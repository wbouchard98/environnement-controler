Test unitaire pour tester la librairie RPi.GPIO.

Le test sert à savoir si les librairies de base python ont bien été installées. (Pour installer python: sudo apt-get install pyhton3)

Le script met un état haut au GPIO-16 du Pi pendant 5 secondes.

Matériel:

	RASPBERRY PI 3B

PRÉALLABLES :

	Vous deves avoir la librairie RPi.GPIO. Pour l'installée, entrer la commande suivante dans un terminal: sudo pip3 install RPi.GPIO

EXÉCUTION : 

	Excécuter le programme et vérifier l'état du GPIO-16 du RaspberryPi. Si un état haut de 5 secondes est détecté, alors la librairie devrait être OK.