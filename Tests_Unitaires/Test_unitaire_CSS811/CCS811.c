/***************************************************************************
  This is a library for the CCS811 air

  This sketch reads the sensor

  Designed specifically to work with the Adafruit CCS811 breakout
  ----> http://www.adafruit.com/products/3566

  These sensors use I2C to communicate. The device's I2C address is 0x5A

  Adafruit invests time and resources providing this open source code,
  please support Adafruit andopen-source hardware by purchasing products
  from Adafruit!

  Written by Dean Miller for Adafruit Industries.
  BSD license, all text above must be included in any redistribution
 ***************************************************************************/
/*
 * 
 * Programme test pour la lecture des donnees du capteur de CO2 CCS811 sur ardui nano
 * IMPORTANT: Ceci n'est pas un code pour le Raspberry Pi, mais bien pour le ARDUINO NANO.
 * Ce programme prend les valeurs de PPM du capteur et de TVOC pour les envoyer sur le port
 * serie. 
 * Marche en parrallele avec le programme serial_read_from_arduino.py sur le RASPBERRY PI.
 * 
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
