from machine import ADC, Pin, Timer, UART
from utime import sleep_ms
import sh1106

pinLed1 = Pin(4, Pin.OUT)
pinLed2 = Pin(3, Pin.OUT)

global fltVoltaje
fltVoltaje = 0.0
strTemperatura = []

objTimer = Timer()
objSensorTemp = ADC(4)
objPuertoSerial0 = UART(0, baudrate = 9600, tx = Pin(0), rx = Pin(1))
objI2C = machine.I2C(1, scl=machine.Pin(19), sda=machine.Pin(18))
objPantOled = sh1106.SH1106_I2C(128, 64, objI2C)

def TimerLeeSensor(Dato):
    global pinLed1
    global fltVoltaje
    fltVoltaje = objSensorTemp.read_u16() * 3.3 / 65535
    pinLed1.toggle()

objTimer.init(period = 5, mode = Timer.PERIODIC, callback = TimerLeeSensor)

objPantOled.fill(0)
objPantOled.rotate(1)
objPantOled.show()
sleep_ms(500)
objPantOled.text("Temperatura = ", 0, 0)
objPantOled.show()

while True:
    
    fltTemperatura = 27.0 - (fltVoltaje - 0.706) / 0.001721
    strTemperatura = str(str(round(fltTemperatura, 0)))
    objPuertoSerial0.write(strTemperatura.replace(".0", "") + " °C" +  '\r\n')

    objPantOled.text(strTemperatura.replace(".0", "") + " gC", 0, 10)
    objPantOled.show()
    objPantOled.text(strTemperatura.replace(".0", "") + " gC", 0, 10, 0)

    pinLed2.toggle()
    sleep_ms(500)