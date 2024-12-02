import serial, time
arduino = serial.Serial('COM12', 9600)
time.sleep(2)
message = "toma"
arduino.write(message.encode())
print(f"Sent: {message}")
read = arduino.readline()
print (read)
arduino.close








#Example code in arduino

#const int led= 13;
#void setup() {
# // put your setup code here, to run once:
#  Serial.begin(9600);
#  pinMode(13, OUTPUT);

#}

#void loop() {
#  // put your main code here, to run repeatedly:
#  if (Serial.readString() == "toma"){
#    Serial.println("si lo agarre pp");
#    digitalWrite(13,HIGH);
#    delay(3000);
#    digitalWrite(13,LOW);
#    }

#}

