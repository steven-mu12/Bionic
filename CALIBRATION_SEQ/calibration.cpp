#include <SoftwareSerial.h>

// pin definitions
#define motorOne 5
#define motorTwo 8
#define onLed 3
#define moveLed 11

string data;


void setup() {
  
  Serial.begin(9600);
  Serial.setTimeout(10);

  // set up pins
  pinMode(2, OUTPUT);
  digitalWrite(2, LOW);
  pinMode(4, OUTPUT);
  digitalWrite(4, LOW);
  pinMode(6, OUTPUT);
  digitalWrite(6, LOW);
  pinMode(9, OUTPUT);
  digitalWrite(9, LOW);
  pinMode(12, OUTPUT);
  digitalWrite(12, LOW);

  // actual pins
  pinMode(motorOne, OUTPUT);
  pinMode(motorTwo, OUTPUT);
  pinMode(onLed, OUTPUT);
  digitalWrite(onLed, HIGH);
  pinMode(moveLed, OUTPUT);
  
} 



void loop() {
  if (Serial.available() > 0){
    data = Serial.readString();
    movement();
  }
}



// ---------
// functions
// ---------

void movement() {

  // go up
  if (data == "1"){
    digitalWrite(motorOne, HIGH);
    digitalWrite(motorTwo, LOW);   
  }

  // go down
  else if (data == "-1"){
    digitalWrite(motorOne, LOW);
    digitalWrite(motorTwo, HIGH);  
  }
  // stop
  else if (data == "0"){
    digitalWrite(motorOne, LOW);
    digitalWrite(motorTwo, LOW);  
  }
  
}



