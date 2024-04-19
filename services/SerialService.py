import serial


class SerialService:
    def __init__(self, port='/dev/ttyUSB0', baudrate=9600):
        self.port = port
        self.baudrate = baudrate
        self.serial = None

    def open_serial_connection(self):
        try:
            self.serial = serial.Serial(self.port, self.baudrate)
            print(f"Serial connection opened on port {self.port}")
        except serial.SerialException as e:
            print(f"Error opening serial connection: {e}")


