from machine import Pin, UART
import utime

pinLed = Pin(4, Pin.OUT)
miPuertoSerial = UART(0, baudrate = 9600, tx = Pin(0), rx = Pin(1))
miPuertoSerial.write('Contador \r\n')

intContador = 0
strContador = []

while True:
    intContador += 1
    strContador = str(intContador)
    miPuertoSerial.write(strContador + '\r\n')
    pinLed.toggle()
    utime.sleep_ms(1000)