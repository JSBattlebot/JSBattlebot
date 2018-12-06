#These are imported commands from libraries
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

#This is where the motors are connected
motor1A = 23
motor1B = 24
motor2A = 27
motor2B = 17

GPIO.setmode(GPIO.BCM)

#This sets the pins as output
GPIO.setup(motor1A, GPIO.OUT)
GPIO.setup(motor1B, GPIO.OUT)
GPIO.setup(motor2A, GPIO.OUT)
GPIO.setup(motor2B, GPIO.OUT)

sleep(2)

#This makes the motors spin
#Pins is set to default that it puts out a high signal, to turn off
#put all to high.
def forward():
    GPIO.output(motor1A, GPIO.HIGH)
    GPIO.output(motor1B, GPIO.LOW)
    GPIO.output(motor2A, GPIO.HIGH)
    GPIO.output(motor2B, GPIO.LOW)
    
def back():
    GPIO.output(motor1A, GPIO.LOW)
    GPIO.output(motor1B, GPIO.HIGH)
    GPIO.output(motor2A, GPIO.LOW)
    GPIO.output(motor2B, GPIO.HIGH)
    
def stop():
    GPIO.output(motor1A, GPIO.HIGH)
    GPIO.output(motor1B, GPIO.HIGH)
    GPIO.output(motor2A, GPIO.HIGH)
    GPIO.output(motor2B, GPIO.HIGH)

forward()
