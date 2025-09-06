from machine import ADC
from utime import sleep

intADC = 0
pinPot = ADC(26)

while True:
    intADC = pinPot.read_u16()
    sleep(1)
    print("ADC = ", intADC)