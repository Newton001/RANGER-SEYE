#define analogTemperatureInputPin A0
#include <SoftwareSerial.h>

int temperatureRecorded;
int counterVariable = 1;
int ledAlertPin1 = 8;
int ledAlertPin2 = 7;
int ledAlertPin3 = 9;

int buzzerAlertPin = 5;//Pin that will make the buzzer buzz.

SoftwareSerial bluetooth(0x27 , 2 , 3); //Initialize the bluetooth object as Pin 2 being the TX and pin 3 Being the RX.

char bufferDelay [5];

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  bluetooth.begin(9600);
  pinMode(ledAlertPin1 , OUTPUT);  //This pin will turn to high and  light up the LEDs When the fire Breaks out.
  //pinMode(ledAlertPin1 , LOW);   //Start with our output Pin being low on the setup function.
  pinMode(ledAlertPin2 , OUTPUT);
  pinMode(ledAlertPin3 , OUTPUT);

  pinMode(buzzerAlertPin , OUTPUT);
   
//  Serial.println("Recording the values of the temperature.");
//  bluetooth.println("Temperature Values read From the Sensor.");

  delay(5000);
}

void loop() {
  // put your main code here, to run repeatedly:
  temperatureRecorded = analogRead(analogTemperatureInputPin) * 0.48828125; //Convert the value of the temperature that has been recorded.
                                                    //Store it in the variable named temperatureRecorded.
  //Send the data to the raspberry PI.
  sprintf( bufferDelay , "%2f" , temperatureRecorded );//This line of code sends the data to the Raspberry Pi through the serial communication
                                                       //The Raspberry receices the values as floats through the serial. These values can then
                                                       //be sent to the cloud or any other relevant paths.
  //Serial.println();
//  Serial.print("Attempt ");
//  Serial.print(counterVariable);
//  Serial.print(" Temperature =  ");  // Display the rate of transmission of the temperature from the sensor.

  Serial.println(temperatureRecorded);

  bluetooth.print("Temperature Value = ");
  bluetooth.println(temperatureRecorded);

  if ( temperatureRecorded >= 28 ){

    digitalWrite(ledAlertPin1 , HIGH);
    digitalWrite(ledAlertPin2 , HIGH);
    digitalWrite(ledAlertPin3 , HIGH);

    tone(buzzerAlertPin , 1000);  //This is the frequency that the buzzer will operate at. 1KHz

    blinkLEDFunction(ledAlertPin1 , ledAlertPin2 , ledAlertPin3);
    
  }
  else {
    digitalWrite(ledAlertPin1 , LOW);
    digitalWrite(ledAlertPin2 , LOW);
    digitalWrite(ledAlertPin3 , LOW);

    noTone(buzzerAlertPin);   // No other parameter for the Buzzer frequency.
  }
  
  ++counterVariable;

  delay(500);     //delay function to make the Communication smooth.
}

void blinkLEDFunction(int firstLedPin , int secondLedPin , int thirdLedPin){

    digitalWrite(firstLedPin , LOW);
    digitalWrite(secondLedPin , LOW);
    digitalWrite(thirdLedPin , LOW);

    delay(500);

    digitalWrite(firstLedPin , HIGH);
    digitalWrite(secondLedPin , HIGH);
    digitalWrite(thirdLedPin, HIGH);
}
