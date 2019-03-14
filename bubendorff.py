import RPi.GPIO as GPIO
import requests
import time
import dht11


PINRELAIS = 18
PINTEMP = 23
PINLIGHT = 25


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
    WEATHER_DATA_URL  = 'http://api.openweathermap.org/data/2.5/weather?q=Koekelberg,BE&units=metricAPPID=375e74b400588fcf07d13dbd342093fc'

    weather_data = requests.get(WEATHER_DATA_URL)
    weather_data = weather_data.json()
    temp = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    return temp,humidity

def light(pin):
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pin, GPIO.IN)
	light_dark = GPIO.input(pin)
	GPIO.cleanup()
	return light_dark


if __name__ == '__main__':
    relais(PINRELAIS)
    print(light(PINLIGHT))
    print(temp_humidity_inside(PINTEMP))
	print(temp_humidity_outside())
	