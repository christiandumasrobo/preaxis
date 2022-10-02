#!/usr/bin/env python3
import pigpio
import time

turn_pin = 26
tilt_pin = 18

class TableController:
    def __init__(self):
        print('Initializing Controller')
        self.last_turn = 50
        self.last_tilt = 50
        self.turn(self.last_turn)
        self.tilt(self.last_tilt)
        time.sleep(2)
        print('Controller initialized')

    def turn(self, percent):
        print('Turning to', percent)
        pw = (2500 - 500) * percent / 100 + 500
        pi.set_servo_pulsewidth(turn_pin, pw)
        print('Successful turn')

    def tilt(self, percent):
        print('Tilting to', percent)
        pw = (1900 - 1450) * percent / 100 + 1450
        pi.set_servo_pulsewidth(tilt_pin, pw)
        print('Successful tilt')

    def move_to(self, turn_v, tilt_v):
        pass##turn_inc = 


pi = pigpio.pi()
c = TableController()
c.tilt(0)
time.sleep(2)
for i in range(100):
    c.turn(i)
    time.sleep(0.1)
pi.stop()
