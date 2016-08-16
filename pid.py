import time

class PID:

    def __init__(self, pTune, iTune, dTune):
        self.lastError = 0.0
        self.pTune = pTune
        self.iTune = iTune
        self.dTune = dTune
        self.iError = 0.0
        self.dt = int(time.time())

    def update(self, input, target):

        print("Input: "+str(input))

        self.dt = self.dt - int(time.time())

        if self.dt <= 0:
            self.dt = 1

        print("DT: "+str(self.dt))

        error = target - input

        print("ERROR: "+str(error))

        self.iError += (error + self.iError) * self.dt

        pError = error * self.pTune

        print("pError: "+str(pError))

        iError = self.iError * self.iTune

        print("iError: "+str(iError))

        dError = ((error - self.lastError) / self.dt) * self.dTune

        print("dError: "+str(dError))

        self.lastError = error

        output = pError + iError + dError

        print("output: "+str(output))

        return output
