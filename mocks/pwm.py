class PWM:

    def __init__(self):
        self.channels = dict()

    def set_pwm_freq(self, frequency):
        print("setting PWM frequency: "+str(frequency))

    def set_pwm(self,channel,on,pwmValue):
        self.channels[channel] = pwmValue
        print('updated PWM value for channel '+str(channel)+" to "+str(pwmValue))
