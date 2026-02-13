import gpiod
from mpu6050 import mpu6050

# Test Mode #
TEST_MODE: bool = True

gpiochip: gpiod.Chip = gpiod.Chip('/dev/gpiochip0')

# Math Constants #

GRAVITY: float = 9.80665          # m/s^2
GAS_CONSTANT: float = 8.314462618 # J/(mol*K)

# Pin/Line definitions #
### NOTE: DONT USE 8 AND 9

# Linear Actuators - numbers are subject to change
LINEAR_ACTUATOR_L_PIN_1: int = 6
LINEAR_ACTUATOR_L_PIN_2: int = 13
LINEAR_ACTUATOR_R_PIN_1: int = 19
LINEAR_ACTUATOR_R_PIN_2: int = 26

# Stepper Motor - numbers are subject to change
STEPPER_MOTOR_DIR_PIN:   int = 23
STEPPER_MOTOR_STEP_PIN:  int = 24

# Altimiter(Barometer) - numbers are subject to change
BAROMETER_I2C_ADDRESS:          int = 0x76
BAROMETER_i2C_OUTPUT_DATA_RATE: int = 0xF4

# IMU - numbers are subject to change
IMU: mpu6050 = mpu6050(0x68)

# Stepper Motor Windows positions #
DEGREE_TO_STEP: float = 200 / 360 # 200 steps per revolution, 360 degrees per revolution

WINDOW1_STEPS: float  = 0   * DEGREE_TO_STEP  
WINDOW2_STEPS: float  = 90  * DEGREE_TO_STEP  
WINDOW3_STEPS: float  = 0   * DEGREE_TO_STEP  
WINDOW4_STEPS: float  = 90  * DEGREE_TO_STEP  

default_settings: gpiod.LineSettings = gpiod.line_settings.LineSettings(
    direction=gpiod.line.Direction.OUTPUT
    )
input_settings: gpiod.LineSettings = gpiod.line_settings.LineSettings(
    direction=gpiod.line.Direction.INPUT
    )

request: gpiod.LineRequest = gpiochip.request_lines(
    consumer="payload",
    config={
        LINEAR_ACTUATOR_L_PIN_1: default_settings,
        LINEAR_ACTUATOR_L_PIN_2: default_settings,
        LINEAR_ACTUATOR_R_PIN_1: default_settings,
        LINEAR_ACTUATOR_R_PIN_2: default_settings,
        STEPPER_MOTOR_DIR_PIN:   default_settings,
        STEPPER_MOTOR_STEP_PIN:  default_settings,
    },
)