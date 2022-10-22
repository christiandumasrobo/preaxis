#!/usr/bin/env python3
import time
import os
import json
import pigpio
import subprocess
import sys

import logging
logging.basicConfig(filename='log.log', level=logging.INFO)

log = logging.getLogger(__name__)

turn_pin = 26
tilt_pin = 18

class TableController:
    def __init__(self):
        logging.debug('Initializing Controller')
        self.pi = pigpio.pi()
        self.last_turn = 50
        self.last_tilt = 50
        if os.path.exists('state.json'):
            with open('state.json', 'r') as fin:
                state_json = json.loads(fin.read())
                self.last_turn = state_json[0]
                self.last_tilt = state_json[1]
        self.turn(self.last_turn)
        self.tilt(self.last_tilt)
        time.sleep(2)
        logging.debug('Controller initialized')

    def turn(self, percent):
        logging.debug('Turning to %f' % percent)
        pw = (2500 - 500) * percent / 100 + 500
        pw = max(pw, 500)
        logging.debug(' pw: %f' % pw)
        self.pi.set_servo_pulsewidth(turn_pin, pw)
        logging.debug('Successful turn')

    def tilt(self, percent):
        logging.debug('Tilting to %f' % percent)
        pw = (1900 - 1450) * percent / 100 + 1450
        pw = max(pw, 500)
        logging.debug(' pw: %f' % pw)
        self.pi.set_servo_pulsewidth(tilt_pin, pw)
        logging.debug('Successful tilt')

    def move_to(self, turn_v, tilt_v, duration):
        logging.debug('Moving to %f %f' % (turn_v, tilt_v))
        turn_dist = turn_v - self.last_turn
        turn_inc = turn_dist / (10 * duration)
        tilt_dist = tilt_v - self.last_tilt
        tilt_inc = tilt_dist / (10 * duration)

        for i in range(duration*10):
            self.turn(self.last_turn)
            self.tilt(self.last_tilt)
            self.last_turn += turn_inc
            self.last_tilt += tilt_inc
            time.sleep(1/10)

        logging.debug('Successful move')

    def cleanup(self):
        with open('state.json', 'w+') as fout:
            fout.write(json.dumps([self.last_turn, self.last_tilt]))
        self.pi.stop()


c = TableController()
c.move_to(float(sys.argv[1]), float(sys.argv[2]), 3)
c.cleanup()
