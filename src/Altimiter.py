import gpiod
import smbus
import math

import Constants

class Altimiter:
    # MAJOR TODO: This will take the data from the pico via I2C

    def __init__(self):
        self.bus = smbus.SMBus(4)  # Use I2C bus 4
        self.address = Constants.BAROMETER_I2C_ADDRESS

    def read_pressure(self) -> float:
        # Read the pressure data from the altimiter sensor and return it as a float
        pass

    def get_height(self, reference_pressure, temperature) -> float:
        # Use the hypsometric equation to calculate the height based on the reference pressure and temperature
        # The reference pressure is the pressure at the initial height, and the temperature is the current temp in kelvin
        height = (Constants.GAS_CONSTANT * temperature) / (Constants.GRAVITY) * math.log(reference_pressure / self.read_pressure())
        return height

