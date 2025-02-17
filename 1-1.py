import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
for i in range(3):
    GPIO.output(16, 1)
    time.sleep(1)
    GPIO.output(16, 0)
    time.sleep(1)
    i += 1