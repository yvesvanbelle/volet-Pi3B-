import Rpi.GPIO as GPIO
import dht11
import time


def get_t_h():
    #  Initialize GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()

    #  Read data from DHT11
    reading = dht11.DHT11(pin=23)

    #  Get temperature & humidity
    t = reading.temperature
    h = reading.humidity

    return t,h


if __name__ == '__main__':
    for i in range(100):
        print(get_t_h())
        time.sleep(1)