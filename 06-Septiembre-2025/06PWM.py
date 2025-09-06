from machine import Pin, PWM
from utime import sleep

intTiempo = 50
pinLedPwm = PWM(Pin(5)) #crea objeto

pinLedPwm.freq(1000) #configura la frecuencia de trabajo del PWM

while True:
    pinLedPwm.duty_u16(60000) #Max a poner es el de 65535