import time

import machine
from core.tmb12a05 import buzzer
from config.board import Pico

# Power-on beep
buzzer.toggle()
time.sleep(0.03)
buzzer.toggle()

time.sleep(0.1)
machine.freq(Pico.MCU_FREQUENCY)
machine.RTC().datetime(Pico.RTC_DATETIME)  # sync internal RTC

# Boot complete beep
buzzer.toggle()
time.sleep(0.03)
buzzer.toggle()
