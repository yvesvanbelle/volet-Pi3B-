import RPi.GPIO as GPIO
import requests
import time
import dht11

PIN_RELAIS = 18
PIN_TEMP = 23
PIN_LIGHT = 25


def relais(pin):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)

    GPIO.output(pin, True)
    time.sleep(3)
    GPIO.output(pin, False)
    time.sleep(3)

    GPIO.cleanup()


def temp_humidity_inside(pin):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    instance = dht11.DHT11(pin)

    while True:
        result = instance.read()
        if result.is_valid():
            GPIO.cleanup()
            return result.temperature, result.humidity

        time.sleep(1)


def temp_humidity_outside():
    weather_data_url = 'http://api.openweathermap.org/data/2.5/weather?q=Koekelberg,BE&units=metric' + \
                       'APPID=375e74b400588fcf07d13dbd342093fc'

    weather_data = requests.get(weather_data_url)
    weather_data = weather_data.json()
    temp = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    return temp, humidity


def light(pin):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)
    light_dark = GPIO.input(pin)
    GPIO.cleanup()
    return light_dark


if __name__ == '__main__':
    relais(PIN_RELAIS)
    print(light(PIN_LIGHT))
    print(temp_humidity_inside(PIN_TEMP))
    print(temp_humidity_outside())
