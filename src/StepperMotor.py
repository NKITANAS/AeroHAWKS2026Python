import gpiod
import Constants
from time import sleep
from enum import Enum

class Windows(Enum):
    WINDOW1 = 1
    WINDOW2 = 2
    WINDOW3 = 3
    WINDOW4 = 4

class StepperMotor:
    # Count of steps taken
    step_count: int = 0

    # Initialize the stepper motor control pins
    def __init__(self):
        self.dir_pin  = Constants.STEPPER_MOTOR_DIR_PIN
        self.step_pin = Constants.STEPPER_MOTOR_STEP_PIN

    # One Step Forward
    def step_forward(self):
        Constants.request.set_value(self.dir_pin,  gpiod.line.Value.ACTIVE)   # Set direction to forward
        sleep(0.01)                                                           # Delay for direction change
        Constants.request.set_value(self.step_pin, gpiod.line.Value.ACTIVE)   # Step
        sleep(0.01)                                                           # Delay for step timing
        Constants.request.set_value(self.step_pin, gpiod.line.Value.INACTIVE) # Reset step pin
        step_count += 1                                                       # Increment step count
        sleep(0.01)                                                           # Delay for step timing

    # One Step Backward
    def step_backward(self):
        Constants.request.set_value(self.dir_pin,  gpiod.line.Value.ACTIVE)   # Set direction to backward
        sleep(0.01)                                                           # Delay for direction change
        Constants.request.set_value(self.step_pin, gpiod.line.Value.ACTIVE)   # Step
        sleep(0.01)                                                           # Delay for step timing
        Constants.request.set_value(self.step_pin, gpiod.line.Value.INACTIVE) # Reset step pin
        step_count -= 1                                                       # Decrement step count
        sleep(0.01)                                                           # Delay for step timing

    def step_to_windows(self, window):
        if window == Windows.WINDOW1:
            for step in range(Constants.WINDOW1_STEPS):
                self.step_forward()
        elif window == Windows.WINDOW2:
            for step in range(Constants.WINDOW2_STEPS):  
                self.step_forward()
        elif window == Windows.WINDOW3:
            for step in range(Constants.WINDOW3_STEPS):  
                self.step_forward()
        elif window == Windows.WINDOW4:
            for step in range(Constants.WINDOW4_STEPS):  
                self.step_forward()