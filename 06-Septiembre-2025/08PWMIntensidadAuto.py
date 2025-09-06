from machine import Pin, PWM
from utime import sleep_us

intTiempo = 50
pinLedPwm = PWM(Pin(5))

pinLedPwm.freq(1000)
while True:
    for intensidad in range(65535):
        pinLedPwm.duty_u16(intensidad)
        sleep_us(1)
    for intensidad in reversed(range(65535)):
        pinLedPwm.duty_u16(intensidad)
        sleep_us(1)