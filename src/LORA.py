from LoRaRF import SX126x

class LORA:
    def __init__(self):
        try:
            # Create new LORA object
            self.Lora = SX126x()

            # Configure the self.Lora
            self.Lora.setSpi(0, 0, 7800000)
            self.Lora.begin()

            # set transmit power to +22 dBm
            self.Lora.setTxPower(22, self.Lora.TX_POWER_SX1262)
            # set receive gain to power saving(Comment first if lora dosent work)
            self.Lora.setRxGain(self.Lora.RX_GAIN_POWER_SAVING)
            # Set frequency to 915 Mhz
            self.Lora.setFrequency(915000000)
            # set spreading factor 8, bandwidth 125 kHz, coding rate 4/5, and low data rate optimization off
            self.Lora.setLoRaModulation(8, 125000, 5, False)
            # set explicit header mode, preamble length 12, payload length 15, CRC on and no invert IQ operation
            self.Lora.setLoRaPacket(self.Lora.HEADER_EXPLICIT, 12, 15, True, False)
            # Set syncronize word for public network (0x3444)
            self.Lora.setSyncWord(0x3444)
            
            # Initialize counter as instance variable
            self.counter = 0
            self.initialized = True
            print("LoRa module initialized successfully")
        except Exception as e:
            print(f"Error initializing LoRa module: {e}")
            self.Lora = None
            self.counter = 0
            self.initialized = False
    
    # Receive Function
    def receive(self) -> str:
        if not self.initialized or not self.Lora:
            print("Error: LoRa module not initialized")
            return ""
            
        try:
            self.Lora.request()
            self.Lora.wait()

            # get message and counter in last byte
            message = ""
            while self.Lora.available() > 1:
                message += chr(self.Lora.read())          # read message bytes
            counter = self.Lora.read()                    # read counter (last byte only)
            return message
        except Exception as e:
            print(f"Error receiving LoRa message: {e}")
            return ""
    
    # Transmit Function
    def transmit(self, message) -> bool:
        if not self.initialized or not self.Lora:
            print("Error: LoRa module not initialized")
            return False
            
        try:
            # message and counter to transmit
            messageList = list(message)
            for i in range(len(messageList)): 
                messageList[i] = ord(messageList[i])

            self.Lora.beginPacket()
            self.Lora.write(messageList) # write multiple bytes
            self.Lora.write(self.counter)               # write single byte
            self.Lora.endPacket()
            self.Lora.wait()
            self.counter += 1
            return True
        except Exception as e:
            print(f"Error transmitting LoRa message: {e}")
            return False

