from machine import Pin

pinSw1 = Pin(16, Pin.IN)
pinSw2 = Pin(17, Pin.IN)
pinSw3 = Pin(18, Pin.IN)
pinLed1 = Pin(19, Pin.OUT)
pinLed2 = Pin(20, Pin.OUT)
pinLed3 = Pin(21, Pin.OUT)


while True:
    pinLed1.value(pinSw1.value())
    pinLed2.value(pinSw2.value())
    pinLed3.value(pinSw3.value())