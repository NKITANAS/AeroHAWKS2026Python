import gpiod
import mpu6050
from time import sleep
import datetime

import Constants
import LORA
import Pico
import tests

from enum import Enum

# Instantiate the classes
pico            = Pico.Pico()
lora            = LORA.LORA()

class Status(Enum):
    IDLE = 1
    ASCENT = 2
    DESCENT = 3
    LANDED = 4


def main():
    turn_on_signal_received: bool = False
    # Wait for the "Turn On" signal from the ground station before starting the main loop
    while not turn_on_signal_received:
        message = lora.recieve()
        if message == "100:1":
            turn_on_signal_received = True
            print("STATUS: Turn On Recieved")
    # Init
    start_time          = datetime.datetime.now()

    # Main loop
    while True:
        # Read data from the Pico
        pico_data = pico.read_data()
        if pico_data:
            print(f"STATUS: Received data from Pico: {pico_data}")
            lora.transmit(pico_data)
        
        # Sleep for a short period to avoid overwhelming the CPU
        sleep(0.1)


if not Constants.TEST_MODE:
    main()
else:
    pass
