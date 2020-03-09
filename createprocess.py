from process import *
from random import *


# Amount of processes,
def create(amount=25):
    processes = []
    currarrival = 0

    for i in range(1, amount+1):                           #Previous Arrival Time + Inter Arrrival Time \/\/
        currarrival = currarrival + randrange(4, 9)  # makes arrival times (previousArrivalTime + random(4,8))
        currservice = randrange(2, 6)                # makes service times (random(2,5))

        if i == 1:  # set the first process arrival time to 0
            currarrival = 0

        p = Process(id="p" + str(i), arrival_time=currarrival, service_time=currservice)
        processes.append(p)  # adds processes to list to be returned
    return processes


# Attempt to make the arrival times using formula
def arrivals(amount):
    l = []
    currarrival = 0
    for i in range(len(amount)):
        r = randrange(0, 2) # makes Random number 0-1
        temp = currarrival
        currarrival = currarrival + (4 + ((8-4)*r))
        # print("{} + (4 + ((8-4)*{})) = {}".format(temp, r, currarrival))
        l.append(currarrival)
    return l


# Attempt to make all the service times with formula
def services(amount):
    l = []
    currservice = 0
    for i in range(len(amount)):
        r = randrange(0, 2)  # makes Random number 0-1
        currservice = (2 + ((5-2)*r))
        # print("(2 + ((5-2)*{})) = {}".format(r, currservice))
        l.append(currservice)
    return l