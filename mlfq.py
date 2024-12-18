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
    def __init__(self, arrival_time, cpu_time: list, io_time: list):
        self.arrival_time = arrival_time
        self.cpu_time = cpu_time
        self.io_time = io_time

    def __str__(self):
        return f"Process(arrival_time={self.arrival_time}, cpu_bursts={self.cpu_time}, io_bursts={self.io_time})"

def get_input():
    processes = {}
    no_of_processes = int(input("Enter number of processes: "))
    for i in range(no_of_processes):
        char_name = chr(65 + i)
        arrival_time = int(input("Enter arrival time for process: "))
        print("Enter CPU and I/O burst in one line separated by space (e.g. 5 5 5 2 2)")
        cpu_time = [int(x) for x in input("Enter CPU Burst Time: ").split()]
        i_o = [int(x) for x in input("Enter I/O Burst Time: ").split()]

        # Sample: "A": Process(0, [5, 5, 5], [2, 2]) - in dictionary format so we can access through process["A"]
        processes[char_name] = Process(arrival_time, cpu_time, i_o)

    # not sure if we should make a list of Chars ([A, B, C]) to help with indexing? 
    return no_of_processes, processes

def mlfq(queues: list, processes: list):
    pass

# Sample given in specs
# A = Process(0, [5, 5, 5], [2, 2])
# B = Process(2, [2, 6], [2])
# C = Process(0, [30], [])

def main():
    queues = [Queue(8), Queue(8), Queue(math.inf)]
    no_of_processes, processes = get_input()
    # mlfq(no_of_processes, processes, queues)

if __name__ == "__main__":
    main()
