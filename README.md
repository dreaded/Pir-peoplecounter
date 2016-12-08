## Pir-peoplecounter
**A project for counting people using a Raspberry pi and a passive infrared sensor.**

The heritagehackers was tasked with creating a people counter for use in Rochdale Touchstones art gallery, with the goal of counting the total vistors to the gallary.

I searched for exisiting projects and found [this project](http://blog.ubidots.com/building-a-people-counter-with-raspberry-pi-and-ubidots)

The project seemed to suits our needs, So we set about building it.

Having built the project a number of issues arose. Temporally losss of internet conectivity resulted in the program crashing.

Some method of keeping the script running was needed. I choose a program called ´forever´ which is installed as follows:

First intall the npm package manager.

> sudo apt-get install npm

followed by the forever program 

> sudo npm install forever -g

To run the peoplecount program at startup i wrote a small script and called it startup.sh

> \#!/bin/bash
> PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/pi
> /usr/local/bin/forever start -c /usr/bin/python /home/pi/peoplecount.py

This script is called by cron at startup of the system.

This is achieved

