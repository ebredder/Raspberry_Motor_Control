#!/usr/bin/python

import RPi.GPIO as G     # reference the GPIO library
G.setmode(G.BCM)         # use the 'BCM' numbering scheme for the pins
G.setup(14, G.OUT)       # Set pin 18 as an Output
while (True):            # keep going around this loop until we're told to quit
  key = raw_input("Enter 'w' for On, 's' for Off and any other key to quit. You'll need to press enter after each character: ")
  if key == "w": 
    G.output(14, True)   # Turn it on
  elif key == "s":
    G.output(14, False)  # Turn it off
  else:
    break                # leave our loop
G.cleanup()              # Tidy up after ourselves so we don't generate warnings next time we run this
