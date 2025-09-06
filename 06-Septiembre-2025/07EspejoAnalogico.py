from machine import Pin, PWM, ADC
from utime import sleep

intADC = 0
pinPot = ADC(26)

pinLedPwm = PWM(Pin(5)) #crea objeto
pinLedPwm.freq(1000) #configura la frecuencia de trabajo del PWM

while True:
    intADC = pinPot.read_u16()
    pinLedPwm.duty_u16(intADC)