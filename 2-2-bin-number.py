import RPi.GPIO as GPIO
import time
# import random

dac = [8, 11, 7, 1, 0, 5, 12, 6]
number = [0] * len(dac)
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

# number = [random.randint(0, 1) for i in range(8)]
number = [1, 1, 0, 1, 1, 1, 0, 0]
GPIO.output(dac, number)
# print(number)
time.sleep(15)
GPIO.output(dac, 0)
GPIO.cleanup()