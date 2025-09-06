from machine import Pin

pinLed1 = Pin(20, Pin.OUT)
pinSw1 = Pin(17, Pin.IN)

while True:
    pinLed1.value(pinSw1.value())