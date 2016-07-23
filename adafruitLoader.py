import sys

class AdafruitLoader:

    def __init__(self, mode):
        self.mode = mode

    def getPwmModule(self):
        if self.mode == 'test':
            from mocks.pwm import PWM
            pwm = PWM()
            return pwm
        else:
            # Import the PCA9685 module.
            import Adafruit_PCA9685
            pwm = Adafruit_PCA9685.PCA9685()
            return pwm

    def getBNO055Module(self):
        if self.mode == 'test':
            from mocks.bno import BNO
            bno = BNO()
            return bno
        else:
            from Adafruit_BNO055 import BNO055
            # Create and configure the BNO sensor connection.  Make sure only ONE of the
            # below 'bno = ...' lines is uncommented:
            # Raspberry Pi configuration with serial UART and RST connected to GPIO 18:
            bno = BNO055.BNO055(serial_port='/dev/ttyAMA0', rst=18)
            return bno
