# Pir-peoplecounter
A project for counting people using a Raspberry pi and a passive infrared sensor.

The heritagehackers was tasked with creating a people counter for use in Rochdale Touchstones museum, with the goal of counting the total vistors to the museum.

I searched for exisiting projects and found http://blog.ubidots.com/building-a-people-counter-with-raspberry-pi-and-ubidots

The project seemed to suits our needs, So we set about building it.

Having built the project a number of issues arose. Temporally losss of internet conectivity resulted in the program crashing.

Some method of keeping the script running was needed. I choose a program called ´forever´ which i installed as follows:

first i intalled the npm package manager ¨sudo apt-get install npm¨ followed by the forever program ¨sudo npm install forever -g¨ 
