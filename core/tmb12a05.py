from machine import Pin
from config.board import BuzzerPin


buzzer = Pin(BuzzerPin.PLUS, mode=Pin.OUT, value=0)
