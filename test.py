from subprocess import check_output as co
import time


def blink_leds(times):
    co(['sudo ./led_test.py ' + str(times)], shell=True)

def move_table(turn, tilt):
    co(['sudo systemctl start pigpiod'], shell=True)
    co(['./controller.py ' + str(turn) + ' ' + str(tilt)], shell=True)
    co(['sudo systemctl stop pigpiod'], shell=True)

#blink_leds(1)
#move_table(50, 100)

for i in range(10):
    time.sleep(1)
    blink_leds(1)
