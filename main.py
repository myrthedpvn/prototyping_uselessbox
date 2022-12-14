#!/bin/python

from gpiozero import LED
#imports LED functions from gpiozero library
from gpiozero import Button
#imports Button functions from gpiozero library
import time
import random
from gpiozero import Servo


led = LED(4)
#declare the GPIO pin 4 for LED output and store it in led variable
button = Button(17)
#declare the GPIO pin 17 for Button output and store it in button variable
servo = Servo(21)
servo.value = None

def robot():
        time.sleep(1)
        servo.value = -0.8 
	#Move servo to push button
        time.sleep(0.25)
        led.toggle() 
	#Turn led off
        servo.value = None 
	#Servo doesn't move and also doesn't make sound
        time.sleep(1)
        servo.value = 1 
	#Move servo back to basic
        time.sleep(0.5)
        servo.value = None
	#Servo doesn't move and also doesn't make sound
        main()

def button_led():
	while True:
		if button.is_pressed:
			print('button is pressed')
			led.toggle() 
			#Turn led on
			time.sleep(0.5)
			robot()
def main():
	button_led()

if __name__ == '__main__':  # code to execute if called from command-line
        main()
