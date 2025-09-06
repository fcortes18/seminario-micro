from machine import ADC
from utime import sleep

intADC = 0
fltVoltaje = 0.0

pinPot = ADC(0)

while True:
    intADC = pinPot.read_u16()
    fltVoltaje = (intADC) * 3.3 / 65535.0
    temp = fltVoltaje * 100.0
    sleep(1)
    print("Temperatura = ", temp) # Voltmetro