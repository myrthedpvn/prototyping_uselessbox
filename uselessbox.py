#!/bin/python
import pigpio
from gpiozero import LED
#imports LED functions from gpiozero library
from gpiozero import Button
#imports Button functions from gpiozero library
from gpiozero import Servo
import time
import random

led = LED(4)
#declare the GPIO pin 4 for LED output and store it in led variable
button = Button(17)
#declare the GPIO pin 17 for Button output and store it in button variable
myservo = 21
#declare the GPIO pin 21 for Servo

pwm = pigpio.pi()
pwm.set_mode(myservo, pigpio.OUTPUT)
pwm.set_PWM_frequency(myservo, 50) 

def robot():
        print( "0 deg" )
        pwm.set_servo_pulsewidth( myservo, 500 ) ;
        time.sleep( 3 )

        print( "90 deg" )
        pwm.set_servo_pulsewidth( myservo, 1500 ) ;
        time.sleep( 3 )

        print( "180 deg" )
        pwm.set_servo_pulsewidth( myservo, 2500 ) ;
        time.sleep( 3 )

        # turning off servo
        pwm.set_PWM_dutycycle( myservo, 0 )
        pwm.set_PWM_frequency( myservo, 0 )

        main()

def robot_1():
        print( "200 deg" )
        pwm.set_servo_pulsewidth( myservo, 500 ) ;
        time.sleep( 1 )

        print( "r3re deg" )
        pwm.set_servo_pulsewidth( myservo, 1250 ) ;
        time.sleep( 1 )

        print( "18fergfr deg" )
        pwm.set_servo_pulsewidth( myservo, 2000 ) ;
        time.sleep( 1 )

        # turning off servo
        pwm.set_PWM_dutycycle( myservo, 0 )
        pwm.set_PWM_frequency( myservo, 0 )

        main()

def button_led():
    while True:
        if button.is_pressed:
            led.toggle()
            time.sleep(0.5)
            if random.randint(1,2) == 1:
                robot()
            else:
                robot_1()

def main():
    button_led()

if name == 'main':  # code to execute if called from command-line
        main()