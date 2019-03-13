import RPi.GPIO as GPIO
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
        relais(PINRELAIS)
        print(light(PINLIGHT))
        print(temp_humidity(PINTEMP))
