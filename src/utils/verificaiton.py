import serial.tools.list_ports

class verify_conections:
    def __init__(self):
        self.arduino_puerto = None
        self.puertos = None
        self.puerto_arduino =None
        
    def detectar_arduino(self):
        # Check all COM ports
        self.puertos = serial.tools.list_ports.comports()

        # Look for a port related with an arduino
        for puerto in self.puertos:
            # Set according to arduino description
            if "Arduino" in puerto.description or "CH340" in puerto.description:
                self.arduino_puerto = puerto.device
                break

        if self.arduino_puerto:
            print(f"Arduino detectado en: {self.arduino_puerto}")
            return self.arduino_puerto
        else:
            print("No se detectó un Arduino conectado.")
            return None
        
    def calling_def(self):
        # Call fuction to detect the arduino
        self.puerto_arduino = self.detectar_arduino()

        # If the arduino is detect, stablish a communication
        if self.puerto_arduino:
            try:
                print("Conexión establecida.")
                # Here is a little commnication
            except Exception as e:
                print(f"Error al conectar con el Arduino: {e}")
                
            

verify = verify_conections()