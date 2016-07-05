from __future__ import division
from motor import Motor

import time
# Import the PCA9685 module.
import Adafruit_PCA9685


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

motor1 = Motor(0, pwm)
motor2 = Motor(1, pwm)
motor3 = Motor(14, pwm)
motor4 = Motor(15, pwm)

def getPWMValueFromNanoseconds(nanoseconds):
    print(nanoseconds)
    pwmValue = nanoseconds / (1000000.0/4096.0/60.0)
    return int(round(pwmValue))

def armMotors():
    print('Arming motors')
    motor1.arm()
    motor2.arm()
    motor3.arm()
    motor4.arm()
    time.sleep(5)

def stopMotors():
    print("Stopping")
    motor1.stop()
    motor2.stop()
    motor3.stop()
    motor4.stop()

def calibrateThrottles():
    motor1.calibrateThrottle()
    motor2.calibrateThrottle()
    motor3.calibrateThrottle()
    motor4.calibrateThrottle()

def setPwmForAllMotors(pwmValue):
    motor1.setPwmValue(self, pwmValue)
    motor2.setPwmValue(self, pwmValue)
    motor3.setPwmValue(self, pwmValue)
    motor4.setPwmValue(self, pwmValue)

def simpleExample():
    print('Starting motors at 300')
    setPwmForAllMotors(300)
    time.sleep(3)
    print('increasing to 360')
    setPwmForAllMotors(360)
    time.sleep(3)
    print('increasing to 400')
    setPwmForAllMotors(400)
    time.sleep(3)
    print('increasing to 450')
    setPwmForAllMotors(450)
    time.sleep(3)

armMotors()

time.sleep(5)
simpleExample()

stopMotors()


#
# def motorRangeExample():
#     for x in range(1060, 1861):
#         pwmValue  = getPWMValueFromNanoseconds(x)
#         print("increasing to %d" % (pwmValue))
#         pwm.set_pwm(0,0,pwmValue)
#         pwm.set_pwm(1,0,pwmValue)
#         pwm.set_pwm(14,0,pwmValue)
#         pwm.set_pwm(15,0,pwmValue)
#         #time.sleep(1)
#

#
# def manualControl():
#     exit = False
#     pwmValue = 261
#     print("Press i to increase speed, d to decrease, q to quit")
#     while not(exit):
#         action = raw_input()
#
#         if action == "i":
#             pwmValue+=1
#         elif action == "d":
#             pwmValue-=1
#         elif action == "q":
#             exit = True
#
#         print(pwmValue)
#
#         if not(exit):
#             pwm.set_pwm(15,0,pwmValue)
#
# armMotor()
# motorRangeExample()
# #time.sleep(5)
# #simpleMotorExample()
# #manualControl()
# stopMotor()


#calibrateThrottle()
