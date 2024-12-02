import serial, time
class sendings_to_arduino:
    def __init__(self):
        self.message_time = None
        self.message_intensity = None 
        self.arduino = serial.Serial('COM12', 9600,timeout=10)

    def send_time_to_arduino(self,text_field_time):
        self.message_time = text_field_time
        confirm_pass_time = f"time was sent,{self.message_time}"
        self.arduino.write(confirm_pass_time.encode())
        print (self.arduino.readline())
        self.arduino.close

    def send_intensity_to_arduino(self,text_field_intesity):
        self.message_intensity = text_field_intesity
        confirm_pass_intensity = f"intensity was sent,{self.message_intensity}"
        self.arduino.write(confirm_pass_intensity.encode())
        print (self.arduino.readline())
        self.arduino.close




communication = sendings_to_arduino()








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

