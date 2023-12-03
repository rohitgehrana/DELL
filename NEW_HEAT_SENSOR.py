mport board
import digitalio
import time

# Define the pins for the flame sensor and water pump
flame_sensor_pin = board.GP3
water_pump_pin = board.GP8

# Initialize the flame sensor pin as an input
flame_sensor = digitalio.DigitalInOut(flame_sensor_pin)
flame_sensor.direction = digitalio.Direction.INPUT
