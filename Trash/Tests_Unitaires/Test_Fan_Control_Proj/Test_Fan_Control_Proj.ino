#define FAN 9
#define POTFAN A1
#define MAXFAN 75 //Values found experimenting
#define MINFAN 3

int potRead=0;

void setup() 
{
  cli();
  TCCR2A=2;   // Mode CTC ( Clear Timer On Compare)
  TCCR2B=0x03;  // wgm22 est a 0 , CS2 a 0 CS1 a 1 CS0 a 1 donc un prescaler de 64
  OCR2A = 100;    // valeur de comparaison a 100 ( 100 interruption max )
  TIMSK2=0x02;    // Active l'interruption lorsque Compteur TCNT2 =  OCR2A ( 100 interrupts)
  TCNT2=0; // set le timer2 a 0 ( fresh start)
  sei();
  
  Serial.begin(115200);
  
  pinMode(FAN, OUTPUT);
  Serial.println("Starting in 3 seconds...");
  
  for(int i =2 ; i>0;i--)
  {
    delay(1000);
    if(i>1)
      Serial.println(String(i)+"...");
    else
      Serial.println("Fan is a go!");  
  }
}

void loop() 
{
  /*
  for(int i =0;i<20;i++)
  {
    for(int i =MINFAN;i<MAXFAN;i+=1)
    {
      delay(10000/(MAXFAN-MINFAN));
      analogWrite(FAN, i);
    }
    for(int i =MAXFAN;i>MINFAN;i-=1)
    {
      delay(10000/(MAXFAN-MINFAN));
      analogWrite(FAN, i);
    }
  }*/
  Serial.print("Raw : ");
  Serial.print(potRead);
  Serial.print(" | Mapped : ");
  Serial.println(map(potRead,0,1023,0,255));
  
  analogWrite(FAN, map(potRead,0,1023,0,255)); // sets the digital pin 13 on
  //delay(20000);            // waits for a second
  //Serial.println("Fan is stopping!");
  //analogWrite(FAN, 0);  // sets the digital pin 13 off
  //delay(100000);
  // put your main code here, to run repeatedly:

}


ISR(TIMER2_COMPA_vect)        // interruptions au 2500e de secondes 
{
  potRead = analogRead(POTFAN);
}
