import RPi.GPIO as GPIO
import time

# Set up GPIO with a pull-down resistor
flame_sensor_pin = 40
GPIO.setmode(GPIO.BCM)
GPIO.setup(flame_sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    print("Waiting for flame sensor to be triggered...")

    # This loop will continuously check the state of the flame sensor
    while True:
        if GPIO.input(flame_sensor_pin) == GPIO.HIGH:
            print("Flame detected!")
        else:
            print("No flame detected.")
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting due to keyboard interrupt")

finally:
    # Clean up GPIO
    GPIO.cleanup()
