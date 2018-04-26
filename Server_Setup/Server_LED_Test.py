#!/usr/bin/pythonRoot

# bring in the libraries
import RPi.GPIO as G     
from flup.server.fcgi import WSGIServer 
import sys, urlparse

# set up our GPIO pins
G.setmode(G.BCM)
G.setup(14, G.OUT)

# all of our code now lives within the app() function which is called for each http request we receive
def app(environ, start_response):
  # start our http response 
  start_response("200 OK", [("Content-Type", "text/html")])
  # look for inputs on the URL
  i = urlparse.parse_qs(environ["QUERY_STRING"])
  yield ('&nbsp;') # flup expects a string to be returned from this function
  # if there's a url variable named 'q'
  if "q" in i:
    if i["q"][0] == "w": 
      G.output(14, True)   # Turn it on
    elif i["q"][0] == "s":
      G.output(14, False)  # Turn it off

#by default, Flup works out how to bind to the web server for us, so just call it with our app() function and let it get on with it
WSGIServer(app).run()
