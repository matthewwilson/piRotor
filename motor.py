class Motor:
    def __init__(self, channel, pwm):
        self.channel = channel
        self.pwm = pwm

    def arm():
        print('Arming motor on channel: '+self.channel)
        pwm.set_pwm(self.channel,0,260)
