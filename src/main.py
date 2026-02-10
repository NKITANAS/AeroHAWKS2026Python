import gpiod
from time import sleep

import Constants
import IMU
import LinearActuators
import LORA
import StepperMotor

def main():
    # Create a new GPIO chip object for the specified chip name
    chip = gpiod.Chip('gpiochip0')

    # Request a line for output and set its initial value to 0 (low)
    line = chip.get_line(17)
    line.request(consumer='my-consumer', type=gpiod.LINE_REQ_DIR_OUT, default_vals=[0])

    # Set the line value to 1 (high)
    line.set_value(1)

main()