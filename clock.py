import time


class Clock:
    def __init__(self, sleeptime, quantum,  seconds=250):
        self.quantum = quantum
        self.sleeptime = sleeptime
        self.seconds = seconds
        self.maxtime = 500
        self.timenow = 0
        self.pilltokill = True

    def start(self):
        time.clock()
        while self.pilltokill is True:
            print(" {}".format(self.timenow), end='')

            time.sleep(float(self.sleeptime))
            self.timenow += 1

    def stop(self):
        self.pilltokill = False
        quit()

    def gettime(self):
        return int(self.timenow)


