import RPi.GPIO as GPIO
import time

# Set up GPIO
flame_sensor_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(flame_sensor_pin, GPIO.IN)

try:
    print("Waiting for flame sensor to be triggered...")

    # This loop will continuously check the state of the flame sensor
    while True:
        if GPIO.input(flame_sensor_pin) == GPIO.LOW:
            print("Flame detected!")
        else:
            print("No flame detected.")
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting due to keyboard interrupt")

finally:
    # Clean up GPIO
    GPIO.cleanup()
