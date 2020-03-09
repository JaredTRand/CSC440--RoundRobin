from process import *
from clock import *
from queue import *
from createprocess import *
import threading


def main():
    n = 0
    counter = len(completed)
    decidebreak = False
    while True:
        for i in range(len(processes)):
            # This is checks if the process is in the queue and if the runtime is at or over the arrival time of the next
            if not(thequeue.isin(processes[i])) and not(completed.count(processes[i]) > 0)\
                    and theclock.gettime() == int(processes[i].arrival_time):
                thequeue.add_to_back(processes[i])
                thequeue.show_queue()
        if not thequeue.isempty():
            if thequeue.curr_process() == -1:
                break
            runningprocess = thequeue.curr_process()


            # gets first process in queue, then subtracts from the service time for each "second" in the "CPU"
            if n is not theclock.gettime() and runningprocess is not -1:
                runningprocess.currservicetime -= 1

                # checks if it has started running yet so it knows to set the start time
                if runningprocess.started is False:
                    runningprocess.started = True
                    if runningprocess.id == 'p1':
                        runningprocess.setstarttime(0)
                    runningprocess.setstarttime(float(theclock.gettime()))

                # checks if the quantum has been reached, then moves the first to the back of the queue
                if theclock.gettime() % quantum == 0:
                    # checks if the process is done
                    if runningprocess.currservicetime <= 0:
                        runningprocess.setendtime(theclock.gettime())
                        thequeue.remove(runningprocess)
                        # if it's not already in the completed list, it adds it in.
                        if completed.count(runningprocess) is 0:
                            completed.append(runningprocess)
                    # checks if a process was just completed, so it can skip the swap
                    if len(completed) is not counter:
                        counter = len(completed)
                        decidebreak = True


                    # if decidebreak = true, then the last process finished and gave its extra time to the next, negating the need for a swap
                    if not decidebreak:
                        print(" SWAP\n")
                        thequeue.move_first_to_back()
                    decidebreak = False

            # checks if the process is done
            if runningprocess.currservicetime <= 0:
                runningprocess.setendtime(theclock.gettime())
                thequeue.remove(runningprocess)

                # if it's not already in the completed list, it adds it in.
                if completed.count(runningprocess) is 0:
                    completed.append(runningprocess)

        n = theclock.gettime()
        time.sleep(.01)

        # breaks if the queue is empty and theres all in the completed array
        if len(completed) is len(processes):

            for i in range(len(completed)):
                print("{} COMPLETED ".format(completed[i].getid()))
            print("FINISHED")
            calculations()

            return False

# calculate all the stuff we need
def calculations():

    p = []
    w = []

    print("\n\n::: STATS ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n"
          "::: ID ::: :::START TIME::: :::END TIME::: :::INITIAL WAIT TIME::: :::TURNAROUND TIME:::\n"
          "::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

    for i in range(len(processes)):
        currproccess = processes[i]
        turnaround = currproccess.timeended-currproccess.timestarted
        waittime = currproccess.timestarted - currproccess.arrival_time
        print("::: {} ::: ::: {} ::: ::: {} ::: ::: {} ::: ::: {} :::\n"
              "".format(currproccess.getid(), currproccess.timestarted, currproccess.timeended,
                        waittime, turnaround), end='')
        #get the turnaround times for the average so we don't have to calculate twice
        p.append(turnaround)
        w.append(waittime)
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    avgp = 0
    avgw = 0
    avgs = 0
    for i in range(len(p)):
        avgp += p[i]
        avgw += w[i]
        avgs += processes[i].getservicetime()
    avgp = avgp / len(processes)
    # avgw = avgw / len(processes)
    avgs = avgs / len(processes)
    print("\n\n::: TOTAL WAIT TIME:   {} :::::\n"
          "::: AVERAGE TURNAROUND TIME: {} ::\n"
          "::: AVERAGE SERVICE TIME:    {} ::\n"
          "::::::::::::::::::::::::::::::::::\n\n".format(avgw, avgp, avgs), end='')
    print("\n::: INTER-ARRIVAL TIMES :::")
    for i in range(len(processes)-1):
        print("::: {} to {} ::: {} ::::\n"
              "".format(processes[i].getid(), processes[i+1].getid(),
                        processes[i+1].getarrivaltime() - processes[i].getarrivaltime()), end='')

    theclock.stop()
    print(input("Press Enter To Exit") or "")
    quit()


if __name__ == '__main__':
    quantum = int(input("Input Quantum (Press Enter For Default=15):") or 15)

    processes = create(int(input("Input Amount of Processes(Default = 25): ") or 25))
    for i in range(len(processes)):
        print("ID: {}    Arrival: {}   Service: {}".format(processes[i].getid(), processes[i].getarrivaltime(), processes[i].getservicetime()))
    # print("{} \n {}".format(arrivals(processes), services(processes)))

    # makes a clock, queue and empty completed list to fill later
    theclock = Clock(input("Run Speed( >0.01 and <1, Default=0.5):") or float(0.5), quantum)
    thequeue = RRQueue()
    completed = []

    # starts multithreading so clock can run parallel to main
    b = threading.Thread(name='background', target=theclock.start)
    m = threading.Thread(name='foreground', target=main)
    b.start()
    m.start()
