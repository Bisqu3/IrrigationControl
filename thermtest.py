from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()

def gettemp():
        temp = sensor.get_temperature()
        print("Temp requested")
        return round((temp*1.8)+32,2)

