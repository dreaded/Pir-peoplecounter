
from ubidots import ApiClient
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN) ## pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(10, GPIO.OUT)
try:

    api = ApiClient("")

    people = api.get_variable("")

except:

    print "Couldn't connect to the API, check your Internet connection"

counter = 0

peoplecount = 0

while(1):

    i=GPIO.input(8)

    if (i==True):
    
        peoplecount += 1
        
        GPIO.output(10,1)

        presence = 0

        time.sleep(1.5)

    time.sleep(1)

    counter += 1

    if(counter==5):

        print peoplecount

        people.save_value({'value':peoplecount})

        counter = 0

        peoplecount = 0

    GPIO.output(10,0)
