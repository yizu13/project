import serial, time
class sendings_to_arduino:
    def __init__(self):
        self.message_time = None
        self.message_intensity = None 
        self.level_1 = None
        self.level_2 = None
        self.level_3 = None
        self.command_restart = None
        self.arduino = serial.Serial('COM12', 9600,timeout=10)

    def send_time_to_arduino(self,text_field_time):
        try:
            self.message_time = text_field_time
            confirm_pass_time = f"time was sent,{self.message_time}"
            self.arduino.write(confirm_pass_time.encode())
            print (self.arduino.readline())
            self.arduino.close
        except:
            print("more slow")

    def send_intensity_to_arduino(self,text_field_intesity):
        try:
            self.message_intensity = text_field_intesity
            confirm_pass_intensity = f"intensity was sent,{self.message_intensity}"
            self.arduino.write(confirm_pass_intensity.encode())
            print (self.arduino.readline())
            self.arduino.close
        except:
            print("more slow")
    
    def turn_off_level_1(self,level_1):
        self.level_1 = level_1
        confirm_pass_turn_off_level_1 = f"{self.level_1},1"
        self.arduino.write(confirm_pass_turn_off_level_1.encode())
        self.arduino.close

    def turn_on_level_1(self,level_1):
        self.level_1 = level_1
        confirm_pass_turn_on_level_1 = f"{self.level_1},1"
        self.arduino.write(confirm_pass_turn_on_level_1.encode())
        self.arduino.close



    def turn_off_level_2(self,level_2):
        self.level_2 = level_2
        confirm_pass_turn_off_level_2 = f"{self.level_2},2"
        self.arduino.write(confirm_pass_turn_off_level_2.encode())
        self.arduino.close

    def turn_on_level_2(self,level_2):
        self.level_2 = level_2
        confirm_pass_turn_on_level_2 = f"{self.level_2},2"
        self.arduino.write(confirm_pass_turn_on_level_2.encode())
        self.arduino.close



    def turn_off_level_3(self,level_3):
        self.level_3 = level_3
        confirm_pass_turn_off_level_3 = f"{self.level_3},3"
        self.arduino.write(confirm_pass_turn_off_level_3.encode())
        self.arduino.close

    def turn_on_level_3(self,level_3):
        self.level_3 = level_3
        confirm_pass_turn_on_level_3 = f"{self.level_3},3"
        self.arduino.write(confirm_pass_turn_on_level_3.encode())
        self.arduino.close

    def restart_arduino(self,command):
        self.command_restart = command
        confirm_pass_restart = f"{self.command_restart},4"
        self.arduino.write(confirm_pass_restart.encode())
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

