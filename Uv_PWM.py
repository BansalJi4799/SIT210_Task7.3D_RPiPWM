# Help us to comunicate with our GPIO pins
import RPi.GPIO as GPIO
# For time flexibility of our program - will be used to calculate the distance of the object
import time
# To perform mathematical operations
import math

# Set to BCM to use GPIO pin of the raspberry pi  
GPIO.setmode(GPIO.BCM)                                       

# Here we are defining the global pins for pins variables
HC_SR_ECHO = 14
HC_SR_TRIG = 15
LED = 18

# Set the warning to false to avoid any unecessary warnings
GPIO.setwarnings(False)

#  set the trig pin to output
GPIO.setup(HC_SR_TRIG, GPIO.OUT)
#  echo pin to input
GPIO.setup(HC_SR_ECHO, GPIO.IN)
#  set the led to output
GPIO.setup(LED, GPIO.OUT)

#  created instance of pwn and passed led in it and also pass the frequecy with it
Pulse = GPIO.PWM(LED, 75)
#  here we have initialized the pinb 
Pulse.start(0)

# Calculate the distance of the object
def Object_Distance():
    # set trig pin to high
    GPIO.output(HC_SR_TRIG, True)
    time.sleep(0.00001)
    GPIO.output(HC_SR_TRIG, False)

#  here echo pin is used to record the starting and ending time of the wave 
    while GPIO.input(HC_SR_ECHO) == False:
        Start_Time = time.time()

    while GPIO.input(HC_SR_ECHO) == True:
        End_Time = time.time()

    #  time duration to the pulse to return back
    Time_Duration = End_Time - Start_Time

    #  calculating the distance = speed * time
    #  (duration * speed of sound in air)/2 = (duration * 34300)/2
    distance = Time_Duration * 17150
 
    return distance

# 
def Led_Pulse(dist):
    if dist < 100:
        # width of the pulse
        # rounds a number UP to the nearest integer, if necessary, and returns the result.
        Pulse.start(math.ceil(100 - dist))
    else:
        Pulse.start(0)
    time.sleep(1)

try:
    # this is our loop
  while True:
    #  here we taker the distance from the sensor
    distance = Object_Distance()
    # check the distance on our seriual monitor
    print(distance)
    Led_Pulse(distance)

except KeyboardInterrupt:
    GPIO.cleanup()