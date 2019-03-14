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

angles = numpy.arange(-90, 100, 10)
xReals = []
yReals = []
def readAngle():
    acc_x, acc_y, acc_z = sensorCompass.acceleration
    acc_z -= 0.74
    
    if acc_x >= 0:
        angle_x = numpy.arcsin(acc_x/9.33) * 180/numpy.pi
    else:
        angle_x = numpy.arcsin(acc_x/9.63) * 180/numpy.pi
        
    if acc_y >=0:
        angle_y = numpy.arcsin(acc_y/9.64) * 180/numpy.pi
    else:
        angle_y = numpy.arcsin(acc_y/9.46) * 180/numpy.pi
#        angle_x = numpy.arcsin(acc_x/9.81) * 180/numpy.pi
#        angle_y = numpy.arcsin(acc_y/9.81) * 180/numpy.pi
        
    if math.isnan(angle_y): angle_y = 90 * (acc_y/abs(acc_y))
    if math.isnan(angle_x): angle_x = 90 * (acc_x/abs(acc_x))
    
    return angle_x, angle_y
#        print(numpy.arcsin(0))

for i in angles:
    input("Place car at " + str(i) + " degrees in x and press enter...")
    xReals.append((i, readAngle()[0]))

for i in angles:
    input("Place car at " + str(i) + " degrees in y and press enter...")
    yReals.append((i, readAngle()[1]))
    
    
with open('outputfile.txt', 'w') as f:
    for item in xReals:
        f.write("%s\n" % str(item))
    for item in yReals:
        f.write("%s\n" % str(item))
        
def plot(angles, xReals, yReals):
    xAngles = [x[1] for x in xReals]
    yAngles = [y[1] for y in yReals]
    plt.plot(angles, xAngles, label="x")
    plt.plot(angles, yAngles, label="y")
    plt.show()

plot(angles, xReals, yReals)