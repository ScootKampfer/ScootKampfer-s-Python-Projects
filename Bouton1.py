import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.IN)
GPIO.setup(20, GPIO.OUT)

GPIO.output(20, False)

while True:
    
    if GPIO.input(13):
        
        GPIO.output(20, False)
        
    else:
        
        GPIO.output(20, True)