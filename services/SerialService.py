import serial
import json


class SerialService:
    def __init__(self, port='COM4', baudrate=9600):
        self.port = port
        self.baudrate = baudrate
        self.serial = None

    def open_serial_connection(self):
        try:
            self.serial = serial.Serial(self.port, self.baudrate)
            print(f"Serial connection opened on port {self.port}")
            print(f"To check which port is actually used: {self.serial.name}")
        except serial.SerialException as e:
            print(f"Error opening serial connection: {e}")

    def send_command(self, data):
        if self.serial:
            self.serial.write(data.encode('utf-8'))

    def read_status(self):
        if self.serial:
            x = self.serial.readline()
            print(f"Recieved data:", x)


    def close_serial_connection(self):
        if self.serial and self.serial.is_open:
            self.serial.close()
            print("Serial connection closed")
