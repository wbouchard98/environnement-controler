#include <OneWire.h> 
#include <Wire.h>
#include <DallasTemperature.h>
//#include <PID_v1.h>
#include <Adafruit_CCS811.h>
#include <DFRobot_SHT20.h>
//#include "Adafruit_seesaw.h"



//#define HEATCABLE 3
#define ONE_WIRE_BUS 2 
#define UPDATE_DELAY_MS 1000

//void readCableTemp();
void readCCS();
void readSHT20();
//void setPIDOutput();
void initCCS811();
void initSHT20();
void readDS18B20();
//float mapFloatToPercent(float var, float inLow, float inHigh);

/*const char * states[]= 
{
  "OFF",
  "MAINTAIN",
  "HEATING"
};*/

/*enum stateEnums 
{
  OFF=0,
  MAINTAIN,
  HEATING
};*/

unsigned long pastTime = 0; //last time the sensor was triggered
unsigned long currentTime = millis();

//Vars pour PID
/*stateEnums state_PID = OFF;
double currentTemp; 
double PIDOut = 0;
double difference = 6;
double setPoint = 30;
int Kp = 10;
int Ki = 5;
int Kd = 2;
*/
//Vars pour le capteur Keyestudio CCS811 (Adafruit 3566 https://www.adafruit.com/product/3566)
int ppm_Dioxide=-1;
int ppb_TVOC=-1;

//Vars pour le capteur DFRobot SEN0227//SHT20
float temp_SEN, humid_SEN, tempDS;

//Vars pour le capteur Adafruit Stemma Soil Sensor  (Adafruit 4026 https://www.adafruit.com/product/4026)
//float temp_GND, humid_GND;

Adafruit_CCS811 ccs;
//Adafruit_seesaw soilSensor;
DFRobot_SHT20 sht20;
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);
//PID myPID(&currentTemp, &PIDOut, &setPoint, Kp, Ki, Kd, DIRECT);

void setup() 
{
  //pinMode(HEATCABLE, OUTPUT);
  //myPID.SetMode(AUTOMATIC);
  
  initSHT20();
  initCCS811();
  //initSoil(); //Remettre avant serial.begin apr's avoir mis dans un try except les init
  
  Serial.begin(9600);
}

void loop()
{
  if(currentTime-pastTime >= UPDATE_DELAY_MS)
  {
    //readCableTemp();
    readCCS();
    readSHT20();
    readDS18B20();
    //readSoil();
    sendTrame();
    pastTime = currentTime;
  }
  currentTime = millis();
  delay(69);
  //setPIDOutput();
}

void initCCS811()
{
  if(!ccs.begin())
  {
    Serial.println("Failed to start sensor! Please check your wiring.");
    delay(1000);
  }
  // Wait for the sensor to be ready
  while(!ccs.available());
}

void initSHT20()
{
  sht20.initSHT20();                                  // Init SHT20 Sensor
  delay(100);
  sht20.checkSHT20();                                 // Check SHT20 Sensor
}

/*void initSoil()
{
  if (!soilSensor.begin(0x36)) 
  {
    Serial.println("ERROR! seesaw not found");
    while(1);
  } 
  else 
  {
    Serial.print("seesaw started! version: ");
    Serial.println(soilSensor.getVersion());
  }
}

void readSoil()
{
  uint16_t capread = soilSensor.touchRead(0);
  temp_GND = soilSensor.getTemp();
  humid_GND = mapFloatToPercent(capread,200,2000);
}*/
/*
void readCableTemp()
{
  sensors.requestTemperatures(); // Send the command to get temperature readings 
  currentTemp = sensors.getTempCByIndex(0);
}
*/


void readDS18B20()
{
  sensors.requestTemperatures(); // Send the command to get temperature readings
  tempDS = sensors.getTempCByIndex(0);
}

void readCCS()
{
  if(ccs.available())
  {
    if(!ccs.readData())
    {
      ppm_Dioxide = ccs.geteCO2();
      ppb_TVOC = ccs.getTVOC();
    }
    else
    {
      Serial.println("ERROR!");
      delay(1000);
    }
  }
}

void readSHT20()
{
  humid_SEN = sht20.readHumidity();                  // Read Humidity
  temp_SEN = sht20.readTemperature();               // Read Temperature
}

/*void setPIDOutput()
{
  myPID.Compute();
  if(PIDOut>40)
  {
    PIDOut=100;
    state_PID = HEATING;
  }
  else if(PIDOut <= 40 && PIDOut >0)
    state_PID = MAINTAIN;
  else
    state_PID = OFF;
    
  analogWrite(HEATCABLE, map(PIDOut,0,100,0,255));
}
*/
void sendTrame()
{
  String trame = String(temp_SEN)+";"+String(humid_SEN)+";"+String(ppm_Dioxide)+";"+String(ppb_TVOC)+";"+String(tempDS);
  Serial.println(trame);
}

/*float mapFloatToPercent(float var, float inLow, float inHigh)
{
  float ret = (((var-inLow)/(inHigh-inLow))*100);
  return ret;
}*/
