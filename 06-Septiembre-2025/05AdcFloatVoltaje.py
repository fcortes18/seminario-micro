from machine import ADC
from utime import sleep

intADC = 0
fltVoltaje = 0.0

pinPot = ADC(0) # Otra manera de llamarlo, es el ADC0

while True:
    intADC = pinPot.read_u16()
    fltVoltaje = (intADC - 300) * 3.3 / 65535.0 # (Ajuste por ruido) * Voltaje referencia / Total combinaciones 2 a la 16 menos 1
    sleep(1)
    print("ADC = ", fltVoltaje) # Voltmetro