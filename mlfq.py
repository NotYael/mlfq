# CS 140 Project 1: MLFQ Implementation in Python
# Danyael Dela Cruz
# Matthew Martinez
# Kaila Ondoy
# Sam Teng

# TODO:
# - Implement Round Robin
# - Implement changing of priority
# - Implement I/O time
# - Implement context switching
# - Implement sorting of processes in queue (if needed)
# - Implement final results (turn around time, waiting time, etc.)

import math

class Queue:
    def __init__(self, priority, time_quantum):
        self.priority = priority
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
        self.priority = 0
        self.used_quantum = 0
        self.current_burst = 0
        self.current_io = 0

    def __str__(self):
        return f"Process(label={self.label}, arrival_time={self.arrival_time}, cpu_bursts={self.cpu_time}, io_bursts={self.io_time})"

def get_input():
    queues = []
    processes = []

    print("# Enter Scheduler Details #")
    num_processes = int(input(""))
    for i in range(2):
        time_allotment = int(input())
        queues.append(Queue(i, time_allotment))
    # Infinite time allotment for last queue
    queues.append(Queue(2, math.inf))

    context_switch = int(input(""))

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

# MLFQ Algorithm
# while there are still processes to run
#  if there are processes that have arrived, insert them to the ready queue in order of label
#  if the CPU is not running anything, get the next process to run
#  if the CPU has used up its quantum, move the process to the next queue
#  if the CPU has finished its burst, move the process to the next queue
#  if the process has finished all its bursts, remove it from the system
#  if the process has an IO burst, move it to the IO queue

def mlfq(queues: list, processes: list, context_switch: int):

    time = 0
    num_processes = len(processes)
    done_processes = 0
    ready_queue = []
    io_queue = []
    cpu = None

    print("# Scheduling Results #")

    while done_processes < num_processes:
        
        print(f"At Time = {time}")

        # Case of arriving process
        arrived = [process for process in processes if process.arrival_time == time]
        if arrived:
            arrived.sort(key=lambda Process: Process.label)
            ready_queue += arrived
            print(f"Arriving : [{', '.join(process.label for process in arrived)}]")
        
        # if ready queue not empty, insert processes to queues based on priority
        if ready_queue:
            for process in ready_queue:
                for queue in queues:
                    if process.priority == queue.priority:
                        queue.queue.append(process)
                        ready_queue.remove(process)


        # case for when CPU has used up its quantum
        if cpu and cpu.used_quantum == queues[cpu.priority].time_quantum:
            pass

        # account for round robin somewhere 

        # swap cpu if quantum is used up / and also check if there is still remaining burst and i/o time
        if cpu and cpu.current_burst == 0:
            pass

        # if cpu is not running anything, get the next process to run.
        if not cpu:
            for queue in queues:
                if queue.queue:
                    # ADD SOME CHECKING HERE FOR CASE OF AFTER IO / GOES BACK INTO READY QUEUE / ETC.
                    # what if theres is already an existing process in the queue and another process arrives? ([C], then B arrives, need cause to handle sorting WHEN NEEDED) 
                    #   - still dk when this applies cause I already sorted in ready queue but I feel like this is important
                    cpu = queue.queue.pop(0)
                    # set the current burst to the first burst in the list
                    cpu.current_burst = cpu.cpu_time.pop(0)
                    break

        queue_status = [f"[{' '.join(process.label for process in queue.queue)}]" for queue in queues]
        print(f"Queues : {' '.join(queue_status)}")
        print(f"CPU : {cpu.label}")
        if io_queue:
            print(f"IO : [{' '.join(process.label for process in io_queue)}]")
        print("\n")

        # add case for lowering priority 
        # account for context switching

        time += 1
        if cpu:
            cpu.used_quantum += 1
            cpu.current_burst -= 1
            # add case for I/O time instead
        
        # still need to implement checking if I/O queue is empty
        if io_queue:
            for process in io_queue:
                process.current_io += 1
                if process.current_io == process.io_time[0]:
                    io_queue.remove(process)
                    process.current_io = 0
                    process.io_time.pop(0)
                    # add process back to ready queue
                    ready_queue.append(process)

        # testing
        if time == 10:
            break
    
    # print final results
    # turn around time
    # waiting time


# Sample given in specs
# A = Process(0, [5, 5, 5], [2, 2])
# B = Process(2, [2, 6], [2])
# C = Process(0, [30], [])

def main():
    queues, processes, context_switch = get_input()
    mlfq(queues, processes, context_switch)

if __name__ == "__main__":
    main()
