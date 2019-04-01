#  MIT License
#  Copyright 2019 Yves Van Belle

import requests
import time
import random

PIN_RELAIS_UP = 18
PIN_RELAIS_DOWN = 21
PIN_TEMP = 23
PIN_LIGHT = 25


def relais(pin):
    print("Activated relais {}".format(pin))
    time.sleep(2)
    print("Dectivated relais {}".format(pin))


def volet_up():
    print("Up")
    relais(PIN_RELAIS_UP)


def volet_down():
    print("Down")
    relais(PIN_RELAIS_DOWN)


def temp_humidity_inside():
    temperature = random.randrange(16, 30)
    humidity = random.randrange(0, 100)
    return temperature, humidity


def temp_humidity_outside():
    weather_data_url = 'http://api.openweathermap.org/data/2.5/weather?' + \
                       'q=Koekelberg,BE&units=metric&' + \
                       'APPID=375e74b400588fcf07d13dbd342093fc'

    weather_data = requests.get(weather_data_url)
    weather_data = weather_data.json()
    temp = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    return temp, humidity


def is_dark():
    light_dark = random.randint(0, 1)
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
