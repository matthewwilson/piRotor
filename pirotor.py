from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

#servo_min = set_servo_pulse(0,106)

print('Arming motor')
pwm.set_pwm(0,0,260)
time.sleep(5)
print('Starting motor at 300')
pwm.set_pwm(0,0,300)
time.sleep(3)
print('increasing to 360')
pwm.set_pwm(0,0,360)
time.sleep(3)
print('increasing to 400')
pwm.set_pwm(0,0,400)
time.sleep(3)
print('increasing to 450')
pwm.set_pwm(0,0,450)
time.sleep(3)
print('stopping')
pwm.set_pwm(0,0,260)
