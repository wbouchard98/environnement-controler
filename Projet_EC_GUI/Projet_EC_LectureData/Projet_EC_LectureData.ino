#include <OneWire.h> 
#include <Wire.h>
#include <DallasTemperature.h>
#include <Adafruit_CCS811.h>
#include <DFRobot_SHT20.h>


#define ONE_WIRE_BUS 2 
#define UPDATE_DELAY_MS 1000

void readCCS(int &ppm_Dioxide, int &ppb_TVOC);
void readSHT20(float &humid_SEN, float &temp_SEN);
void initCCS811();
void initSHT20();
float readDS18B20();
void calculChecksum(String bytes[],int int_Bytes[]);

unsigned long pastTime = 0; //last time the sensor was triggered
unsigned long currentTime = millis();

Adafruit_CCS811 ccs;
DFRobot_SHT20 sht20;
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

enum Byte_names
{
  SOH=0,
  temp_SEN_MSB,
  temp_SEN_LSB,
  humid_SEN_MSB,
  humid_SEN_LSB,
  ppm_Dioxide_MSB,
  ppm_Dioxide_LSB,
  ppb_TVOC_MSB,
  ppb_TVOC_LSB,
  temp_DS_MSB,
  temp_DS_LSB,
  checksum,
  maxBytes
};

void setup() 
{
  initSHT20();
  initCCS811();
  Serial.begin(9600);
}

void loop()
{
  int ppb_TVOC=0,ppm_Dioxide=0; //Variables pour le CCS811 (capteur de gaz)
  float temp_SEN=-1,humid_SEN=-1,temp_DS=-1;//Vars pour le capteur SHT20(thermometre et hygrometre) et le DS18B20 (Thermometre)
  
  if(currentTime-pastTime >= UPDATE_DELAY_MS)
  {
    readCCS(ppm_Dioxide,ppb_TVOC);
    readSHT20(temp_SEN,humid_SEN);
    temp_DS = readDS18B20();
    sendTrame(temp_SEN,humid_SEN,ppm_Dioxide,ppb_TVOC,temp_DS);
    pastTime = currentTime;
  }
  currentTime = millis();
  delay(50);
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


float readDS18B20()
{
  sensors.requestTemperatures(); // Send the command to get temperature readings
  return sensors.getTempCByIndex(0);
}

void readCCS(int &ppm_Dioxide, int &ppb_TVOC)
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
      //Serial.println("ERROR!");
    }
  }
}

void readSHT20(float &temp_SEN, float &humid_SEN)
{
  humid_SEN = sht20.readHumidity();                  // Read Humidity
  temp_SEN = sht20.readTemperature();               // Read Temperature
}

void calculChecksum(String bytes[],int int_Bytes[])
{
  byte calc_ChkSum=0;
  for(int i =1; i< maxBytes-1;i++)
  {
    calc_ChkSum += bytes[i].toInt();
    int_Bytes[i]=bytes[i].toInt();
  }
  int_Bytes[checksum]= calc_ChkSum;
}

void sendTrame(float temp_SEN, float humid_SEN, int ppm_Dioxide, int ppb_TVOC, float temp_DS)
{
  String bytes[maxBytes];
  int int_Bytes[maxBytes];
  String trame;
  int_Bytes[SOH]=1;
  bytes[temp_SEN_MSB] = String(temp_SEN).substring(0,String(temp_SEN).indexOf("."));
  bytes[temp_SEN_LSB] = String(temp_SEN).substring(String(temp_SEN).indexOf(".")+1,String(temp_SEN).length());
  bytes[humid_SEN_MSB] = String(humid_SEN).substring(0,String(humid_SEN).indexOf("."));
  bytes[humid_SEN_LSB] = String(humid_SEN).substring(String(humid_SEN).indexOf(".")+1,String(humid_SEN).length());
  bytes[ppm_Dioxide_MSB] = String(ppm_Dioxide/256);
  bytes[ppm_Dioxide_LSB] = String(ppm_Dioxide%256);
  bytes[ppb_TVOC_MSB] = String(ppb_TVOC/256);
  bytes[ppb_TVOC_LSB] = String(ppb_TVOC%256);
  bytes[temp_DS_MSB] = String(temp_DS).substring(0,String(temp_DS).indexOf("."));
  bytes[temp_DS_LSB] = String(temp_DS).substring(String(temp_DS).indexOf(".")+1,String(temp_DS).length());
  calculChecksum(bytes,int_Bytes);
  
  trame= "";
  for(int i =0;i<maxBytes;i++)
  {
    trame+=String(int_Bytes[i],HEX)+" ";
  }
  
  Serial.println(trame);
}
