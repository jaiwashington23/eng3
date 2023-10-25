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

