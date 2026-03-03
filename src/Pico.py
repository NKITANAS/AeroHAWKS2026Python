import Constants
import serial

# Handles communication with the Pico, which reads the sensor data as the pi dosent have analog pins
class Pico:
    def __init__(self):
        try:
            self.ser = serial.Serial(Constants.PICO_SERIAL_PORT, Constants.PICO_BAUD_RATE, timeout=1)
            self.connected = True
        except serial.SerialException as e:
            print(f"Error opening serial port: {e}")
            self.ser = None
            self.connected = False 
        
    def read_data(self):
        if self.connected and self.ser.in_waiting > 0:
            line = self.ser.readline().decode('utf-8').rstrip()
            return line