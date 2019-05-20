from gpiozero import LED
import RPi.GPIO as GPIO
import time

#GPIO Setup
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

#LED Setup
led = LED(18)

def callback(channel):
    if GPIO.input(channel):
        print("water has been detected")
        led.on()
        time.sleep(.5)
        led.off()
        
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300) #let us know when pin is HIGH or Low
GPIO.add_event_callback(channel, callback) #assigns function to pin 21 and runs function

#forever loop
while True:
    time.sleep(1)