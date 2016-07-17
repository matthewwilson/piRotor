import time

class PID:

    def __init__(self, pTune, iTune, dTune, escMin, escMax):
        self.lastError = 0.0
        self.pTune = pTune
        self.iTune = iTune
        self.dTune = dTune
        self.iError = 0.0
        self.escMin = escMin
        self.escMax = escMax
        self.dt = int(time.time())

    def update(self, input, target):

        self.dt = self.dt - int(time.time())

        if self.dt == 0
            self.dt = 1

        error = target - input

        self.iError += (error + self.iError) * self.dt

        pError = error * self.pTune
        iError = self.iError * self.iTune
        dError = (error - self.lastError) / self.dt

        self.lastError = error

        output = pError + iError + dError

        if output > self.escMax
            output = self.escMax
        elif output < self.escMin
            output = self.escMin

        return output
