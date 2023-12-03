import RPi.GPIO as GPIO
import time

# GPIO pins for flame sensor and infrared sensor
FLAME_SENSOR_PIN = 18  # You can change this to the actual GPIO pin you are using for the flame sensor
IR_SENSOR_PIN = 18     # You can change this to the actual GPIO pin you are using for the IR sensor

# GPIO pin for the pump (replace with your actual pump pin)
PUMP_PIN = 23

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(FLAME_SENSOR_PIN, GPIO.IN)
    GPIO.setup(IR_SENSOR_PIN, GPIO.IN)
    GPIO.setup(PUMP_PIN, GPIO.OUT)
    GPIO.output(PUMP_PIN, GPIO.LOW)  # Initialize pump to OFF

def detect_flame():
    return GPIO.input(FLAME_SENSOR_PIN)

def measure_distance():
    # Add code here to measure distance using the infrared sensor
    # You can use a library like RPi.GPIO or smbus to interface with the sensor
    # Replace the following line with your distance measurement code
    return 0  # Replace this with the actual distance value

def control_pump():
    # Add your pump control code here
    # For example, turn on the pump when a flame is detected and the distance is within a certain range
    flame_detected = detect_flame()
    distance = measure_distance()

    if flame_detected and distance < 50:  # Replace 50 with your desired distance threshold
        GPIO.output(PUMP_PIN, GPIO.HIGH)
        print("Pump is ON")
    else:
        GPIO.output(PUMP_PIN, GPIO.LOW)
        print("Pump is OFF")

def cleanup():
    GPIO.cleanup()

if __name__ == "__main__":
    try:
        setup()
        while True:
            control_pump()
            time.sleep(1)  # Adjust the sleep time as needed
    except KeyboardInterrupt:
        cleanup()
