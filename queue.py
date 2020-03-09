
class RRQueue:
    def __init__(self, size=1):
        self.size = size
        self.a = []

    def add_to_back(self, new):
        try:
            self.a.append(new)
        except IndexError:
            print('Queue Is Full!\n')

    def move_first_to_back(self):
        try:
            temp = self.a.pop(0)
            self.a.append(temp)
        except IndexError:
            "\nQueue Is Empty!"
        self.show_queue()

    def remove(self, id):
        if len(self.a) == 1:
            print("\n\n{} Complete! Removed From Queue!".format(id.getid()))
            self.a = []
        else:
            for i in range(len(self.a)-1):
                if self.a[i] == id:
                    self.a.remove(id)
                    print("\n\n{} Complete! Removed From Queue!".format(id.getid()))

        self.show_queue()

    def get_queue(self):
        return self.a

    def curr_process(self):
        if len(self.a) > 0:
            return self.a[0]
        else:
            return -1   # RETURNS -1 WHEN THERE'S NOTHING LEFT IN THE QUEUE

    def show_queue(self):
        b = []
        c = []
        for i in range(len(self.a)):
            b.insert(i, self.a[i].getid())
            c.insert(i, self.a[i].currservicetime)

        print("\n\nFRONT::  {}  ::BACK\n".format(b), end="")
        print("TIMES::  {}  ::LEFT\n".format(c))

    def isempty(self):
        if len(self.a) == 0:
            return True
        return False

    def isin(self, x):  # checks is string x is in the queue already
        if self.a.count(x) > 0:
            return True
        else:
            return False

