# CS 140 Project 1: MLFQ Implementation in Python
# Danyael Dela Cruz
# Matthew Martinez
# Kaila Ondoy
# Sam Teng

import math

class Queue_1:
    time_allotment = 8
    queue = []

class Queue_2:
    time_allotment = 8
    queue = []

class Queue_3:
    time_allotment = math.inf
    queue = []

class Process:
    def __init__(self, arrival_time, burst_time: list, i_o: list):
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.i_o = i_o

# Sample given in specs, but not sure if this is the proper way to input
A = Process(0, [5, 5, 5], [2, 2])
B = Process(2, [2, 6], [2])
C = Process(0, [30])