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

for idx in range(int(sys.argv[1])):
    for x in range(total_leds):
        pixels[x] = (0, 0, 0)
    leds_so_far = []
    while len(leds_so_far) < lit_leds:
        led_to_light = random.randint(0, total_leds - 1)
        if led_to_light not in leds_so_far:
            leds_so_far.append(led_to_light)

    for x in leds_so_far:
        pixels[x] = (255, 255, 255)
    time.sleep(0.5)

