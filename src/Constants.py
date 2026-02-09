import gpiod

gpiochip = gpiod.Chip('gpiochip0')

# Pin/Line definitions #

# Linear Actuators - numbers are subject to change
LINEAR_ACTUATOR_L_PIN_1 = gpiochip.get_line(1)
LINEAR_ACTUATOR_L_PIN_2 = gpiochip.get_line(2)
LINEAR_ACTUATOR_R_PIN_1 = gpiochip.get_line(3)
LINEAR_ACTUATOR_R_PIN_2 = gpiochip.get_line(4)

# Stepper Motor - numbers are subject to change
STEPPER_MOTOR_PIN_1 = gpiochip.get_line(5)
STEPPER_MOTOR_PIN_2 = gpiochip.get_line(6)
STEPPER_MOTOR_PIN_3 = gpiochip.get_line(7)
STEPPER_MOTOR_PIN_4 = gpiochip.get_line(8)

# IMU - numbers are subject to change
IMU_SDA_PIN = gpiochip.get_line(9)
IMU_SCL_PIN = gpiochip.get_line(10)
IMU_INT_PIN = gpiochip.get_line(11)
IMU_XDA_PIN = gpiochip.get_line(12)
IMU_XCL_PIN = gpiochip.get_line(13)
IMU_ADO_PIN = gpiochip.get_line(14)