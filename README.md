Write the raspian to the sd-card:

# dd bs=4M if=2019-04-08-raspbian-stretch.img of=/dev/sde conv=fsync

When the command is done, run the sync command twice

# sync
# sync

Insert the flash-card and boot the raspberry bi, log in with username: pi and password: raspberry

Setup the rasperry as you normally would. (Timezone, Network, password and so on).

If you need to rotate the screen you have to add "display_rotate=N" to /boot/config.txt where

0: 0 degrees rotation
1: is 90 degrees rotation
2: is 180 degrees rotation
3: is 270 degrees rotation

Reboot afterwards

You probably wants to enable ssh as well, run raspi-config as root, select, "5 Interfacing Options"
and select "P2 SSH" and answer yes. 

To obtain the ip, run : ip a|grep inet


Install packages: 
# apt-get update
# apt-get install python-webkit python-webkit-dev git vim

Clone git repo

# cd /opt
# git clone https://github.com/Mikjaer/raspian-signage.git
# cp raspian-signage/Xsession /etc/X11/Xsession
# chmod +x raspian-signage/browser.py

edit /home/pi/browser.py and change the url to the desired website

# reboot


