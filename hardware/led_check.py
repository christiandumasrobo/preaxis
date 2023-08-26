#!/usr/bin/env python3

STRIP_PIN = 21
import board
import neopixel
import random
import sys
import time
total_leds = 160
pixels = neopixel.NeoPixel(board.D21, total_leds)

lit_leds = 3

pixels[total_leds - 1] = (255, 255, 255)

