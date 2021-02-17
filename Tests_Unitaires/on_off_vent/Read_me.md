Test unitaire qui permet de simuler l'activation de la ventilation qui a pour but
de refroidir la chambre. Une LED sur le Shield Raspberry simule l'activation de la
ventilation théorique (GPIO-16).

Capteur: ds18b20
Entrée One-wire: GPIO-04
Librairie requise: w1thermsensor et RPI.GPIO
Le One-wire doit être activé sur le Raspberry Pi.


Pour l'utiliser, faites monter la température plus haut que 26 Celcius en réchauffant le capteur dans vos mains. (GPIO-16 état haut)
Pour le refroidir, tremper le dans l'eau pour que la température descende en bas de 24 Celcius. (GPIO-16 etat bas)
