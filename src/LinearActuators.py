import gpiod
import Constants

class LinearActuators:
    def __init__(self, left_actuator_pin_1, left_actuator_pin_2, right_actuator_pin_1, right_actuator_pin_2):
        self.left_actuator_pin_1 = left_actuator_pin_1
        self.left_actuator_pin_2 = left_actuator_pin_2
        self.right_actuator_pin_1 = right_actuator_pin_1
        self.right_actuator_pin_2 = right_actuator_pin_2

        self.left_actuator_pin_1.request(consumer='linear-actuators', type=gpiod.LINE_REQ_DIR_OUT, default_vals=[0])
        self.left_actuator_pin_2.request(consumer='linear-actuators', type=gpiod.LINE_REQ_DIR_OUT, default_vals=[0])
        self.right_actuator_pin_1.request(consumer='linear-actuators', type=gpiod.LINE_REQ_DIR_OUT, default_vals=[0])
        self.right_actuator_pin_2.request(consumer='linear-actuators', type=gpiod.LINE_REQ_DIR_OUT, default_vals=[0])

    def extend_left_actuator(self):
        self.left_actuator_pin_1.set_value(1)
        self.left_actuator_pin_2.set_value(0)
    def retract_left_actuator(self):
        self.left_actuator_pin_1.set_value(0)
        self.left_actuator_pin_2.set_value(1)
    def extend_right_actuator(self):
        self.right_actuator_pin_1.set_value(1)
        self.right_actuator_pin_2.set_value(0)
    def retract_right_actuator(self):
        self.right_actuator_pin_1.set_value(0)
        self.right_actuator_pin_2.set_value(1)
    def reset_actuators(self):
        self.left_actuator_pin_1.set_value(0)
        self.left_actuator_pin_2.set_value(0)
        self.right_actuator_pin_1.set_value(0)
        self.right_actuator_pin_2.set_value(0)