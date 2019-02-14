import RPi.GPIO as GPIO

PIN_NUMBER = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_NUMBER, GPIO.IN)

print(GPIO.input(PIN_NUMBER))

GPIO.cleanup()
