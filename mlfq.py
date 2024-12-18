# CS 140 Project 1: MLFQ Implementation in Python
# Danyael Dela Cruz
# Matthew Martinez
# Kaila Ondoy
# Sam Teng

import math

class Queue:
    def __init__(self, time_quantum, priority):
        self.time_quantum = time_quantum
        self.queue = []

class Process:
    def __init__(self, arrival_time, burst_time: list, i_o: list):
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.i_o = i_o

# Sample given in specs, but not sure if this is the proper way to input
A = Process(0, [5, 5, 5], [2, 2])
B = Process(2, [2, 6], [2])
C = Process(0, [30])

Q_1 = Queue(8)
Q_2 = Queue(8)
Q_3 = Queue(math.inf)

