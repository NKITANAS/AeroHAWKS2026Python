from time import sleep
import LORA

lora = LORA.LORA()

def main():
    print("--- LoRa RX Only (Press Ctrl+C to stop) ---")

    while True:
        try:
            incoming = lora.check_for_message()

            if incoming:
                print(f"RX: {incoming}")

            sleep(0.01)

        except KeyboardInterrupt:
            print("\nSTATUS: Shutting down gracefully...")
            break
        except Exception as e:
            print(f"ERROR: {e}")
            sleep(1)

if __name__ == "__main__":
    main()