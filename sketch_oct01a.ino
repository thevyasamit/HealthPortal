int potPin = 0;

void setup(){
  Serial.begin(9600);     
}

void loop(){
  delay(2000);
  int val;
  int data;
  val = analogRead(0);
  float mv = ( val/1024.0)*5000;
  data = mv/10;
  //Serial.print("Temperature: ");
  String st= String("Temperature: ") +((data * (9/5))+ 32)+ String("F");
  //Serial.println("F");
//  Serial.print("Temperature: ");
//  Serial.print(data);
  Serial.println(st);
  delay(2000);

  int LED13 = 13;   //  The on-board Arduion LED

int Signal;                // holds the incoming raw data. Signal value can range from 0-1024
int Threshold = 550;            // Determine which Signal to "count as a beat", and which to ingore.
pinMode(LED13,OUTPUT);

  Signal = analogRead(1);  // Read the PulseSensor's value.
                                              // Assign this value to the "Signal" variable.
   Serial.print("Oxygen Level is:");
   Serial.println(Signal);                    // Send the Signal value to Serial Plotter.


   if(Signal > Threshold){                          // If the signal is above "550", then "turn-on" Arduino's on-Board LED.
     digitalWrite(LED13,HIGH);
   } else {
     digitalWrite(LED13,LOW);                //  Else, the sigal must be below "550", so "turn-off" this LED.
   }


delay(1000);

  
}



//
//void pulseFunc(){
//
//int PulseSensorPurplePin = analogRead(1);        // Pulse Sensor PURPLE WIRE connected to ANALOG PIN 0
//int LED13 = 13;   //  The on-board Arduion LED
//
//int Signal;                // holds the incoming raw data. Signal value can range from 0-1024
//int Threshold = 550;            // Determine which Signal to "count as a beat", and which to ingore.
//pinMode(LED13,OUTPUT);

// The SetUp Function:
//void setup() {
//      // pin that will blink to your heartbeat!
//   Serial.begin(9600);         // Set's up Serial Communication at certain speed.
//
//}

//// The Main Loop Function
//loop(); {
//
//  Signal = analogRead(1);  // Read the PulseSensor's value.
//                                              // Assign this value to the "Signal" variable.
//   Serial.print("Oxygen level:");
//   Serial.println(Signal);                    // Send the Signal value to Serial Plotter.
//
//
//   if(Signal > Threshold){                          // If the signal is above "550", then "turn-on" Arduino's on-Board LED.
//     digitalWrite(LED13,HIGH);
//   } else {
//     digitalWrite(LED13,LOW);                //  Else, the sigal must be below "550", so "turn-off" this LED.
//   }
//
//
//delay(1000);

//
//}
//}
