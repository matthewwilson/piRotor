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

motor1.arm()

# def getPWMValueFromNanoseconds(nanoseconds):
#     print(nanoseconds)
#     pwmValue = nanoseconds / (1000000.0/4096.0/60.0)
#     return int(round(pwmValue))
#
# def armMotor():
#     print('Arming motor')
#     pwm.set_pwm(0,0,260)
#     pwm.set_pwm(1,0,260)
#     pwm.set_pwm(14,0,260)
#     pwm.set_pwm(15,0,260)
#     time.sleep(5)
#
# def stopMotor():
#     print("Stopping")
#     pwm.set_pwm(0,0,260)
#     pwm.set_pwm(1,0,260)
#     pwm.set_pwm(14,0,260)
#     pwm.set_pwm(15,0,260)
#
# def simpleMotorExample():
#     print('Starting motor at 300')
#     pwm.set_pwm(0,0,300)
#     time.sleep(3)
#     print('increasing to 360')
#     pwm.set_pwm(0,0,360)
#     time.sleep(3)
#     print('increasing to 400')
#     pwm.set_pwm(0,0,400)
#     time.sleep(3)
#     print('increasing to 450')
#     pwm.set_pwm(0,0,450)
#     time.sleep(3)
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
# def calibrateThrottle():
#     print("Disconnect power from ESC, leave connected to PWM hat")
#     time.sleep(5)
#     print("Setting throttle to highest position, please connect power to ESC")
#     pwm.set_pwm(0,0,457)
#     time.sleep(10)
#     print("The motor should produce a series of initialization beeps increasing in pitch, followed by another beep matching the pitch of the last initialization beep.")
#     raw_input("Press enter once initialization beeps finish")
#     print("Moving throttle to lowest position, two beeps of the same pitch should be emitted, followed by higher pitched long beep")
#     pwm.set_pwm(0,0,261)
#     raw_input("Press enter after the beeps")
#     print("ESC exiting calibration mode")
#     print("ESC should arm and produce a higher pitched long beep")
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
