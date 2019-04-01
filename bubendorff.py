#  MIT LIcense
#  Copyright 2019 Yves Van Belle

import RPi.GPIO as GPIO
import requests
import time
import dht11

PIN_RELAIS_UP = 18
PIN_RELAIS_DOWN = 21
PIN_TEMP = 23
PIN_LIGHT = 25


def relais(pin):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)

    GPIO.output(pin, True)
    time.sleep(2)
    GPIO.output(pin, False)
    time.sleep(2)

    GPIO.cleanup()


def volet_up():
    relais(PIN_RELAIS_UP)


def volet_down():
    relais(PIN_RELAIS_DOWN)


def temp_humidity_inside():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    instance = dht11.DHT11(PIN_TEMP)

    while True:
        result = instance.read()
        if result.is_valid():
            GPIO.cleanup()
            return result.temperature, result.humidity

        time.sleep(1)


def temp_humidity_outside():
    weather_data_url = 'http://api.openweathermap.org/data/2.5/weather?q=Koekelberg,BE&units=metric&' + \
                       'APPID=375e74b400588fcf07d13dbd342093fc'

    weather_data = requests.get(weather_data_url)
    weather_data = weather_data.json()
    temp = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    return temp, humidity


def is_dark():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_LIGHT, GPIO.IN)
    light_dark = GPIO.input(PIN_LIGHT)
    GPIO.cleanup()
    if light_dark == 0:
        return True
    elif light_dark == 1:
        return False


if __name__ == '__main__':
    print("----------")
    volet_up()
    volet_down()
    print("Dark: {}".format(is_dark()))
    print("Inside temp, humidity: {}".format(temp_humidity_inside()))
    print("Outside temp, humidity: {}".format(temp_humidity_outside()))
