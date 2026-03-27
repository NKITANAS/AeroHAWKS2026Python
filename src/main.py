from time import sleep
import datetime

import Constants
import LORA
import Pico

from enum import Enum

# Instantiate the classes
pico            = Pico.Pico()
lora            = LORA.LORA()
try:
    logfile = open(Constants.LOG_FILE_PATH, 'a')  # Open log file in append mode
except IOError as e:
    print(f"Error opening log file: {e}")
    logfile = None

class Status(Enum):
    IDLE = 1
    ASCENT = 2
    DESCENT = 3
    LANDED = 4


def main():
    turn_on_signal_received: bool = False
    # Wait for the "Turn On" signal from the ground station before starting the main loop
    #while not turn_on_signal_received:
    #    message = lora.receive()
    #    if message == "100:1":
    #        turn_on_signal_received = True
    #        print("STATUS: Turn On Received")
    # Init
    start_time = datetime.datetime.now()

    # Main loop
    while True:
        try:
            # Read data from the Pico
            pico_data = pico.read_data()
            if pico_data:
                print(f"STATUS: Received data from Pico: {pico_data}")
                success = lora.transmit(pico_data)
                if success:
                    print(f"STATUS: Successfully transmitted data")
                if logfile:
                    logfile.write(f"{datetime.datetime.now()}: {pico_data}\n")  # Log the data with a timestamp
                    logfile.flush()  # Ensure data is written to the file immediately
            
            # Sleep for a short period to avoid overwhelming the CPU
            sleep(0.1)
            
        except KeyboardInterrupt:
            print("\nSTATUS: Shutting down gracefully...")
            if logfile:
                logfile.close()
            pico.close()
            break
        except Exception as e:
            print(f"ERROR: Unexpected error in main loop: {e}")
            sleep(1)  # Wait a bit longer on errors


if not Constants.TEST_MODE:
    main()
else:
    pass
