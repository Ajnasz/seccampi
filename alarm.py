#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|-|S|p|y|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# pir_1.py
# Detect movement using a PIR module
#
# Author : Matt Hawkins
# Date	 : 21/01/2013
 
# Import required Python libraries
import RPi.GPIO as GPIO
import time
import os
 
# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
 
# Define GPIO to use on Pi
GPIO_PIR = 7
 
print("PIR Module Test (CTRL-C to exit)")
 
# Set pin as input
GPIO.setup(GPIO_PIR,GPIO.IN)			# Echo
 
current_State = 0
Previous_State = 0
last_img = 0


import PicUploader
import ImageCreator


imageCreator = ImageCreator.ImageCreator()
picUploader = PicUploader.PicUploader()

try:
 
	print("Waiting for PIR to settle ...")
 
	# Loop until PIR output is 0
	while GPIO.input(GPIO_PIR)==1:
		current_State	= 0
 
	print("	Ready")
 
	# Loop until users quits with CTRL-C
	while True :

		# Read PIR state
		current_State = GPIO.input(GPIO_PIR)

		if current_State==1 and Previous_State==0:
			# PIR is triggered
			print("	Motion detected!")

			fn = imageCreator.createImage()
			if (fn != ''):
				picUploader.upload(fn)

			Previous_State=1

		elif current_State==0 and Previous_State==1:
			# PIR has returned to ready state
			print("	Ready")
			Previous_State=0

		# Wait for 10 milliseconds
		time.sleep(0.01)
	 
except KeyboardInterrupt:
	print("	Quit")
	# Reset GPIO settings
	GPIO.cleanup()
