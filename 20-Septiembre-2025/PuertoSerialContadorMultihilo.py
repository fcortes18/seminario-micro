import machine
import utime
import _thread

global intStart1
global intBase
global intContador
intStart1 = 0
intBase = 100
intContador = 0

intStart100ms = utime.ticks_ms()

pinLed1 = machine.Pin(4, machine.Pin.OUT)
pinLed2 = machine.Pin(3, machine.Pin.OUT)

objPuertoSerial0 = machine.UART(0, baudrate = 9600, tx = machine.Pin(0), rx = machine.Pin(1))

def nucleo2():
    global intStart1
    global intBase
    global intContador
    
    while True:
        strContador = str(intContador)
        objPuertoSerial0.write(strContador + '\r\n')
        pinLed2.toggle()
        utime.sleep_ms(100)
        
_thread.start_new_thread(nucleo2, ())

while True:
    intDelta1 = utile.ticks_diff(utime.ticks_ms(), intStart1)
    if intDelta1 > intBase:
        intContador += 1
        intStart1 = utime.ticks_ms()
        pinLed1.toggle()