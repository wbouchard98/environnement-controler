Test unitaire qui permet de simuler l'activation de la ventilation qui a pour but
de refroidir la chambre. Une LED sur le Shiled Raspberry simule l'activation de la
ventilation theorique (GPIO-16).

Capteur: ds18b20
Entree One-wire: GPIO-04
Librairie requise: w1thermsensor et RPI.GPIO


Pour l'utiliser, faites monter la temperature plus haut que 26 Celcius en rechauffant le capteur dans vos mains. (GPIO-16 etat haut)
Pour le refroidir, tremper le dans l'eau pour que la temperature descende en bas de 24 Celcius. (GPIO-16 etat bas)