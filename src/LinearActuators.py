import gpiod
import Constants

class LinearActuators:
    def __init__(self):
        # Initialize the linear actuator control pins
        self.left_actuator_pin_1  = Constants.LINEAR_ACTUATOR_L_PIN_1
        self.left_actuator_pin_2  = Constants.LINEAR_ACTUATOR_L_PIN_2
        self.right_actuator_pin_1 = Constants.LINEAR_ACTUATOR_R_PIN_1
        self.right_actuator_pin_2 = Constants.LINEAR_ACTUATOR_R_PIN_2


    # The Linear Actuators are controlled with an H-Bridge Motor Controller(DRV 8833)
    # You can look up the datasheet, but basically:
    # pin1 HIGH + pin2 LOW  = Forward
    # pin1 LOW  + pin2 HIGH = Backward
    # pin1 LOW  + pin2 LOW  = Stop
    # pin1 HIGH + pin2 HIGH = Stop
    def extend_left_actuator(self):
        Constants.request.set_value(self.left_actuator_pin_1,  gpiod.line.Value.ACTIVE)
        Constants.request.set_value(self.left_actuator_pin_2,  gpiod.line.Value.INACTIVE)

    def retract_left_actuator(self):
        Constants.request.set_value(self.left_actuator_pin_1,  gpiod.line.Value.INACTIVE)
        Constants.request.set_value(self.left_actuator_pin_2,  gpiod.line.Value.ACTIVE)

    def extend_right_actuator(self):
        Constants.request.set_value(self.right_actuator_pin_1, gpiod.line.Value.ACTIVE)
        Constants.request.set_value(self.right_actuator_pin_2, gpiod.line.Value.INACTIVE)
    def retract_right_actuator(self):
        Constants.request.set_value(self.right_actuator_pin_1, gpiod.line.Value.INACTIVE)
        Constants.request.set_value(self.right_actuator_pin_2, gpiod.line.Value.ACTIVE)

    def reset_actuators(self):
        Constants.request.set_value(self.left_actuator_pin_1,  gpiod.line.Value.INACTIVE)
        Constants.request.set_value(self.left_actuator_pin_2,  gpiod.line.Value.INACTIVE)
        Constants.request.set_value(self.right_actuator_pin_1, gpiod.line.Value.INACTIVE)
        Constants.request.set_value(self.right_actuator_pin_2, gpiod.line.Value.INACTIVE)