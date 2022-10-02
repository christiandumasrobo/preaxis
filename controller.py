#!/usr/bin/env python
import RPi.GPIO as gp
import time

gp.setmode(gp.BCM)

turn_pin = 26
tilt_pin = 18
gp.setup(turn_pin, gp.OUT)
gp.setup(tilt_pin, gp.OUT)

p1 = gp.PWM(turn_pin, 50)
p2 = gp.PWM(tilt_pin, 100)

p1.start(2.5)
p2.start(2.5)

tilt_bot = 6
tilt_top = 9

turn_bot = 2
turn_top = 12

def turn(angle):
    dc_val = angle * 3 / 90 + 6
    p1.ChangeDutyCycle(dc_val)

def tilt(angle):
    print(angle)
    dc_val = angle * 10 / 90 + 2
    p2.ChangeDutyCycle(dc_val)

try:
    p1.ChangeDutyCycle(20.0)
    p2.ChangeDutyCycle(10.0)
    time.sleep(.01)
    p1.stop()
    p2.stop()
    gp.cleanup()
    exit()
    turn(45)
    tilt(45)

    time.sleep(5)

    turn(100)
    #tilt(50)
except Exception as e:
    print(e)

p1.stop()
p2.stop()
gp.cleanup()
