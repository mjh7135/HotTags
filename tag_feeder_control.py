#!/usr/bin/env python3

import RPi.GPIO as GPIO
from time import sleep
from guizero import *
from gpiozero import Motor

##set for GPIO numbering
GPIO.setmode(GPIO.BCM)
##set input and ouputs
#GPIO.setup(GPIO pin, GPIO.OUT/GPIO.IN)

app = App()
num_tags = Text(app, text="1")

def push_tag():
  #set PWM
  #sleep
  pass

def retract():
  #set PWM
  #sleep
  pass

def reverse_motor():
  #if forward:
    #set motor speed
    #set direction to backward
  #elif backward:
    #set motor speed
    #set direction to forward
  pass

def increase_tags():
  count = int(num_tags.value) + 1
  num_tags.set(f"{count}")

def decrease_tags(sub):
  if num_tags.value =! 1:
    count = int(num_tags.value) - 1
    num_tags.set(f"{count}")

def shutdown():
  pass

def run():
  tag_count = int(num_tags.value)
  #disable buttons
  #start motor
  push_tag()
  reverse_motor()
  retract()
  #wait for sensor
  reverse_motor()
  for tag in range(1, tag_count):
    push_tag()
    reverse_motor()
    retract()
    #wait for sensor 
    reverse_motor()
  #stop motor
  #enable buttons
  pass

increase_by_1_button = PushButton(app, command=increase_tags, text="+1")
#increase_by_5_button = PushButton(app, command=increase_tags, text="+5")
#increase_by_10_button = PushButton(app, command=increase_tags, text="+10")
decrease_by_1_button = PushButton(app, command=decrease_tags, text="-1")
#decrease_by_5_button = PushButton(app, command=decrease_tags, text="-5")
#decrease_by_10_button = PushButton(app, command=decrease_tags, text="-10")

app.display()
