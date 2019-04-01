#  MIT LIcense
#  Copyright 2019 Yves Van Belle

import requests
import random

PIN_RELAIS = 18
PIN_TEMP = 23
PIN_LIGHT = 25


def relais(pin):
    print("Activated relais {}".format(pin))


def temp_humidity_inside(pin):
    temperature = random.randrange(-5, 50)
    humidity = random.randrange(0, 100)
    return temperature, humidity


def temp_humidity_outside():
    weather_data_url = 'http://api.openweathermap.org/data/2.5/weather?q=Koekelberg,BE&units=metric&' + \
                       'APPID=375e74b400588fcf07d13dbd342093fc'

    weather_data = requests.get(weather_data_url)
    weather_data = weather_data.json()
    temp = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    return temp, humidity


def is_dark(pin):
    light_dark = random.randint(0, 1)
    if light_dark == 0:
        return True
    elif light_dark == 1:
        return False


if __name__ == '__main__':
    print("----------")
    relais(PIN_RELAIS)
    print("Dark: {}".format(is_dark(PIN_LIGHT)))
    print("Inside temp, humidity: {}".format(temp_humidity_inside(PIN_TEMP)))
    print("Outside temp, humidity: {}".format(temp_humidity_outside()))
