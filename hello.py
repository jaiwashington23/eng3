# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
from adafruit_motor import servo
import digitalio

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)


btn0 = digitalio.DigitalInOut(board.D4)
btn1 = digitalio.DigitalInOut(board.D5)
btn0.pull = digitalio.Pull.DOWN
btn1.pull = digitalio.Pull.DOWN

angle=90
print("hi")


while True:
    if btn0.value:
        if angle < 178:
            angle+=1
            my_servo.angle=angle
            print(angle)
            time.sleep(0.01
        )
    if btn1.value:
        if angle> 5:
            angle-=1
            my_servo.angle=angle
            print(angle)
            time.sleep(0.01)

            