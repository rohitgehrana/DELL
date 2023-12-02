import RPi.GPIO as GPIO
import time

# Set the GPIO mode and pin
pir_pin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(pir_pin, GPIO.IN)

try:
    print("Motion detection system initialized. Waiting for motion...")

    while True:
        # Read the state of the PIR sensor
        pir_state = GPIO.input(pir_pin)

        # Check if motion is detected
        if pir_state == GPIO.HIGH:
            print("MOTION DETECTED")

        # Add a small delay to avoid high CPU usage
        time.sleep(0.1)

except KeyboardInterrupt:
    # Clean up GPIO on program exit
    GPIO.cleanup()
