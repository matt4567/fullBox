import numpy
import math
import time
import board
import busio
import adafruit_l3gd20
import adafruit_lsm303
import matplotlib.pyplot as plt

outf = open('output.txt', 'a')
outf.truncate(0)

# Hardware I2C setup:
I2C = busio.I2C(board.SCL, board.SDA)
sensorGyro = adafruit_l3gd20.L3GD20_I2C(I2C)
sensorCompass = adafruit_lsm303.LSM303(I2C)
sensorCompass.mag_rate = adafruit_lsm303.MAGRATE_220

headings = []
counter = 0
time.sleep(10)
print("starting")
angles = numpy.arange(-90, 100, 10)
while counter < 1000:
        mag_x, mag_y, mag_z = sensorCompass.magnetic
       # acc_x += 0.52
       # acc_y -= 0.37
        #acc_z -= 0.74
#        print(accs[-1])
		heading = (180/numpy.pi) * numpy.arctan2(mag_y, mag_x)
        if (heading < 0):
            heading += 360
        headings.append(heading)
        counter += 1
        
       
            
        
print(numpy.mean(heading))
plt.plot(headings, label = "heading")
plt.legend()
plt.show()


import numpy
import math
import time
import board
import busio
import adafruit_l3gd20
import adafruit_lsm303
import matplotlib.pyplot as plt

outf = open('output.txt', 'a')
outf.truncate(0)

# Hardware I2C setup:
I2C = busio.I2C(board.SCL, board.SDA)
sensorGyro = adafruit_l3gd20.L3GD20_I2C(I2C)
sensorCompass = adafruit_lsm303.LSM303(I2C)
sensorCompass.mag_rate = adafruit_lsm303.MAGRATE_220

accsX = []
accsY = []
accsZ = []
counter = 0

angles = numpy.arange(-10, 10, 10)
headings = []
yReals = []
def readAngle():
	mag_x, mag_y, mag_z = sensorCompass.magnetic
	heading = (180/numpy.pi) * numpy.arctan2(mag_y, mag_x)
	if (heading < 0):
		heading += 360
		
	return heading
    


for i in angles:
    input("Place car at " + str(i) + " degrees and press enter...")
    xReals.append((i, readAngle()))


    
    
with open('outputfile.txt', 'w') as f:
    for item in headings:
        f.write("%s\n" % str(item))

def plot(angles, xReals, yReals):
    heading = [x[1] for x in headings]
    plt.plot(angles, heading, label="heading")
    plt.show()

plot(angles, xReals, yReals)