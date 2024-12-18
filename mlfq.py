# CS 140 Project 1: MLFQ Implementation in Python
# Danyael Dela Cruz
# Matthew Martinez
# Kaila Ondoy
# Sam Teng

import math

class Queue:
    def __init__(self, time_quantum):
        self.time_quantum = time_quantum
        self.queue = []

class Process:
    def __init__(self, arrival_time, burst_time: list, i_o: list):
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.i_o = i_o

def get_input():
    # GET COMMANDLINE INPUT
    arrival_time = int(input("Enter arrival time: "))
    burst_time = []
    i_o = []

    while True:
        # continuously ask for burst time and i/o until input is empty
        break

    return arrival_time, burst_time, i_o

def mlfq(queues: list, processes: list):
    pass


# Sample given in specs
# A = Process(0, [5, 5, 5], [2, 2])
# B = Process(2, [2, 6], [2])
# C = Process(0, [30], [])

Q_1 = Queue(8)
Q_2 = Queue(8)
Q_3 = Queue(math.inf)
