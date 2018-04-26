# Raspberry_Motor_Control

## Raspberry Pi 3
Make sure to start with Raspbian-Lite downloaded from: [Raspbian Stretch Lite](https://www.raspberrypi.org/downloads/raspbian/)

Boot into your terminal session:

U/N: `pi`

P/W: `raspberry`

To allow for SSH and Remote GPIO Control we must run this command:

`sudo raspi-config`

**Option 2: Network Options**
+ N2 - Wi-fi
+ Enter Country or leave blank
+ Enter the SSID for the network
+ Enter the passphrase if necessary

**Option 5: Interfacing Options**
+ P2 - SSH
+ Enable
+ P8 - Remote GPIO
+ Enable

**Exit** (TAB will allow you to switch menus)

Type:

`hostname -I`

Write down this IP address for SSH log in.

## Your computer...
Use an SSH software to communicate to the PI. Linux and Mac have this built in, if you are using Windows, the easiest way to get started is [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)

**Mac/Linux:**
+ In terminal emulator:
`ssh pi@[IP ADDRESS OF PI]`
+ Enter password to continue...

**PuTTY**
+ Type in the hostname into the blank area labeled Host Name (or IP Address)
+ Connection Type: SSH
+ Click Open to start you session
+ Enter the password to continue
+ If you need more help try [here](https://www.raspberrypi.org/documentation/remote-access/ssh/windows.md)

This should get you started with the remote communication to the Raspberry Pi!
