import time
import datetime
import RPi.GPIO as GPIO
import dht11

VOLETUP = 20
VOLETDOWN = 21
PINTEMP = 23
PINLIGHT = 25


def relais(pin):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)

    GPIO.output(pin, True)
    time.sleep(2)
    GPIO.output(pin, False)
    time.sleep(2)

    GPIO.cleanup()


def temp_humidity(pin):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    instance = dht11.DHT11(pin)

    while True:
        result = instance.read()
        if result.is_valid():
            GPIO.cleanup()
            return result.temperature, result.humidity

        time.sleep(1)


def light(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)

    return GPIO.input(pin)


if __name__ == '__main__':
    start_evening = datetime.time(17)
    start_morning = datetime.time(6, 30)
    current_time = datetime.datetime.now().time()
    current_day = datetime.datetime.now().weekday()  # 0 is monday

    with open('statusvolet.txt', 'r') as f:
        status = f.read()

    action = VOLETUP

    if(light == 0):  # if it is dark
        if(start_evening < current_time < start_morning):  # between 17:00 to 6:30
            if(current_day < 5):  # if current day is before saturday
                action = VOLETDOWN

    if(temp_humidity(PINLIGHT)[0] > 24):  # if temp is higher than 24°C
        action = VOLETDOWN

    if(action != status):
        with open('statusvolet.txt', 'w') as f:
            f.write(action)
        relais(action)
