from machine import Pin
import utime

intStart1 = utime.ticks_ms()
intStart2 = utime.ticks_ms()

intDelta1 = 0
intDelta2 = 0

pinLed1 = Pin(21, Pin.OUT)
pinLed2 = Pin(22, Pin.OUT)

while True:
    intDelta1 = utime.ticks_diff(utime.ticks_ms(), intStart1)
    if intDelta1 > 1000:
        intStart1 = utime.ticks_ms()
        pinLed1.toggle()
    
    intDelta2 = utime.ticks_diff(utime.ticks_ms(), intStart2)
    if intDelta2 > 10:
        intStart2 = utime.ticks_ms()
        pinLed2.toggle()
        
