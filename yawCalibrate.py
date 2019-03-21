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
#sensorCompass.mag_rate = adafruit_lsm303.MAGRATE_220


angles = numpy.arange(0, 370, 10)
headings = []
def readAngle():
        headingsForAv = []
        counter = 0
        while counter < 100:
            mag_x, mag_y, mag_z = sensorCompass.magnetic
            heading = (180/numpy.pi) * numpy.arctan2(mag_y, mag_x)
            if (heading < 0):
                    heading += 360
            headingsForAv.append(heading)
            counter += 1
        return numpy.mean(headingsForAv)
    


for i in angles:
    input("Place car at " + str(i) + " degrees and press enter...")
    headings.append(readAngle())


    
    
with open('outputfile.txt', 'w') as f:
    for item in headings:
        f.write("%s\n" % str(item))

def plot(angles, headings):
    plt.plot(angles, headings, label="heading")
    plt.legend()
    plt.show()

plt.plot(angles, headings)
plt.show()