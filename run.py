#essential libraries
import RPi.GPIO as GPIO
from time import sleep, strftime
#Seperate py scripts for sensor readouts.
from thermtest import *

#sensor libraries

#GPIO declare
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

#schedule options
morning_water = "08:00AM"
sensorchecks = True
midday_sensorcheck = "02:00PM"
night_water = "08:00PM"

#printout dont touch
stout = ["Morning: ","Midday Check: ","Night: "]
sout = [morning_water,midday_sensorcheck,night_water]

#debug options
dotest = False;
reset_gpio = False;

#main function takes time on device as cue to send signal to relay
#check state of sensors to decide how long program should run
def main():
    print(strftime("%I:%M%p"))
    print("Waiting For Schedule")
    timewait()
    s = [None]
    # append sensors to s array
    s.append(gettemp())
    print(s)
    #decide how long pump should remain on
    wt = watertime(s)
    print("Watering for "+ str(wt)+ " minutes")
    water(wt)
    print("Cycle Complete")
    main()


def test():
    tick = 0;
    while True:
        GPIO.output(11,1);
        sleep(10);
        GPIO.output(11,0);
        sleep(5);
        tick+=1;
        print(tick);
        if(reset_gpio == True):
            GPIO.cleanup()

def timewait():
    #wait till time of day is reached then check sensors or commence watering
    night = False
    while True:
        hour = strftime("%I:%M%p")
        #Check for day schedule
        if hour == morning_water:
            print("Schedule Match")
            break
        #Check for midday sensor read to determine if more watering is needed at night
        elif hour == midday_sensorcheck and sensorchecks == True:
            print("Midday Sensor Check")
            t = gettemp()
            if t >= 70:
                night = True
            sleep(60)
        #Check for night schedule and permission
        elif hour == night_water:
            print("Schedule Match")
            if night == True:
                break
            else:
                print("Skip Night Watering")
        else:
            sleep(30)

def watertime(s):
    #t in minutes, multiply 60 for seconds for use with time.sleep
    t = 5
    p = 0
    #if temp reads above 70 in the morning, then double watering time.
    if s[1] > 70:
        p=2
    else:
        p=1
    return t*p
    #using sensor info decide watering duration using a point system 'p' to multiply the default daily watering time.

def water(time):
    print("start pump")
    limit = time*60
    GPIO.output(11,1)
    sleep(limit)
    print("stop pump")
    GPIO.output(11,0)



#main loop start
try:
    a=0
    for i in stout:
       print(i+sout[a])
       a+=1
    if(dotest == True):
        test();
    else:
        GPIO.output(11,0)
        main();
except:
    print("error "+str(errcode))


