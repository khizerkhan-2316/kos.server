import serial
import time
import threading


class SerialService:
    def __init__(self, port='COM3', baudrate=9600, timeout=15):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial = None
        self.lock = threading.Lock()

    def open_serial_connection(self):
        try:
            self.serial = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                bytesize=serial.EIGHTBITS,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                timeout=self.timeout
            )
            print(f"Serial connection opened on port {self.port}")
            print(f"To check which port is actually used: {self.serial.name}")
            time.sleep(1)


        except serial.SerialException as e:
            print(f"Error opening serial connection: {e}")

    def send_and_read_command(self, command):
        with self.lock:  # Ensure only one operation at a time
            if self.serial:
                try:
                    # Send command
                    self.serial.write(command.encode('utf-8'))
                    print(f"Command sent: {command}")

                    # Immediately read response
                    echoed_data = self.serial.readline().decode('utf-8').strip()
                    print("\nReceived data:", echoed_data, "\n")
                    return echoed_data

                except serial.SerialTimeoutException:
                    print("Serial communication timed out.")
                except Exception as e:
                    print(f"Error during serial operation: {e}")

    def close_serial_connection(self):
        if self.serial and self.serial.is_open:
            self.serial.close()
            print("Serial connection closed.")
