#!/usr/bin/python

import RPi.GPIO as G # reference the GPIO library
G.setmode(G.BCM)     # use the 'BCM' numbering scheme for the pins
G.setup(14, G.OUT)   # Set pin 14 as an Output
G.output(14, True)   # Turn it on
raw_input('Press return to exit')
G.cleanup()          # Tidy up after ourselves so we don't generate warnings next time we run this
