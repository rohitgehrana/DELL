import RPi.GPIO as GPIO
import time

# Set the GPIO mode and pin
sensor_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)

try:
    while True:
        # Read the state of the sensor
        sensor_state = GPIO.input(sensor_pin)

        # Check if the sensor is detected (modify this condition based on your sensor)
        if sensor_state == GPIO.HIGH:
            print("SENSOR DETECTED")

        # Add a small delay to avoid high CPU usage
        time.sleep(0.1)

except KeyboardInterrupt:
    # Clean up GPIO on program exit
    GPIO.cleanup()

