class Motor:
    def __init__(self, channel, pwm, minPwm, maxPwm):
        self.channel = channel
        self.pwm = pwm
        self.pwmValue = 0
        self.minPwm = minPwm
        self.maxPwm = maxPwm

    def arm(self):
        print('Arming motor on channel: '+str(self.channel))
        self.pwmValue = 260
        self.pwm.set_pwm(self.channel,0,260)

    def setPwmValue(self, pwmValue):

        if pwmValue > self.maxPwm:
            pwmValue = self.maxPwm
        elif pwmValue < self.minPwm:
            pwmValue = self.minPwm

        self.pwmValue = pwmValue
        self.pwm.set_pwm(self.channel,0,pwmValue)

    def getPwmValue(self):
        return self.pwmValue

    def stop(self):
        print('Stopping motor on channel: '+str(self.channel))
        self.speed = 260
        self.pwm.set_pwm(self.channel,0,260)

    def calibrateThrottle():
        print("Disconnect power from ESC, leave connected to PWM hat")
        time.sleep(5)
        print("Setting throttle to highest position, please connect power to ESC")
        pwm.set_pwm(self.channel,0,457)
        time.sleep(10)
        print("The motor should produce a series of initialization beeps increasing in pitch, followed by another beep matching the pitch of the last initialization beep.")
        raw_input("Press enter once initialization beeps finish")
        print("Moving throttle to lowest position, two beeps of the same pitch should be emitted, followed by higher pitched long beep")
        pwm.set_pwm(self.channel,0,276)
        raw_input("Press enter after the beeps")
        print("ESC exiting calibration mode")
        print("ESC should arm and produce a higher pitched long beep")
