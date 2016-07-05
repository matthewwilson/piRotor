class Motor:
    def __init__(self, channel, pwm):
        self.channel = channel
        self.pwm = pwm

    def arm(self):
        print('Arming motor on channel: '+str(self.channel))
        self.pwm.set_pwm(self.channel,0,260)

    def setSpeed(self, pwmValue):
        self.pwm.set_pwm(self.channel,0,pwmValue)    
