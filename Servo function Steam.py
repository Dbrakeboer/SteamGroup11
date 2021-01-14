import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

print( "servo wave" )

def pulse( pin, delay1, delay2 ):
   # copieer hier je implementatie van de pulse functie
   GPIO.output( pin, GPIO.HIGH )
   time.sleep( delay1 )
   GPIO.output( pin, GPIO.LOW )
   time.sleep( delay2 )


def spinServo():
    def servo_pulse( pin_nr, position ):
       def pulse( pin, delay1, delay2 ):
           GPIO.output( pin, GPIO.HIGH )
           time.sleep( delay1 )
           GPIO.output( pin, GPIO.LOW )
           time.sleep( delay2 )
       
       pos = (0.5/1000) + (position/50000)
       print(pos)
       pulse(pin_nr, pos , 0.01)
       
    delay = 0.1
    delay_offset = 0.02 

    servo = 25
    GPIO.setup( servo, GPIO.OUT )
    while True:
       for i in range( 0, 100, 1 ):
          servo_pulse( servo, i )
       time.sleep(delay - delay_offset)
       for i in range( 100, 0, -1 ):
          servo_pulse( servo, i )
       time.sleep(delay - delay_offset)

spinServo()
