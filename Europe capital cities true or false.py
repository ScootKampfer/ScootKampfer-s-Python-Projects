import RPi.GPIO as GPIO
import time

answer = 0

LED_on = True
LED_off = False
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.IN)
GPIO.setup(26, GPIO.IN)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

GPIO.output(18, LED_off)
GPIO.output(20, LED_off)
GPIO.output(21, LED_off)
GPIO.output(23, LED_off)

print('Are you ready to play? (1 for yes, 2 for no)') and wait

if answer == '1':
    
    print('ok')