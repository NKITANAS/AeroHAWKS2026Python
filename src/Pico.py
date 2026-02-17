import Constants
import serial

# Handles communication with the Pico, which reads the sensor data as the pi dosent have analog pins
class Pico:
    def __init__(self):
        ser = serial.Serial(Constants.PICO_SERIAL_PORT, Constants.PICO_BAUD_RATE, timeout=1)

    def read_moisture(self, sensor_number: int) -> float:
        # Open serial connection to Pico
        with serial.Serial(Constants.PICO_SERIAL_PORT, Constants.PICO_BAUD_RATE, timeout=1) as ser:
            # Send sensor number to Pico
            ser.write(f"MOISTURE_{sensor_number}".encode())

            # Read moisture value from Pico
            moisture_value = ser.readline().decode().strip()

        return float(moisture_value)
    def read_altitude(self) -> float:
        # Open serial connection to Pico
        with serial.Serial(Constants.PICO_SERIAL_PORT, Constants.PICO_BAUD_RATE, timeout=1) as ser:
            # Send command to read altitude
            ser.write("ALTITUDE".encode())

            # Read altitude value from Pico
            altitude_value = ser.readline().decode().strip()

        return float(altitude_value)
    def read_temperature(self) -> float:
        # Open serial connection to Pico
        with serial.Serial(Constants.PICO_SERIAL_PORT, Constants.PICO_BAUD_RATE, timeout=1) as ser:
            # Send command to read temperature
            ser.write("TEMP".encode())

            # Read temperature value from Pico
            temperature_value = ser.readline().decode().strip()

        return float(temperature_value)
    def read_gyroscope(self) -> dict:
        # Open serial connection to Pico
        with serial.Serial(Constants.PICO_SERIAL_PORT, Constants.PICO_BAUD_RATE, timeout=1) as ser:
            # Send command to read gyroscope data
            ser.write("GYRO".encode())

            # Read gyroscope data from Pico
            gyro_data = ser.readline().decode().strip()

        # Parse the gyroscope data into a dictionary
        gyro_dict = {}
        for axis_data in gyro_data.split(","):
            axis, value = axis_data.split(":")
            gyro_dict[axis] = float(value)

        return gyro_dict
    def read_accelerometer(self) -> dict:
        # Open serial connection to Pico
        with serial.Serial(Constants.PICO_SERIAL_PORT, Constants.PICO_BAUD_RATE, timeout=1) as ser:
            # Send command to read accelerometer data
            ser.write("ACCEL".encode())

            # Read accelerometer data from Pico
            accel_data = ser.readline().decode().strip()

        # Parse the accelerometer data into a dictionary
        accel_dict = {}
        for axis_data in accel_data.split(","):
            axis, value = axis_data.split(":")
            accel_dict[axis] = float(value)

        return accel_dict   