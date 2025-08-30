from machine import Pin
from utime import sleep_ms

# Constructor
pinLed = Pin(28, Pin.OUT)

while True:
    for intensidad in range(0, 10): 
        for j in range(0, 10):
            pinLed.value(1)
            sleep_ms(10-intensidad)
            pinLed.value(0)
            sleep_ms(intensidad)
    for intensidad in range(0, 10): 
        for j in range(0, 10):
            pinLed.value(1)
            sleep_ms(intensidad)
            pinLed.value(0)
            sleep_ms(10-intensidad)