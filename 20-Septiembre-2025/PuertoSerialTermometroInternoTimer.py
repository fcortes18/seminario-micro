from machine import ADC, Pin, Timer, UART
from utime import sleep_ms

pinLed1 = Pin(4, Pin.OUT)
pinLed2 = Pin(3, Pin.OUT)

global fltVoltaje
fltVoltaje = 0.0
strTemperatura = []

objTimer = Timer()
objSensorTemp = ADC(4)
objPuertoSerial0 = UART(0, baudrate = 9600, tx = Pin(0), rx = Pin(1))

def TimerLeeSensor(Dato):
    global pinLed1
    global fltVoltaje
    fltVoltaje = objSensorTemp.read_u16() * 3.3 / 65535
    pinLed1.toggle()
    
objTimer.init(period = 100, mode = Timer.PERIODIC, callback = TimerLeeSensor)

while True:
    
    fltTemperatura = 27.0 - (fltVoltaje - 0.706) / 0.001721
    strTemperatura = str(str(round(fltTemperatura, 0)))
    objPuertoSerial0.write(strTemperatura.strip(".0") +  '\r\n')
    pinLed2.toggle()
    sleep_ms(500)