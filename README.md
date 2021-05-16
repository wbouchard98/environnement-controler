# environnement-controlé
Collaborateurs : Simon Jourdenais (Symon4k18) et William Bouchard (wbouchard98)

Ce repo contient les codes du projet de Serres Domestiques Automatisées, anciennement appelées Environnement Controlé.

Les dossier et fichiers intitulés 'UTest_' sont des tests unitaires.
Le dossier "Ancien_test_unitaires" contient plusieurs anciens code que nous avons pensé nécessaire, mais après restructuration de notre projet, avons abandonné. Ces codes ne seront pas aussi bien expliqué et peuvent ne pas marcher, mais nous avons décidé de les laisser là comme historique de notre travaille.
Le dossier "Project_Code" contient les codes nécessaires pour faire fonctionner le projet. Plusieurs version sont disponible montrant l'évolution de notre travaille.

Le projet suivant sert à prendre des mesures de température, humidité et de qualité de l'air, par le biais de différents capteurs et de par la suite
réguler l'environnement.

Voici la liste de matériel utilisé pour le projet:
	1) RaspberryPi 3b+
	2) PCB "Bloc de capteurs" *
	3) PCB "Bloc de contrôle" *
	4) DS18B20 x2
	5) CSS811
	6) SEN0227

	*Les détails des PCB seront montré plus loin.

Pour que le RaspberryPi fonctionne pour ce projet, voici les étapes que nous avons effectué:

![RPIlogo](https://github.com/wbouchard98/hello-world/blob/1bab890407de53b6081342bc769ee3ec7076baf6/RPILOGO.png) 
# Étapes de l’installation de l’image du Raspberry Pi 

1)	Allez chercher une image de Raspberry Pi Buster Desktop 
2)	”Flash” une carte SD d’au moins 8Go avec cette image. Nous avons utilisé Balena Etcher pour cette étape.
3)	Faire la configuration du Raspberry Pi lors de son premier démarrage. Lorsqu’il vous est demandé de redémarrer le Raspberry Pi, redémarrer le.
4)	Maintenant, il faut activer les interfaces dont on aura besoin. Ouvrez un terminal, et tapez la commande : sudo raspi-config
5)	Une fois la fenêtre de configuration ouverte sélectionner l’index 5(Interfacing Options).
6)	Activer ‘’SSH’’, ‘’VNC’’, ‘’I2C’’ et ‘’1-Wire’’. Il faut aussi activer le ‘’Serial’’. Cependant lorsqu’il va être demandé s’il est désiré que le ‘’login shell’’ soit accessible depuis le serial, faire non, et lorsque l’usager est demandé de vouloir activer le ‘’Serial port hardware’’ faire oui.
7)	Redémarrez le Raspberry Pi pour effectuer les changements.
8)	Maintenant, il faut se connecter au serveur de temps pour pouvoir automatiquement mettre à jour le temps du Raspberry Pi. Ouvrez le fichier /etc/systemd/timesyncd.conf .
9)	Modifiez les lignes ‘’NTP’’ et ‘’FallbackNTP’’ pour que leur valeur sois : time.apple.com .
10)	Effectuez un : sudo systemctl restart systemd-timesync.service .
11)	Effectuer par la suite : sudo systemctl daemon-reload .
12)	Maintenant faire les ‘’update’’ et ‘’upgrade’’.
13)	Si vous utilisez un écran de petite taille, comme un écran 7" comme nous, nous vous recommandons de changer la résolution de l'écran. Pour ce faire, cliquer le logo Raspberry dans le haut de l'écran, puis aller sur "Preferences" et "Raspberry Pi Configuration". Aller dans l'onglet "Display" et puis "Set Resolution...". Nous utilisons "DMT mode 9 800x600 60Hz 4:3".

Une fois le RaspberryPi bien configuré, il faut ajouter les bonnes librairies pythons dans le RaspberryPi pour que les codes puissent bien fonctionner.

Voici les démarches à suivre pour l'installation de ces librairies:

![Pyhton](https://github.com/wbouchard98/hello-world/blob/b0a1c2ca098754fc5b32db06101120003069b15e/pyhton.PNG)
# Étapes pour l’installation des librairies Python

1) Premièrement, il faut s’assurer que Pyhton3 soit bien installé : sudo apt-get install python3 .
2) Une fois installé, il faut pouvoir accéder au I/O du Raspberry Pi. La librairie suivante va faire ce travail : sudo pip3 install RPI.GPIO
3) Pour pouvoir lire les données du capteur SEN0227 qui va lire la température de l’environnement dans lequel le Raspberry Pi se situe (et non l’environnement que l’on souhaite contrôler) : sudo pip3 install sht20 .
4) Maintenant, pour être capable de faire les communications MQTT, il nous faut un "Broker MQTT" : sudo apt-get install mosquitto : et : sudo apt-get install mosquitto-clients .
5) Une fois le "Broker" installé, il nous faut la librairie pour accéder à ce "Broker" : sudo pip3 install paho-mqtt .
6) Maintenant, il faut que notre "GUI" puisse accéder aux librairies PYQT5 : sudo apt-get install qt5-default pyqt5-dev pyqt5-dev-tools
7) Pour contrôler la plupart des éléments de l’environnement, l’utilisation d’un PID est importante. La librairie suivante va nous permettre d’utiliser des PID : sudo pip3 install simple-pid .


Maintenant il est temps d'ajouter les librairies à l'IDE Arduino:

![Arduino](https://github.com/wbouchard98/hello-world/blob/0736af7814e1af2afb997678829bb6392046420a/ardard.png)
# Étape pour l’installation des librairies Arduino

1) Adafruit_CCS811: Pour l'ajouter à l'IDE Arduino, ouvrir l'IDE Arduino, cliquer sur l'onglet "Croquis". Aller par la suite sur "Inclure une bibliothèque" et ensuite "Gérer les bibliothèques". Taper "CCS" dans la barre de recherche et une librairie du nom de "Adafruit CSS811 Library par Adafruit" devrait être disponible. Cliquer sur "Installer".  

2) DFRobot_SHT20: Pour ajouter cette librairie, visiter DFRobot/DFRobot_SHT20 (github.com) . Télécharger le repositary avec le bouton vert avec la flèche. Une fois télécharger mettre le dossier "DFRobot_SHT20-master" dans le dossier "C:\Program Files (x86)\Arduino\libraries". 

3) OneWire: Suivre les étapes pour le Adafruit_CCS811, mais taper "Onewire" dans la barre de recherche. Dans le "ComboBox" "Sujet" sélectionner "Communication". Une librairie du nom de "OneWire" devrait être disponible. Installer celle-ci. 

4) DallasTemperature: Suivre les étapes pour le Adafruit_CCS811, mais tapper "Dallas" dans la barre de recherche. Une librairie du nom de "DallasTemperature" devrait être        disponible. Installer celle-ci. 

## Explication des PCB

Notre projet contient deux PCB. L'un d'entre eux sert à la lecture des capteurs, et l'autre sert à contrôler les diverts éléments de contrôle.
### PCB bloc de capteurs

Pour lire l'état actuel de la chambre, nous avons créé un PCB qui relie plusieurs capteurs(DS18B20, SEN0227, CCS811) à un ATmega328p-AU. Les informations des capteurs sont ensuites transmises au RaspberryPi.
#### Transmission des informations
Nous utilisons la prise USB-mini pour transmettre les informations des capteurs vers le RaspberryPi. Ce même connecteur peut être utilisé pour le transfert du code .ino/.c. Nous avons aussi mis des traces pour un connecteur pour le module bluetooth HM-10.
Pour changer le mode entre Bluetooth et USB, il suffit de changer la position du cavalier JP201 et JP203 (position 1-2 Bluetooth, 2-3 USB). 
Dans notre projet nous utilisons pas le module Bluetooth, alors aucun code n'a été fait pour son utilisation, mais son ajout peut être possible grâce au PCB.
#### Alimentation
L'alimentation de ce PCB vient du câble USB, mais si on désire utiliser le module Bluetooth, alors un connecteur(J202) permet de connecter une batterie Li-po de 5V pour alimenter le montage de façon indépendante au RaspberryPi.
Comme mentionné plus tôt, nous utilisons la communication USB, alors l'alimentation provenant de batterie Li-po n'a pas été testé.
#### Communication des capteurs
##### DS18B20
Le capteur de température DS18B20 communique avec le ATmega en protocole 1-wire. La plaque contient une empreinte pour placer directement un DS18B20 en format TO-92, et un connecteur permet de pouvoir aussi utiliser un DS18B20.
##### SEN0227
Le capteur de température/humidité SEN0227 communique en I2C avec le ATmega. La plaque contient une empreinte pour placer directement un SHT-20, et un connecteur permet de pouvoir aussi utiliser un SEN0227.
##### CCS811
Le capteur de qualité de l'air CCS811 communique en I2C avec le ATmega. La plaque contient les empreintes pour placer directement CCS811 et les composants requis pour son fonctionement, et un connecteur permet de pouvoir aussi utiliser un CCS811 de Keyestudio.
La trace JP301 permet de changer l'adresse du CCS811.
##### SGP30
Le capteur de qualité de l'air SGP30 communique en I2C avec le Atmega. La plaque contient une empreinte pour placer directement un SGP30, et un connecteur permet de pouvoir aussi utiliser un "board" SGP30 de Adafruit.
Dans notre projet nous utilisons pas le SGP30, alors aucun code dans notre conteneur Github sera fait avec la considération de son utilisation, mais il sera possible de modifier le code pour l'inclure s'il est désiré.

### PCB de contrôle

Ce PCB sert à transformer les PWM du RaspberryPi, pour qu'ils soient capable de contrôler les éléments de contrôle(Lumière, ventillation, chauffage, humidificateur).

#### Connection au RaspberryPi
Le RaspberryPi se connecte au PCB par l'entremise d'un câble plat 40 pins.
#### Ventillation
La ventillation est contrôllé par le GPIO-27 du RaspberryPi. Le signal du GPIO-27 est ensuite transformer en 120 VAC par un CPC1966B pour faire fonctionner le système de ventillation.

#### Élément chauffant
Même méthode que pour la ventillation, mais le GPIO-17 est utilisé.

#### Lumière
Même principle que la ventillation, mais le GPIO-06 est utilisé.

#### Déshumidificateur
Même principle que la ventillation, mais le GPIO-22 est utilisé. On a pas intégré le déshumidificateur à notre projet, alors notre code ne contient pas son activation, mais il est possible d'ajouter son activation si désiré.

#### Humidificateur
L'humidificateur est contrôlé par le GPIO-05 du RaspberryPi. Un CPC1907B transforme le signal du RaspberryPi en signal 24V.

#### LED 100W
Une LED de 100W peut être connecté au PCB pour utiliser au lieu du panneau de lumière. Cette lumière sera contrôlé par le GPIO-13 du RaspberryPi. Un transitor permet de faire circuler le courant pour allumer la LED.

#### Ventillation du boitier
Un ventillateur à l'intérieur du boitier permet de refroidir la température de celui-ci. Ce ventillateur est contrôllé par un PWM de la pin GPIO-12 du RaspberryPi. Un transitor permet de conduire le courant à partir du 12V.

#### Ventillateur de la LED 100W
Un ventillateur qui permet de refroidir la LED de 100W. Ce ventillateur est "driver" par un transitor contrôlé par la pin GPIO-18 du RaspberryPi.

#### Connecteur 12V supplémentaire
On ajouté ce connecteur pour pouvoir ajouter d'autre élément fonctionnant sur du 12V. Comme par exemple une pompe à eau pour arroser la terre ou un ventillaeur supplémentaire. Ce connecteur sera contrôler par la pin GPIO-19 du RaspberryPi.

## Utilisation de l'interface graphique
L'interface graphique se compose de deux sections: un menu ancré sur la gauche de l'écran et l'affichage principale qui occupe le restant. Voir figure ci-dessus.
![SecGUI](https://github.com/wbouchard98/hello-world/blob/8abe3be088b4d87ddb48692b84ce3599287a2228/sectionGUI.png)

Le menu nous permet de naviguer entre 4 modes de GUI différents. Le premier est le mode monitorage, le deuxième est le mode consigne, le troisième est le mode paramètre et finalement le dernier est le mode administrateur.

### Mode Monitorage
Le mode monitorage est bien simple; il affiche les valeurs reçues. Les valeurs sont la température, l'humidité, la concentration de C02 et la quantité de matière organique dans l'air. Voir la figure ci-dessus pour exemple de l'affichage en mode monitorage.
![MonGUI](https://github.com/wbouchard98/hello-world/blob/fc8c7f09e50d0535397c7cd5c68dbf6a1d3f6e35/monitoring.png)

### Mode Consigne
Le mode consigne permet à l'usager d'accomplir plusieurs tâches. Premièrement, une section de l'affichage est réservé à afficher les valeurs de consignes courantes. Une autre section sert à modifier manuellement les valeurs des consignes courantes. Les valeurs à l'écran dans la section de l'affichage des consignes vont changer avec les modifications effectué. L'autre section sert à choisir ou enregistrer des valeurs de consignes. Ces valeurs sont alors réutilisables si l'usager souhaite les utiliser plus tard, ou si le système est mis hors tension. Voir la figure ci-dessus pour un visuel du GUI en mode consigne.
![ConGUI](https://github.com/wbouchard98/hello-world/blob/12d96521d4533a530a72c2a7a51c8ea9c224a35f/infoconsigne.png)

### Mode Paramètre
Le mode paramètre nous permet de se connecter à la base de données ThingSpeak, de se connecter à un réseau Wi-Fi et à voir des informations utiles pour l'usgaer. Pour pouvoir entrer les informations requises de Thingspeak et du Wi-Fi, un clavier sera nécessaire. Simplement le brancher dans un port USB du RaspberryPi. L'iamge ci-dessous nous permet de voir un exemple de la fenêtre paramètre.
![ParaGUI](https://github.com/wbouchard98/hello-world/blob/5c9a7b863dd67d611bd76d9151b4cd8fe0018b1b/pramertredf.png)

### Mode Administrateur
Le mode Administarteur permet de contrôler manuellement les éléments de contrôle. Cette fenêtre est très utile pour vérifier le fonctionnment de son matériel. Des "sliders" servent à ajuster le PWM des éléments et ainsi dicter leur intensité de fonctionnment. Voir la figure ci-dessus pour un apperçu.

![AdminGUI](https://github.com/wbouchard98/hello-world/blob/c58ebe2f87ef538df8b078601df17fc888be1bdc/admin.png)


