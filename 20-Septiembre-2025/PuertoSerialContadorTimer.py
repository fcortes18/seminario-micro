import machine
import utime
import _thread

global intContador
intContador = 0

pinLed1 = machine.Pin(4, machine.Pin.OUT)
pinLed2 = machine.Pin(3, machine.Pin.OUT)

objTim1 = machine.Timer()
objTim2 = machine.Timer()

objPuertoSerial0 = machine.UART(0, baudrate = 9600, tx = machine.Pin(0), rx = machine.Pin(1))

def Ya1(arg1):
    global pinLed1
    global intContador
    
    strContador = str(intContador)
    objPuertoSerial0.write(strContador + '\r\n')
    pinLed1.toggle()
        
def Ya2(arg1):
    global pinLed1
    global intContador
    
    intContador += 1
    pinLed2.toggle()

objTim1.init(period = 100, mode = machine.Timer.PERIODIC, callback = Ya1)
# utime.sleep_ms(250)
objTim2.init(period = 100, mode = machine.Timer.PERIODIC, callback = Ya2)

