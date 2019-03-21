import numpy
import math
import time
import board
import busio
import adafruit_l3gd20
import adafruit_lsm303

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
while True:
        mag_x, mag_y, mag_z = sensorCompass.magnetic
        gyro_x, gyro_y, gyro_z = sensorGyro.gyro
        acc_x, acc_y, acc_z = sensorCompass.acceleration
       # acc_x += 0.52
       # acc_y -= 0.37
        acc_z -= 0.74
        accsX.append(acc_x)
        accsY.append(acc_y)
        accsZ.append(acc_z)
#        print(accs[-1])
#       counter += 1
        
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
#        print(numpy.arcsin(0))
#        print(acc_x, acc_y)
#        print(angle_x, angle_y)
#       time.sleep(1)

#        print(acc_x, acc_y, acc_z)
#        time.sleep(1)
        
#	print('Angular momenturm (rad/s): {}'.format(sensorGyro.gyro))
#	print('Magnetometer(gauss): ({0:10.3f}, {1:10.3f}, {2:10.3f}) '.format(mag_x, mag_y, mag_z))
#        if (mag_y != 0):
#		heading = (180/numpy.pi) * numpy.arctan2(numpy.array(mag_x),numpy.array(mag_y))
        heading = (180/numpy.pi) * numpy.arctan2(mag_y, mag_x)
        if (heading < 0):
            heading += 360
#        print(heading, mag_y, mag_x)
#        time.sleep(1)    
        timeStr = time.time()
            
        print(str(timeStr) + " " + str(gyro_x) + " " + str(gyro_y)+ " " + str(gyro_z) + " " + str(angle_y) + " " +
              str(angle_x) + " " + str(heading) + " " + str(acc_x) + " " + str(acc_y) + " " + str(acc_z))
        outf.write(str(timeStr) + " " + str(gyro_x) + " " + str(gyro_y)+ " " + str(gyro_z) + " " + str(angle_y) + " " +
              str(angle_x) + " " + str(heading) + " " + str(acc_x) + " " + str(acc_y) + " " + str(acc_z) + "\n")
        outf.flush()

#print(numpy.mean(accsX), numpy.mean(accsY), numpy.mean(accsZ))
