from __future__ import division
from adafruit_loader import AdafruitLoader
from motor import Motor
from pid import PID

import time
import sys

class FlightController:

    def __init__(self, mode):
        self.mode = mode
        adafruitLoader = AdafruitLoader(self.mode)
        self.pwm = adafruitLoader.getPwmModule()
        self.bno = adafruitLoader.getBNO055Module()

        if not self.bno.begin():
            raise RuntimeError('Failed to initialize BNO055! Is the sensor connected?')

        # Set frequency to 60hz, good for servos.
        self.pwm.set_pwm_freq(60)

        self.motor1 = Motor(0, self.pwm, 276,457)
        self.motor2 = Motor(1, self.pwm, 276,457)
        self.motor3 = Motor(14, self.pwm, 276,457)
        self.motor4 = Motor(15, self.pwm, 276,457)

    def getPWMValueFromNanoseconds(self,nanoseconds):
        print(nanoseconds)
        pwmValue = nanoseconds / (1000000.0/4096.0/60.0)
        return int(round(pwmValue))

    def armMotors(self):
        print('Arming motors')
        self.motor1.arm()
        self.motor2.arm()
        self.motor3.arm()
        self.motor4.arm()
        time.sleep(5)

    def stopMotors(self):
        print("Stopping")
        self.motor1.stop()
        self.motor2.stop()
        self.motor3.stop()
        self.motor4.stop()

    def calibrateThrottles(self):
        self.motor1.calibrateThrottle()
        self.motor2.calibrateThrottle()
        self.motor3.calibrateThrottle()
        self.motor4.calibrateThrottle()

    def setPwmForAllMotors(self, pwmValue):
        self.motor1.setPwmValue(pwmValue)
        self.motor2.setPwmValue(pwmValue)
        self.motor3.setPwmValue(pwmValue)
        self.motor4.setPwmValue(pwmValue)

    def simpleExample(self):
        print('Starting motors at 300')
        self.setPwmForAllMotors(300)
        time.sleep(3)
        print('increasing to 360')
        self.setPwmForAllMotors(360)
        time.sleep(3)
        print('increasing to 400')
        self.setPwmForAllMotors(400)
        time.sleep(3)
        print('increasing to 450')
        self.setPwmForAllMotors(450)
        time.sleep(3)

    def manualControl(self):
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


    def autonomousControl(self):

        # Print system status and self test result.
        status, self_test, error = self.bno.get_system_status()
        print('System status: {0}'.format(status))
        print('Self test result (0x0F is normal): 0x{0:02X}'.format(self_test))
        # Print out an error if system status is in error mode.
        if status == 0x01:
            print('System error: {0}'.format(error))
            print('See datasheet section 4.3.59 for the meaning.')

        # Print BNO055 software revision and other diagnostic data.
        sw, bl, accel, mag, gyro = self.bno.get_revision()
        print('Software version:   {0}'.format(sw))
        print('Bootloader version: {0}'.format(bl))
        print('Accelerometer ID:   0x{0:02X}'.format(accel))
        print('Magnetometer ID:    0x{0:02X}'.format(mag))
        print('Gyroscope ID:       0x{0:02X}\n'.format(gyro))

        pitchPIDController = PID(0.7,0.1,0.1)

        self.setPwmForAllMotors(300)

        while True:
            heading, roll, pitch = self.bno.read_euler()

            pitchPIDOutput = pitchPIDController.update(pitch, 0)

            print('Heading={0:0.2F} Roll={1:0.2F} Pitch={2:0.2F}'.format(heading, roll, pitch))

            print('PITCH PID OUTPUT: '+str(pitchPIDOutput))

            motor1Value = int(round(self.motor1.getPwmValue()+pitchPIDOutput))
            motor2Value = int(round(self.motor2.getPwmValue()+pitchPIDOutput))

            motor3Value = int(round(self.motor3.getPwmValue()-pitchPIDOutput))
            motor4Value = int(round(self.motor4.getPwmValue()-pitchPIDOutput))

            print('motor1={0} motor2={1} motor3={2} motor4={3}'.format(motor1Value, motor2Value, motor3Value, motor4Value))

            self.motor1.setPwmValue(motor1Value)
            self.motor2.setPwmValue(motor2Value)
            self.motor3.setPwmValue(motor3Value)
            self.motor4.setPwmValue(motor4Value)

            time.sleep(1)
