String myCmd;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  while(Serial.available() == 0){
  }
  myCmd = Serial.readStringUntil('\r');
  if(myCmd == "1"){
    tone(3, 100, 2000);
      
    
    
  }
  if(myCmd == "0"){
    noTone(3);
  }
}
