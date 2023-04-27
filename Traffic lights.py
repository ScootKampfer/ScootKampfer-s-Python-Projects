import RPi.GPIO as GPIO
import time

LED_on = True
LED_off = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

while True:
    
    while GPIO.input(13) == False:
    
        GPIO.output(20, LED_off)
    GPIO.output(21, LED_on)
    time.sleep(1)
    GPIO.output(21, LED_off)
    GPIO.output(26, LED_on)
    time.sleep(1)
    GPIO.output(26, LED_off)
    GPIO.output(20, LED_on)
    time.sleep(1)
    
    if GPIO.input(13) == True:
    
        break
