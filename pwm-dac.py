import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
p = GPIO.PWM(20, 50)
p.start(0)
try:
    while True:
        duty_cycle = int(input())
        p.ChangeDutyCycle(duty_cycle)
        voltage = 3.3 * duty_cycle/100
        print(voltage)
finally:
    p.stop()
    GPIO.cleanup()