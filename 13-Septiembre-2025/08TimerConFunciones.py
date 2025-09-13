import machine
import utime

objTim1 = machine.Timer()
objTim2 = machine.Timer()

intDelta1 = 0
intDelta2 = 0

pinLed1 = machine.Pin(21, machine.Pin.OUT)
pinLed2 = machine.Pin(22, machine.Pin.OUT)

def Ya1(arg1):
    global pinLed1
    pinLed1.toggle()
    
def Ya2(arg1):
    global pinLed2
    pinLed2.toggle()
    
objTim1.init(freq = 1, mode = machine.Timer.PERIODIC, callback = Ya1)
# utime.sleep_ms(250)
objTim2.init(period = 500, mode = machine.Timer.PERIODIC, callback = Ya2)
