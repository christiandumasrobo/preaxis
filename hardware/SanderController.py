#!/usr/bin/env python3
import time
import os
import json
import pigpio
import subprocess
import sys
import argparse

import logging
logging.basicConfig(filename='log.log', level=logging.INFO)

log = logging.getLogger(__name__)

push_pin = 19
pull_pin = 26

class SanderController:
    def __init__(self):
        logging.debug('Initializing Controller')
        self.pi = pigpio.pi()
        #time.sleep(1)
        logging.debug('Controller initialized')

    def pull(self, duration):
        self.pi.write(pull_pin, 1)
        self.pi.write(push_pin, 0)
        time.sleep(duration)
        self.pi.write(pull_pin, 0)

    def push(self, duration):
        self.pi.write(push_pin, 1)
        self.pi.write(pull_pin, 0)
        time.sleep(duration)
        self.pi.write(push_pin, 0)

    def move(self, percent):
        self.pull(1.35)
        self.push(1.35 * percent / 100)

    def cleanup(self):
        self.pi.stop()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('command', help='push or pull')
    parser.add_argument('duration', help='in seconds')
    args = parser.parse_args()

    c = SanderController()
    commandMap = {
        'push': c.push,
        'pull': c.pull,
        'move': c.move,
    }
    commandMap[args.command](float(args.duration))
    c.cleanup()
