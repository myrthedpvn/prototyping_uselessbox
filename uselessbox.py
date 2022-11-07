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
#myservo_2 = 16
pwm = pigpio.pi()
pwm.set_mode(myservo, pigpio.OUTPUT)
pwm.set_PWM_frequency(myservo, 50)
#pwm.set_mode(myservo_2, pigpio.OUTPUT)
#pwm.set_PWM_frequency(myservo_2, 50)


def robot():
        print( "0 deg servo 1" )
        pwm.set_servo_pulsewidth( myservo, 500 ) ;
        time.sleep( 2 )
        led.toggle()
        pwm.set_PWM_dutycycle( myservo, 0 )
        pwm.set_PWM_frequency( myservo, 0 )
        main()



#def robot_knop():
        print( "200 deg servo_2" )
        pwm.set_servo_pulsewidth( myservo_2, 500 ) ;
        time.sleep( 2 )

        print( "r3re deg servo_2" )
        pwm.set_servo_pulsewidth( myservo_2, 1250 ) ;
        time.sleep( 2 )

        print( "18fergfr deg servo_2" )
        pwm.set_servo_pulsewidth( myservo_2, 2000 ) ;
        time.sleep( 2 )
        led.toggle()
        pwm.set_servo_pulsewidth( myservo_2, 500 ) ;
        time.sleep(2)
        pwm.set_servo_pulsewidth( myservo, 500 ) ;

        # turning off servo
        pwm.set_PWM_dutycycle( myservo_2, 0 )
        pwm.set_PWM_frequency( myservo_2, 0 )
        pwm.set_PWM_dutycycle( myservo, 0 )
        pwm.set_PWM_frequency( myservo, 0 )


        main()


def button_led():
    while True:
        if button.is_pressed:
            print('button is pressed')
            led.toggle()
            time.sleep(0.5)
            robot()
def main():
    button_led()

if name == 'main':  # code to execute if called from command-line
        main()
