from machine import Pin
from utime import sleep_ms

tiempo = 50
back = False
while True:
    pin = 10
    
    while pin < 14:
        pinLed = Pin(pin, Pin.OUT)
        pinLed.on()
        sleep_ms(tiempo)
        pinLed.off()
        
        if pin == 13:
            back = True
            
        if pin == 10:
            back = False
        
        if back == False:
            pin = pin + 1
        else:
            pin = pin - 1
            
