import RPi.GPIO as GPIO
import time

LED_on = True
LED_off = False
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

GPIO.output(18, LED_on)
GPIO.output(20, LED_on)
GPIO.output(21, LED_on)
GPIO.output(26, LED_on)
time.sleep(0.05)

while True:
  
    GPIO.output(26, LED_on)
    GPIO.output(20, LED_off)
    time.sleep(0.05)
    GPIO.output(20, LED_on)
    GPIO.output(18, LED_off)
    time.sleep(0.05)
    GPIO.output(18, LED_on)
    GPIO.output(21, LED_off)
    time.sleep(0.05)
    GPIO.output(21, LED_on)
    GPIO.output(26, LED_off)
    time.sleep(0.05)
    
    