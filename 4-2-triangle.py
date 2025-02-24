import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)

def dec2bin(num):
    bi = bin(num)[2:].zfill(8)
    result = list(map(int, bi))
    return result
    
try:
    tim = int(input())
    while True:
        for value in range(255):
            GPIO.output(dac, dec2bin(value))
            time.sleep(tim/510)
        for value in range(255, -1, -1):
            GPIO.output(dac, dec2bin(value))
            time.sleep(tim/510)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()