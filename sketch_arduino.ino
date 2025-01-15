int led_pin = 3;

void setup() { 

  Serial.begin(9600);
  pinMode(led_pin, OUTPUT);
  
  }

void loop() {

  String text = Serial.readString();

  if (text == String("sign")){
    digitalWrite(led_pin, HIGH); delay(2000);
    } 

  else if (text == String("none")){
    digitalWrite(led_pin, LOW); delay(2000);
    }
}
