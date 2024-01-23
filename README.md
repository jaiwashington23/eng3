### Multipart Design Practice

### Description 

the purpose of this assignment is to get ready for the Certified Onshape Associate certification. You should finish this assignment in one hour.  


### EVIDENCE
![nig](https://github.com/jaiwashington23/eng3/assets/143545376/db5ca9dc-3c22-44d1-9501-24f969ecf020)


## PART LINK
https://cvilleschools.onshape.com/documents/20cebd7642126c2674b6d080/w/757516b6ca5430c4e704b050/e/c7e861ee95e2d4e8f447d53e?renderMode=0&uiState=654d45028421ab756fcf9b65


### REFLECTION

This assignment was fun and challenging. I learned a lot and got even more comfortable with Onshape! Even though it was challenging I had fun because Onshap is my favorite thing to do in this class. The only thing I would have done differently was the amount of time I spent on this assignment.  



### Swing Arm

### Description
the purpose of this assignment is to get ready for the Certified Onshape Associate certification. This assignment will help you determine what additional concepts you need to focus on for the certification exam. 



 ### Evidence 
![swing arm Copy 1](https://github.com/jaiwashington23/eng3/assets/143545376/593f98b7-8d45-4831-ba5a-53cc0c00d861)

## part link 
https://cvilleschools.onshape.com/documents/213f1bc214a32d55b924fa98/w/52f7d1c9b76fb7044b183068/e/551a0ea8520cadca6ad90a14?renderMode=0&uiState=6538178547cb436741981539


### Reflection
This assignment was fun and challenging. I learned a lot and got even more comfortable with Onshape! Even though it was challenging I had fun because Onshap is my favorite thing to do in this class.





## Hanger onshape 
https://cvilleschools.onshape.com/documents/213f1bc214a32d55b924fa98/w/52f7d1c9b76fb7044b183068/e/551a0ea8520cadca6ad90a1
### Assignment Description
The purpose of this assignment is to improve onshape skills. This assignment is helpful in getting familiar with the mass and getting more comfortable with Onshape in general.  
### Evidence

Take several cropped screenshots of your Onshape document from different angles. Try to capture all important aspects of the design. Turn off overlays that obscure the parts, such as planes or mate connectors. Your images should have captions, so the reader knows what they are looking at!  
![image](https://github.com/jaiwashington23/eng3/assets/143545376/349e3513-8ace-4f4f-8edb-405f5165bdac)

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Reflection
the way I tried to do it at first was wrong. the challenging part was geting to the right mass. I figured it out by asking for help. I learned that shortcuts are not the way. I wish the measurements were more clear.

&nbsp;



# CircuitPython
 [ directory of all students!](https://github.com/chssigma/Class_Accounts)
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code Snippets
Assignment: Get an RGB LED to cycle through a bunch of colors, but prettily. It should gradually shift colors, cycling through the entire rainbow. We ended up using an example neopixel code from "the complete Adafruit Library" and loading that after changing a few things, such as how fast it goes through the cycle.

```python
pixels = neopixel.NeoPixel(PIN, NUMPIXELS, brightness=BRIGHTNESS, auto_write=False)\
def rainbow_cycle(wait):
    for color in range(255):
        for pixel in range(len(pixels)):  # pylint: disable=consider-using-enumerate
            pixel_index = (pixel * 256 // len(pixels)) + color * 5
            pixels[pixel] = colorwheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)
while True:
    rainbow_cycle(SPEED)
# CPyProjectTemplate
Put a description for your project here!
This repo is a template VS code project for CircuitPython projects that automatically uploads your code to the board when you press F5. Requires F5Anything extension.
## What does this do?
This makes it easirt to develop for boards like 
## Use
### Every new project:
1. Make a GitHub account if you don't have one with your normal school credentials and sign into it.
2. Click the big green Use This Template button at the top of this page.
3. Name the new repository something appropriate to the purpose of your project (Your first one should probably be named `Engr3`).
4. Hit "Create repository from template." (The default settings should be fine.)
5. Open VS Code on your machine. Click Clone Repository. If it doesn't show up, hit Ctrl+Shift+P and then type Clone, then hit Enter.
6. Paste in the link to the new repository you've just created from the template and hit enter.
7. For the location, Documents folder.
8. Hit "Open Cloned Directory" in the bottom-left corner.
9. Install the reccomended extensions when you get that popup in the lower right corner. IF the pop-up dissapears before you can click it, hit the tiny bell icon in the lower left corner to bring it back.
### To commit from VS Code:
1. Go to the little branch icon in the left bar of VS Code.
2. Click the + icon next to the files you want to commit.
3. Write a message that descibes your changes in the "Message" box and hit commit.
4. If you get an error about user.name and user.email, see the next section.
5. Click the "Sync changes" button.
### If you get an error about user.name and user.email
1. In VS Code, hit `` Ctrl+Shift+` ``
2. Filling in your actual information, run the following commands one line at a time. The paste shortcut is `Ctrl+V` or you can right click then hit paste. Spelling must match exactly:
```

[C:\Users\abuckne38\Documents\engr3\hello.py
](https://github.com/addddddy/engr3/blob/main/hello.py)

### Evidence

![ezgif com-video-to-gif](https://github.com/addddddy/engr3/assets/143544940/8e3104e2-fc72-45ad-a922-281586c123d8)

Photo creds to Addy Buckner
[Addy Buckner's Github](https://github.com/addddddy)

### Wiring
We literally had no wiring. The neopixel is directly attached to the board, so all we had to do was plug in the board
<img src="https://cdn-learn.adafruit.com/assets/assets/000/041/507/original/microcontrollers_3505_iso_ORIG.jpg">
Image credit goes to [Lady Ada](https://learn.adafruit.com/adafruit-metro-m0-express)

### Reflection
This was, at first, a confusing assignment. With no prior knowledge of any code of any sort, I was really confused. I spent the first two days just staring at the computer and doing nothing. Finally, I jumped right in. I spent about a whole day just googling up random commands before we got the wise advice to just find an example code. So that is precisely what we did. We used a random code example labeled something along the lines of "neopixel rainbow test" from "the complete Adafruit Library". All that we had to do was press run. It happened to be perfect, all we  had to do was adjust a few  lines of  code and it  ran perfectly.


## CircuitPython_Servo

### Description & Code Snippets
The goal of this assignment is to get a 180° micro servo to slowly sweep back and forth between 0 and 180°. 

### Code

"""CircuitPython Essentials Capacitive Touch on two pins example. Does not work on Trinket M0!"""
import time
import board
import touchio
import pwmio
from adafruit_motor import servo


pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)


my_servo = servo.ContinuousServo(pwm)

touch_A4 = touchio.TouchIn(board.A4)  # Not a touch pin on Trinket M0!
touch_A5 = touchio.TouchIn(board.A5)  # Not a touch pin on Trinket M0!

while True:
    my_servo.throttle = 0.0
    while touch_A4.value:
        my_servo.throttle = 1.0
        time.sleep(.5)
    while touch_A5.value:
        my_servo.throttle = -1.0
        time.sleep(.5)
Josh poo



### Evidence

![ezgif com-optimize](https://github.com/addddddy/engr3/assets/143544940/561c9908-fda6-4a8d-a112-b2ad3f70374c)

This beautiful GIF was finely produced by Addy Buckner
[Addy's Github](https://github.com/addddddy)

### Wiring

![267764949-da8131b8-15df-4c77-98ea-45a548e7e9d1](https://github.com/jaiwashington23/eng3/assets/143545376/6e5e0dab-db50-4565-97cc-af7b9c2c29f8)

### Reflection
The servo wasn't hard but did have some challenging parts when it came to code. The cod was challenging because I was just getting back into it as well as me not being the best coder. I figured it out by asking for help. what helped me succeed was looking at examples of code and wiring.  



## CircuitPython_Motor control

### Description & Code Snippets
In this assignment, you will determine how much voltage you send to the transistor gate and that in turn will determine how much current runs from the 6 V battery pack through the motor.  The motor/transistor part of the circuit is below. 
import board
import analogio

motor = analogio.AnalogOut(board.A0)
pot = analogio.AnalogIn(board.A1)
while True:
    speed = pot.value
    motor.value = speed
## code 

spinny = pwmio.PWMOut(board.D6, duty_cycle=65535,frequency = 5000 )# wire in pin 5
speed = analogio.AnalogIn(board.A1)
while True:
    sdfg = speed.value
    spinny.duty_cycle = sdfg

  ###  Evidence
https://github.com/SempronChip/engr3/assets/143545309/15a4333c-a8c2-4cba-8b52-bf43765f76a8

 ### Wiring
![IRLB8721 Motor Control](https://github.com/jaiwashington23/eng3/assets/143545376/6747d782-7cf2-47e0-a06b-c1321138d4fb)


### Reflection
The hardest part of this assignment was getting the wiring right! For me, wiring is not something I'm fully comfortable with so it was definitely a little struggle. I learned that 
working together makes everything better. I also  learned the importance of import time when it comes to code.


### Description 

The goal of this assignment is to make the neopixel change color based on the distances reported by the ultrasonic sensor. we used the previous code we had for the neopixel to include the if statements and distance sensor.

### code 

# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_hcsr04
import neopixel

NUMPIXELS = 1  # Update this to match the number of LEDs.
SPEED = 0.05  # Increase to slow down the rainbow. Decrease to speed it up.
BRIGHTNESS = 1.0  # A number between 0.0 and 1.0, where 0.0 is off, and 1.0 is max.
PIN = board.NEOPIXEL
pixels = neopixel.NeoPixel(PIN, NUMPIXELS, brightness=BRIGHTNESS, auto_write=False)
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)

while True:
    try:
        print((sonar.distance,))
        if sonar.distance < 5:
            for pixel in range(len(pixels)):  # pylint: disable=consider-using-enumerate
                pixels[pixel] = (255, 0,0)
                pixels.show()
        if sonar.distance > 5 and sonar.distance < 20:
            for pixel in range(len(pixels)):  # pylint: disable=consider-using-enumerate
                pixels[pixel] = (255-(sonar.distance - 5 / 15 * 255), 0, (sonar.distance - 5 / 15 * 255))
                pixels.show()

        if sonar.distance > 20 and sonar.distance < 35:
            for pixel in range(len(pixels)):  # pylint: disable=consider-using-enumerate
                pixels[pixel] = ( 0, (sonar.distance - 5 / 15 * 255), 255-(sonar.distance - 5 / 15 * 255))
                pixels.show()
        if sonar.distance > 35:
            for pixel in range(len(pixels)):  # pylint: disable=consider-using-enumerate
                pixels[pixel] = ( 0, 255, 0)
                pixels.show()   
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)

     ### Wiring
![134725601-72db0fcb-0d50-486c-aff5-9e0ec1772057](https://github.com/jaiwashington23/eng3/assets/143545376/7179987a-2a13-480b-bbf1-24bf72fe7b91)


### Reflection
This assignment was challenging because I kept putting wires in the wrong pins. I also found this assignment to be really cool because we used the old code to make a new code! I learned to always save your code because you never know when you will need it.


### Description 



### code 
# Rotary Encodare light thingksf;ja             # [lines 1-7] Import and set up neccesary libraries
import time
import rotaryio
import neopixel
import board
from lcd import LCD
from i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull


encoder = rotaryio.IncrementalEncoder(board.D4, board.D3) # [lines 9-24] Start all Variables and define INs and OUTs
last_position = 0
btn = DigitalInOut(board.D2)
btn.direction = Direction.INPUT
btn.pull = Pull.UP
state = 0
Button = 1
led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = .3
i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)





while True:                #[lines 27-38] Set up varible for encoder, limit it to >0 and <3
    position = encoder.position
    if position != last_position:
        state = position % 3
        if state == 0:     #[lines 39-47] Print to LCD based on Encoder Var
            lcd.clear()
            lcd.set_cursor_pos(0, 0) # [39
            lcd.print("Don't stop")
        elif state == 1:
            lcd.clear()
            lcd.set_cursor_pos(0, 0)
            lcd.print("Speed up")
        elif state == 2:
            lcd.clear()
            lcd.set_cursor_pos(0, 0)
            lcd.print("Slam on brakes")
    if btn.value == 0 and Button == 1: #[lines 48-63] If the button is pressed make the Encoder Var match the lights.
        print("buttion")
        if state == 0:
            print('g')
            led[0] = (0, 255, 0)
        elif state == 1:
            print('y')
            led[0] = (255, 234, 0)
        elif state == 2:
            print('r')
            led[0] = (250, 0, 0)
        Button = 0       #[lines 64-68] Resets and delay
    if btn.value == 1:
        time.sleep(.1)
        Button = 1
    last_position = position

### Wiring
![134725601-72db0fcb-0d50-486c-aff5-9e0ec1772057](https://github.com/jaiwashington23/eng3/blob/3aac1d4f067bfd9bf4bd6c16ee14970643e7cd80/wiring.PNG)


### Reflection
