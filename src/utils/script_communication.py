import serial, time
from src.utils.verificaiton import verify



#Consideraciones: debe programar un detector automatico de puerto com o del puerto en linux (si usa linux el puerto se escribe diferente)
#También el programa no inicia al menos que detecte el arduino por lo tanto si desea hacer pruebas sin arduino debe desactivar esta página
class sendings_to_arduino:
    def __init__(self):
        self.message_time = None
        self.message_intensity = None 
        self.level_1 = None
        self.level_2 = None
        self.level_3 = None
        self.command_restart = None
        self.start_test = None
        self.stop_test = None
        self.finish_test_to_go_out_glitch = None
        self.warning_comunication_lost = None
        try:
         self.arduino = serial.Serial(verify.detectar_arduino(), 9600,timeout=5)
        except serial.SerialTimeoutException:
            print("Se produjo un timeout en la comunicación serial.")
            self.warning_comunication_lost.value = "Reinicia el dispositivo"
            self.restart_arduino("Restart arduino")

    def send_time_to_arduino(self,text_field_time,warning_comunication_lost):
        self.warning_comunication_lost = warning_comunication_lost
        try:
            self.message_time = text_field_time
            confirm_pass_time = f"time was sent,{self.message_time}"
            self.arduino.write(confirm_pass_time.encode())
            printing = self.arduino.readline()
            print(printing)
            self.arduino.close
            if (printing == b''):
                print("Se produjo un timeout en la comunicación serial.")
                warning_comunication_lost.value = "Reinicia el dispositivo"
                self.restart_arduino("Restart arduino")
        except :
            print("more slow")

    def send_intensity_to_arduino(self,text_field_intesity,warning_comunication_lost):
        try:
            self.message_intensity = str(8300*((60*int(text_field_intesity))/10000))
            confirm_pass_intensity = f"intensity was sent,{self.message_intensity}"
            self.arduino.write(confirm_pass_intensity.encode())
            printing = self.arduino.readline()
            self.arduino.close
            print(printing)
            if (printing == b''):
                print("Se produjo un timeout en la comunicación serial.")
                warning_comunication_lost.value = "Reinicia el dispositivo"
                self.restart_arduino("Restart arduino")
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

    def Stop_test(self,stop_test,warning_comunication_lost):
        try:
            self.stop_test = stop_test
            confirm_pass_stop_test = f"{self.stop_test},0"
            self.arduino.write(confirm_pass_stop_test.encode())
            printing = self.arduino.readline()
            printing_2 = self.arduino.readline()
            self.arduino.close
            print(printing)
            print(printing_2)
            if (printing == b'') or (printing_2 == b''):
                print("Se produjo un timeout en la comunicación serial.")
                warning_comunication_lost.value = "Reinicia el dispositivo"
                self.restart_arduino("Restart arduino")
        except serial.SerialTimeoutException:
            print("Se produjo un timeout en la comunicación serial(rare case).")




communication = sendings_to_arduino()


