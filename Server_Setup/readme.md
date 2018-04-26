# Setting up the Server

## Install lighttpd Server package:

`sudo apt-get install lighttpd`

`sudo service lighttpd start`

Set up a hompage by typing:

`cd /var/www/html`

Then create the HTML homapage using:

`sudo nano index.html`

Make sure to save that file in the **/var/www/html** folder. Point your browser to your IP Address of the PI to see if the server is setup.

To make sure the server can run the python script use:

`sudo chmod 755 /var/www/html/pythonfile.py`

## Install the Python Web Server interpreter:

`sudo apt-get -no-install-recommended install python-flup`

Now you can save your python scripts to **/var/www/html** in order to run them remotely. You will also need to adjust your scripts to run from the server not from a local script. Check the example in the RPI_3 folder.

To set up permissions properly:

```
ls -l /usr/bin/python
sudo cp /usr/bin/python2.7 /usr/bin/pythonRoot
sudo chmod u+s /usr/bin/pythonRoot
ls -l /usr/bin/pythonRoot
sudo nano /etc/lighttpd/lighttpd.conf
```

Add this line to **server.modules=()**:

`"mod_fastcgi",`

Add this to the end of the file:

```
fastcgi.server = (
   ".py" => (
     "python-fcgi" => (
       "socket" => "/tmp/fastcgi.python.socket",
       "bin-path" => "/var/www/html/Server_LED_Test.py",
       "check-local" => "disable",
       "max-procs" => 1)
    )
 )
```

**CTRL+X** to Exit and use Y to save changes upon exiting.

Restart the server:

`sudo service lighttpd restart`
