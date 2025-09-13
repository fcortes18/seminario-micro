from machine import Pin
import utime
import _thread

pinSwMasFrec = Pin(15, Pin.IN, Pin.PULL_DOWN)
pinSwMenFrec = Pin(16, Pin.IN, Pin.PULL_DOWN)

pinLed1 = Pin(21, Pin.OUT)
pinLed2 = Pin(22, Pin.OUT)

global intTiempo
intTiempo = 500

def nucleo1():
    global intTiempo
    while True:
        pinLed1.on()
        utime.sleep_ms(intTiempo)
        pinLed1.off()
        utime.sleep_ms(intTiempo)
        
_thread.start_new_thread(nucleo1, ())

#Nucleo principal
while True:
    global intTiempo
    if pinSwMasFrec():
        utime.sleep_ms(20) #Tiempo de rebote
        intTiempo -= 20
        pinLed2.toggle()
        while pinSwMasFrec():
            pass
        
    if pinSwMenFrec():
        utime.sleep_ms(20)
        intTiempo += 20
        pinLed2.toggle()
        while pinSwMenFrec():
            pass
    
    
    
    
    