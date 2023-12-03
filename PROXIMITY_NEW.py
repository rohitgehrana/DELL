import RPi.GPIO as GPIO
import time

# Pin configuration
pir_sensor_pin = 17  # Change this to the actual GPIO pin number where you have connected the PIR sensor

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pir_sensor_pin, GPIO.IN)  # Set PIR sensor pin as INPUT

def loop():
    try:
        while True:
            motion_status = GPIO.input(pir_sensor_pin)  # Read the digital signal from the PIR sensor

            if motion_status == GPIO.HIGH:
                print("Motion Detected!")
            else:
                print("No Motion Detected")

            time.sleep(1)  # Delay for a short time to avoid rapid prints

    except KeyboardInterrupt:
        GPIO.cleanup()  # Clean up GPIO on Ctrl+C exit

if __name__ == "__main__":
    setup()
    loop()
