
/* @file CCS811.c
 * @date Fevrier 2021
 * 
 * @brief Programme test pour la lecture des données du capteur de CO2 CCS811 sur ardui nano
 * IMPORTANT: Ceci n'est pas un code pour le Raspberry Pi, mais bien pour le ARDUINO NANO.
 * Ce programme prend les valeurs de PPM du capteur et de TVOC pour les envoyer sur le port
 * série. 
 * Marche en parrallèle avec le programme Userial_read_from_arduino.py sur le RASPBERRY PI.
 * Veuillez lire le Read_me.md associer à ce programme avant son utilisation.

 * @material   Arduino Nano, CCS811
 * */
#include "Adafruit_CCS811.h"

Adafruit_CCS811 ccs;

void setup() {
  Serial.begin(9600);

  Serial.println("CCS811 test");

  if(!ccs.begin()){
    Serial.println("Failed to start sensor! Please check your wiring.");
    while(1);
  }

  // Wait for the sensor to be ready
  while(!ccs.available());
}
//Boucle principale qui lit les data du capteur CCS811 et qui les envoies au RPi.
void loop() {
  if(ccs.available()){
    if(!ccs.readData()){
      Serial.print("CO2: ");
      Serial.print(ccs.geteCO2());
      Serial.print("ppm, TVOC: ");
      Serial.println(ccs.getTVOC());
    }
    else{
      Serial.println("ERROR!");
      while(1);
    }
  }
  delay(500);
}
