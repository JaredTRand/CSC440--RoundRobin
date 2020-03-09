
class Process:

    def __init__(self, quantum=15, service_time=30, arrival_time=0, id=""):
        self.quantum = quantum
        self.arrival_time = float(arrival_time)
        self.service_time = service_time
        self.timestarted = 0
        self.timeended = 0
        self.currservicetime = self.service_time
        self.started = False
        self.id = id

    def getid(self):
        return self.id

    def getarrivaltime(self):
        return self.arrival_time

    def getservicetime(self):
        return self.service_time

    def setservicetime(self, new):
        self.service_time = new

    def setstarttime(self, time):
        self.timestarted = time

    def setendtime(self, time):
        self.timeended = time


