#!/usr/bin/env python3
# Licensed under the MIT license
# Copyright (c) 2019 Yves Van Belle (yvanbelle@outlook.com)

import time
import datetime
import pickle
import RPi.GPIO as GPIO
import dht11

VOLET_UP = 20
VOLET_DOWN = 21
PIN_TEMP = 23
PIN_LIGHT = 25
MAX_TEMP = 25


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


def main():
    begin_day = datetime.time(6, 30)
    end_day = datetime.time(17)
    current_time = datetime.datetime.now().time()
    current_day = datetime.datetime.now().weekday()  # 0 is monday
    light_or_dark = light(PIN_LIGHT)  # 0=dark 1=light
    temperature = temp_humidity(PIN_TEMP)[0]

    print('Day 0-6:', current_day)
    print('Time:', current_time)
    print('Dark 0 / Light 1', light_or_dark)
    print('Temperature', temperature)

    with open('/home/pi/volet-pi3b/statusvolet.txt', 'rb') as f:
        status = pickle.load(f)

    action = VOLET_UP

    if not (begin_day < current_time < end_day):
        if light_or_dark == 0:
            action = VOLET_DOWN

    if (current_day in (5, 6)) and (current_time < datetime.time(10)):
        action = VOLET_DOWN

    if temperature > MAX_TEMP:
        action = VOLET_DOWN

    if action != status:
        relais(action)

    with open('/home/pi/volet-pi3b/statusvolet.txt', 'wb') as f:
        pickle.dump(action, f)


if __name__ == '__main__':
    main()
