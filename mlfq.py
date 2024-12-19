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

    def __str__(self):
        return f"Queue(time_quantum={self.time_quantum}, self.queue={self.queue})"

class Process:
    def __init__(self, label, arrival_time, cpu_time: list, io_time: list):
        self.label = label
        self.arrival_time = arrival_time
        self.cpu_time = cpu_time
        self.io_time = io_time

    def __str__(self):
        return f"Process(label={self.label}, arrival_time={self.arrival_time}, cpu_bursts={self.cpu_time}, io_bursts={self.io_time})"

def get_input():
    queues = []
    processes = []

    # Queues 
    print("# Enter Scheduler Details #")
    num_processes = int(input(""))
    for i in range(2):
        time_allotment = int(input())
        queues.append(Queue(time_allotment))
    # Infinite time allotment for last queue
    queues.append(Queue(math.inf))

    # Context Switch
    context_switch = int(input(""))

    # Processes
    print(f"# Enter {num_processes} Process Details #")
    for i in range(num_processes):
        cpu_bursts = []
        io_bursts = []
        input_data = input().split(";")
        label = input_data[0]
        arrival_time = int(input_data[1])
        for i in range(2, len(input_data)):
            if i % 2 == 0:
                cpu_bursts.append(int(input_data[i]))
            else:
                io_bursts.append(int(input_data[i]))
        
        processes.append(Process(label, arrival_time, cpu_bursts, io_bursts))

    # for queue in queues:
    #     print(queue)

    # for process in processes:
    #     print(process)

    return queues, processes, context_switch

def mlfq(queues: list, processes: list, context_switch: int):

    time = 0
    num_processes = len(processes)
    done_processes = 0

    print("# Scheduling Results #")

    while True:
        if done_processes == num_processes:
            # SIMULATION DONE STUFF
            # PRINT TURNAROUND TIMES
            # PRINT WAITING TIMES
            break
        
        print(f"At Time {time}")

        # Case of arriving process
        arrived = [process.label for process in processes if process.arrival_time == time]
        if arrived:
            print(f"Arriving {arrived} ")

        order = []
        time += 1

        if time == 10:
            break


# Sample given in specs
# A = Process(0, [5, 5, 5], [2, 2])
# B = Process(2, [2, 6], [2])
# C = Process(0, [30], [])

def main():
    queues, processes, context_switch = get_input()
    mlfq(queues, processes, context_switch)

if __name__ == "__main__":
    main()
