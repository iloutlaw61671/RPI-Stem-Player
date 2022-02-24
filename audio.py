from pygame import mixer 
import RPi.GPIO as gpio
import pygame
import BlynkLib
import sys
 
gpio.setmode(gpio.BCM) 
gpio.setup(26, gpio.OUT)

gpio.setup(6, gpio.OUT)

gpio.setup(5, gpio.OUT)

gpio.setup(16, gpio.OUT)


auth=sys.argv[1]
aud1=sys.argv[2]
aud2=sys.argv[3]
aud3=sys.argv[4]
aud4=sys.argv[5]
aud5=sys.argv[6]
                 #Receiving authentication token preferred audio files as arguments
blynk=BlynkLib.Blynk(auth)

print(auth)
print(aud1)
print(aud2)
mixer.init()
pygame.init()  #initializing pygame

vocals=mixer.Sound(aud1)
bass=mixer.Sound(aud2)
drums=mixer.Sound(aud3)
synth=mixer.Sound(aud4)
other=mixer.Sound(aud5)

                     #assigning stems to variables

vocals.play()
bass.play()
drums.play()
synth.play()
other.play()
@blynk.VIRTUAL_WRITE(1)
def my_write_handler(value):         #Blynk write handler called when state is changed
	if value[0]=='1':
		vocals.set_volume(0)
		print('value is 1')
		gpio.output(26, 1) 
	elif value[0]=='0':
		vocals.set_volume(1)
		print("value is 0")
		gpio.output(26, 0)  

@blynk.VIRTUAL_WRITE(2)
def my_write_handler(value):
	if value[0]=='1':
		bass.set_volume(0)
		gpio.output(6, 1)		              

	elif value[0]=='0':
		bass.set_volume(1)
		gpio.output(6, 0)		 

@blynk.VIRTUAL_WRITE(3)
def my_write_handler(value):
	if value[0]=='1':
		drums.set_volume(0)
		gpio.output(5, 1)
	elif value[0]=='0':
		drums.set_volume(1)
		gpio.output(5, 0)

@blynk.VIRTUAL_WRITE(4)
def my_write_handler(value):
	if value[0]=='1':
		synth.set_volume(0)
		gpio.output(16, 1)
	elif value[0]=='0':
		synth.set_volume(1)
		gpio.output(16, 0) 
while True:
	blynk.run()                    #Run till stopped
