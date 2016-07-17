from __future__ import division
from motor import Motor
from pid import PID
from Adafruit_BNO055 import BNO055

import time
# Import the PCA9685 module.
import Adafruit_PCA9685


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Create and configure the BNO sensor connection.  Make sure only ONE of the
# below 'bno = ...' lines is uncommented:
# Raspberry Pi configuration with serial UART and RST connected to GPIO 18:
bno = BNO055.BNO055(serial_port='/dev/ttyAMA0', rst=18)

if not bno.begin():
    raise RuntimeError('Failed to initialize BNO055! Is the sensor connected?')

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

motor1 = Motor(0, pwm, 276,457)
motor2 = Motor(1, pwm, 276,457)
motor3 = Motor(14, pwm, 276,457)
motor4 = Motor(15, pwm, 276,457)

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
    motor1.setPwmValue(pwmValue)
    motor2.setPwmValue(pwmValue)
    motor3.setPwmValue(pwmValue)
    motor4.setPwmValue(pwmValue)

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

def manualControl():
    exit = False
    pwmValue = 261
    print("Press i to increase speed, d to decrease, q to quit")
    while not(exit):
        action = raw_input()

        if action == "i":
            pwmValue+=1
        elif action == "d":
            pwmValue-=1
        elif action == "q":
            exit = True

        print(pwmValue)

        if not(exit):
            setPwmForAllMotors(pwmValue)


def autonomousControl():

    # Print system status and self test result.
    status, self_test, error = bno.get_system_status()
    print('System status: {0}'.format(status))
    print('Self test result (0x0F is normal): 0x{0:02X}'.format(self_test))
    # Print out an error if system status is in error mode.
    if status == 0x01:
        print('System error: {0}'.format(error))
        print('See datasheet section 4.3.59 for the meaning.')

    # Print BNO055 software revision and other diagnostic data.
    sw, bl, accel, mag, gyro = bno.get_revision()
    print('Software version:   {0}'.format(sw))
    print('Bootloader version: {0}'.format(bl))
    print('Accelerometer ID:   0x{0:02X}'.format(accel))
    print('Magnetometer ID:    0x{0:02X}'.format(mag))
    print('Gyroscope ID:       0x{0:02X}\n'.format(gyro))

    pitchPIDController = PID(1,0,0)

    while True:
        heading, roll, pitch = bno.read_euler()

        pitchPIDOutput = pitchPIDController.update(pitch, 0)

        print('Heading={0:0.2F} Roll={1:0.2F} Pitch={2:0.2F}'.format(heading, roll, pitch))

        print('PITCH PID OUTPUT: '+str(pitchPIDOutput))

        time.sleep(1)

#armMotors()

#time.sleep(5)
#simpleExample()
#manualControl()
autonomousControl()

#stopMotors()
