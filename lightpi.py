import time
import RPi.GPIO as GPIO


def RCtime(RCpin):
    reading = 0
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(0.1)
    
    GPIO.setup(RCpin, GPIO.IN)

    while (GPIO.input(RCpin) == GPIO.LOW):
        reading += 1

    GPIO.cleanup()
    return reading

if __name__ == '__main__':
    total=0
    for i in range(0,20):
        reading = RCtime(21)
        print(reading)        
        total += reading
    print(total/20)
