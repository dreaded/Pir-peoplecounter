## Pir-peoplecounter
**A project for counting people using a Raspberry pi and a passive infrared sensor.**

The heritagehackers was tasked with creating a people counter for use in Rochdale Touchstones art gallery, with the goal of counting the total vistors to the gallery each day.

I searched for exisiting projects and found [this project](http://blog.ubidots.com/building-a-people-counter-with-raspberry-pi-and-ubidots)

The project seemed to suits our needs, So we set about building it.

Having built the project a number of issues arose. Temporally losss of internet conectivity resulted in the program crashing.

Some method of keeping the script running was needed. I chose a program called ´forever´ which is installed as follows:

First intall the npm package manager.

> sudo apt-get install npm

followed by forever  

> sudo npm install forever -g

To run the peoplecount program at startup i wrote a small script and called it startup.sh

> \#!/bin/bash
> PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/pi
> /usr/local/bin/forever start -c /usr/bin/python /home/pi/peoplecount.py

This script is called by cron at startup of the system.

Add the script to crontab

> sudo crontab -e

Choose a text editor to use.

Add the following line

> @reboot sh /home/pi/startup.sh

Make the script executable

> sudo chmod +x /home/pi/startup.sh

If all has gone well the script will run at system boot. Forever will restart the peoplecount program in the event of a crash.

Our particular installation caused some trouble. The network we would connect the raspberry pi to required the user to input a email address into a captive portal page and click ok. Furthermore the ip lease was for only 24 hours. Connecting a keyboard and monitor everyday did not appeal! A solution was sought.

I first downloaded the captive portal page 

> wget http://somewebsite.tld

Then fed this into a perl script called formfind.pl. formfind identifys the the web page the the completed form is sent to and also the form fields.

> perl formfind.pl  < \<the web page you just downloaded>

Typical out put would be like.

> --- FORM report. Uses POST to URL "https://www.feedburner.com/fb/a/emailverify"
> Input: NAME="email" (EMAIL)
> Input: NAME="url" VALUE="https://feeds.feedburner.com/~e?ffid=1892871" (HIDDEN)
> Input: NAME="title" VALUE="FormSmarts Updates" (HIDDEN)
> Input: NAME="loc" VALUE="en_US" (HIDDEN)
> Button: "Subscribe" (SUBMIT)
> --- end of FORM

To submit the form data i used cURL which is present on most linux machines. If not

> sudo apt-get install curl

Submitting for example an email address

> curl -d email=someone@somehost.tld https://www.feedburner.com/fb/a/emaillverify

I verified the above command worked, of course subsituting the above data with data relevent to our situation.

I needed the command to run at system boot and at regular intervals as i could never be sure exaclty when the ip lease would expire.

To run at system boot i added

> curl -d email=someone@somehost.tld https://www.feedburner.com/fb/a/emaillverify

to a file i called autostart and moved it to the if-up.d directory located in /etc/network

Scripts in this directory are run after a network inteface is brought up.
I discovered that a delay was neeeded for the curl command to work. The final script is

> \#!bin/bash
> /bin/sleep 20
> curl -d email=someone@somehost.tld https://www.feedburner.com/fb/a/emaillverify

make it executable

> sudo chmod +x autostart




