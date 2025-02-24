import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)

def dec2bin(num):
    bi = bin(num)[2:].zfill(8)
    result = list(map(int, bi))
    return result

try:
    while True:
        number = int(input('Введите число от 0 до 255:'))

        if number == 'q':
            break
        if number < 0 or number > 255:
            print('Число лежит вне указанного диапазона, попробуйте еще раз')
            continue
        GPIO.output(dac, dec2bin(number))
        print(f'Предполагаемое напряжение на ЦАП: {5/256*number}')

except ValueError:
    print('Введено некорректное значение')
        
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
