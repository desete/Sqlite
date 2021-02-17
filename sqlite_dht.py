from time import sleep
import Adafruit_DHT
import sqlite3
import datetime

sensor = Adafruit_DHT.DHT11

#pin fo DHT11
pin = 24

run = True
while run:
    #connect Database
    conn = sqlite3.connect('Sqlite_DHT.sqlite3') 
    print("Connect Database")
    c = conn.cursor()
    
    #Get data from DHT11
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    
    #Get Date now
    daye = datetime.datetime.now()
    sleep(0.5)
    
    if humidity is not None and temperature is not None:
	print('Temep={0:0.1f}*C  Humidity={1:0.1f}% '.format(temperature, humidity))
        
       	#Insert Data in 'data' Table
        c.execute("INSERT INTO data (Temperature,Humidity,Date) \
		VALUES ({},{},'{}')".format(temperature,humidity,daye))
        sleep(0.1)
        
        #Write Changes
	conn.commit()  
    else:
	print('Failed to get reading. Try again!')	
	sleep(10)
    conn.close()


