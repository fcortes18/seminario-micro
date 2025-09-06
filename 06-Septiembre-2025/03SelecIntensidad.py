from machine import Pin
from utime import sleep_ms

pinSw1 = Pin(16, Pin.IN, Pin.PULL_DOWN)
pinSw2 = Pin(17, Pin.IN, Pin.PULL_DOWN)
pinSw3 = Pin(18, Pin.IN, Pin.PULL_DOWN)
pinLed = Pin(19, Pin.OUT)

while True:
    if pinSw1.value() == 1:
        pinLed.on()
        sleep_ms(1)
        pinLed.off()
        sleep_ms(9)
        
    if pinSw2.value() == 1:
        pinLed.on()
        sleep_ms(5)
        pinLed.off()
        sleep_ms(5)
        
    if pinSw3.value() == 1:
        pinLed.on()
        sleep_ms(9)
        pinLed.off()
        sleep_ms(1)