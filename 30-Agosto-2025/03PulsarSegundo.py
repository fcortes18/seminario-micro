from machine import Pin
from utime import sleep

# Constructor
pinLed = Pin(28, Pin.OUT)


while True:
    for i in range(0, 100):
        pinLed.value(1)
        sleep(0.001)
        pinLed.value(0)
        sleep(0.009)
    for i in range(0, 100):
        pinLed.value(1)
        sleep(0.005)
        pinLed.value(0)
        sleep(0.005)
    for i in range(0, 100):
        pinLed.value(1)
        sleep(0.009)
        pinLed.value(0)
        sleep(0.001)