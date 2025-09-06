from machine import Pin
from utime import sleep

leds = [Pin(14, Pin.OUT),Pin(15, Pin.OUT),Pin(16, Pin.OUT),Pin(17, Pin.OUT)]
leds_rev = leds[::-1]

seconds = 0.02

while True:
    for led in leds:
        led.on()
        sleep(seconds)
        led.off()

    for led in leds_rev:
        led.on
        sleep(seconds)
        led.off()