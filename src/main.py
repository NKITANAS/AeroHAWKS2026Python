from time import sleep, monotonic
import LORA

lora = LORA.LORA()

PING_INTERVAL = 5  # seconds

def main():
    print("--- LoRa RX + PING every 5s (Press Ctrl+C to stop) ---")
    last_ping = monotonic()

    while True:
        try:
            incoming = lora.check_for_message()

            if incoming:
                print(f"RX: {incoming}")

            if monotonic() - last_ping >= PING_INTERVAL:
                print("TX: PING")
                lora.transmit("PING")
                last_ping = monotonic()

            sleep(0.01)

        except KeyboardInterrupt:
            print("\nSTATUS: Shutting down gracefully...")
            break
        except Exception as e:
            print(f"ERROR: {e}")
            sleep(1)

if __name__ == "__main__":
    main()