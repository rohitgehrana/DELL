import RPi.GPIO as GPIO
import time

# Set up GPIO
sensor_pin = 17  # Change this to the GPIO pin where your sensor is connected
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)

try:
    while True:
        if GPIO.input(sensor_pin) == GPIO.HIGH:
            print("Motion detected!")
        else:
            print("No motion detected.")
        
        time.sleep(1)  # Adjust the delay as needed

except KeyboardInterrupt:
    print("Program terminated by user.")
finally:
    GPIO.cleanup()
