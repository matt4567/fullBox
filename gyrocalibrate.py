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
time.sleep(10)
print("starting")
while counter < 1000:
        mag_x, mag_y, mag_z = sensorCompass.magnetic
        gyro_x, gyro_y, gyro_z = sensorGyro.gyro
        acc_x, acc_y, acc_z = sensorCompass.acceleration
       # acc_x += 0.52
       # acc_y -= 0.37
        #acc_z -= 0.74
        accsX.append(gyro_x)
        accsY.append(gyro_y)
        accsZ.append(gyro_z)
#        print(accs[-1])
        counter += 1
       
            
        
print(numpy.mean(accsX), numpy.mean(accsY), numpy.mean(accsZ))
plt.plot(accsX, label = "x")
plt.plot(accsY, label = "y")
plt.plot(accsZ, label="z")
plt.legend()
plt.show()
