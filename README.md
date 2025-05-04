# Active buzzer in Micropython

Active buzzer example in Micropython for Raspberry Pi Pico.

## Hardware

-   [Raspberry Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/)
-   Active Buzzer TMB12A05 (5V)

## Software

-   [MicroPython](https://micropython.org/download/RPI_PICO/) - Pico firmware (RP2 port)

## Code examples

See `boot.py` for code example.

```py
from core.tmb12a05 import buzzer
buzzer.on()
time.sleep(0.1)
buzzer.toggle()
```
