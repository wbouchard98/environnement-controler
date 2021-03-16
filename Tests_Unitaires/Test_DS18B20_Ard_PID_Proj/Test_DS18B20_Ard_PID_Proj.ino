#include <OneWire.h> 
#include <DallasTemperature.h>
#include <PID_v1.h>

#define HEATCABLE 3
#define ONE_WIRE_BUS 2 
#define UPDATE_DELAY_MS 1000  
unsigned long changeTime = 0; //last time the sensor was triggered

unsigned long currentTime = millis();

double driverOut = 220;
double difference = 10;
double setPoint = 10;
String inString;
int Kp = 3;
int Ki = 2;
int Kd = 1;

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);
//PID myPID(&difference, &driverOut, &setPoint,Kp,Ki,Kd, DIRECT);

void setup() 
{

  
  Serial.begin(9600);
}

void loop()
{
  if(currentTime-changeTime >= UPDATE_DELAY_MS)
  {
    sensors.requestTemperatures(); // Send the command to get temperature readings 
    Serial.print("Temperature is: "); 
    Serial.print(sensors.getTempCByIndex(0)); // Get Sensor Index 0 
    changeTime = currentTime;
  }
  currentTime = millis();
  
  /********************************************************************/

}
