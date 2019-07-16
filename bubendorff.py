import time
import datetime
import pickle
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
    time.sleep(1)
    GPIO.output(pin, False)
    time.sleep(1)

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


def start():
    begin_day = datetime.time(6, 30)
    end_day = datetime.time(17)
    current_time = datetime.datetime.now().time()
    current_day = datetime.datetime.now().weekday()  # 0 is monday
    light_or_dark = light(PINLIGHT)  # 0=dark 1=light
    temperature = temp_humidity(PINTEMP)[0]

    action = VOLETUP

    with open('/home/pi/volet-pi3b/statusvolet.txt', 'rb') as f:
        status = pickle.load(f)

    if not (begin_day < current_time < end_day):
        if light_or_dark == 0:
            action = VOLETDOWN

    if temperature > 24:
        action = VOLETDOWN

    if action != status:
        with open('/home/pi/volet-pi3b/statusvolet.txt', 'wb') as f:
            pickle.dump(action, f)
        relais(action)


if __name__ == '__main__':
    start()
