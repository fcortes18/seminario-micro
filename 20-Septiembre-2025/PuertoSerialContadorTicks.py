from machine import Pin, UART
import utime

intStart1 = 0
intBase = 10
intContador = 0
intStart1 = utime.ticks_ms()

pinLed = Pin(4, Pin.OUT)
objPuertoSerial0 = UART(0, baudrate = 9600, tx = Pin(0), rx = Pin(1))


while True:
    intDelta1 = utime.ticks_diff(utime.ticks_ms(), intStart1)
    if intDelta1 > intBase:
        intContador += 1
        intStart1 = utime.ticks_ms()
        pinLed.toggle()
        strContador = str(intContador)
        objPuertoSerial0.write(strContador + '\r\n')
        pinLed.toggle()