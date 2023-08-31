# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio, digitalio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)
btn0 = digitalio.DigitalInOut(board.D4)
btn1 = digitalio.DigitalInOut(board.D5)
btn0.pull = digitalio.Pull.DOWN
btn1.pull = digitalio.Pull.DOWN

angle=90

while True:
    if btn0.value is True:
        if not angle == 180:
            angle+=1
            my_servo.angle=angle
            print("Left")
            time.sleep(0.05)
    if btn1.value is True:
        if not angle == 0:
            angle-=1
            my_servo.angle=angle
            print("Right")
            time.sleep(0.05)