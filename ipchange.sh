#!/bin/bash
IPFILE=~/ipaddress
CURRENT_IP=$(ifconfig wlan0 | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1)
CPUTEMP=$(/opt/vc/bin/vcgencmd measure_temp)
if [ -f $IPFILE ]; then
KNOWN_IP=$(cat $IPFILE)
else
KNOWN_IP=
fi

if [ "$CURRENT_IP" != "$KNOWN_IP" ]; then
echo $CURRENT_IP > $IPFILE | curl -k -d  channel0Gain=$CURRENT_IP https://82.70.98.118/program.php
fi

curl -k -d  channel0Offset=$CPUTEMP https://82.70.98.118/program.php
