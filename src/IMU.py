import gpiod
import Constants
from mpu6050 import mpu6050

class IMU:
    def __init__(self):
        self.IMU = Constants.IMU
        # set ranges
        self.IMU.set_accel_range(mpu6050.ACCEL_RANGE_8G)
        self.IMU.set_gyro_range(mpu6050.GYRO_RANGE_500DEG)

    def get_accelerometer_data(self):
        return self.IMU.get_accel_data()
    
    def get_gyroscope_data(self):
        return self.IMU.get_gyro_data()
    
    def get_temperature_data(self):
        return self.IMU.get_temp()