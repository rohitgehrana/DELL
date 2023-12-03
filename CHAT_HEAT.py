import RPi.GPIO as GPIO
import time

# Set up GPIO
sensor_pin = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor_pin, GPIO.IN)

try:
    while True:
        flame_detected = GPIO.input(sensor_pin)
        if flame_detected:
            print("Flame detected!")
        else:
            print("No flame detected.")
        time.sleep(1)

except KeyboardInterrupt:
    print("Program terminated by user.")
    GPIO.cleanup()
