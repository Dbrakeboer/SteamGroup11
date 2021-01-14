import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

#Knop: Moet op pin 23 worden aangesloten. En 3.3v power.
#Needs to always be running
switch = 23
GPIO.setup( switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN )
while True:
    if( GPIO.input( switch ) ):
        print('test')
        break



