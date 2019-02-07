import RPi.GPIO as GPIO
import time
import dht11

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


if __name__ == '__main__':
	#relais(pin=18)

	print(temp_humidity(23))
