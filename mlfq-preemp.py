# CS 140 Project 1: MLFQ Implementation in Python
# Danyael Dela Cruz
# Matthew Martinez
# Kaila Ondoy
# Sam Teng

class Queue:
    def __init__(self, priority: int, time_allotment: int):
        self.priority = priority
        self.time_allotment = time_allotment
        self.processes = []

class Process:
    def __init__(self, name: str, arrival_time: int, cpu_bursts: list[int], io_bursts: list[int]):
        self.name = name
        self.arrival_time = arrival_time
        self.cpu_bursts = cpu_bursts
        self.io_bursts = io_bursts

        self.priority = 0
        self.curr_cpu = 0
        self.curr_io = 0
        self.uptime = 0

        self.completion_time = 0
        self.total_burst = sum(cpu_bursts) + sum(io_bursts)
    
    def __str__(self):
        return f"[{self.name} : {self.priority}]\t| UPTIME: {self.uptime}\t| CPU: {self.curr_cpu}\t| I/O: {self.curr_io}\t| CPU BURSTS: {self.cpu_bursts}\t| I/O BURSTS: {self.io_bursts}"

def get_input():
    queues = []
    processes = []

    print("# Enter Scheduler Details #")
    num_processes = int(input())
    for i in range(2): queues.append(Queue(i, int(input())))
    queues.append(Queue(2, 50))
    context_switch = int(input())

    print(f"# Enter {num_processes} Process Details #")
    for i in range(num_processes):
        cpu_bursts = []
        io_bursts = []
        user_input = input().split(";")
        name = user_input[0]
        arrival_time = int(user_input[1])
        for i in range(2, len(user_input)):
            if i % 2 == 0: cpu_bursts.append(int(user_input[i]))
            else: io_bursts.append(int(user_input[i]))
        processes.append(Process(name, arrival_time, cpu_bursts, io_bursts))

    return queues, processes, num_processes, context_switch

def enqueue(queues: list[Queue], processes: list[Process]):
    if processes:
        for queue in queues:
            for process in processes:
                if process.priority == queue.priority and process not in queue.processes:
                    queue.processes.append(process)
                    # processes.remove(process)

def mlfq(queues: list[Queue], processes: list[Process], num_processes: int, context_switch: int):
    time = 0
    curr_cs = 0

    cpu: Process = None
    io: list[Process] = []
    
    completed: list[Process] = []

    print("# Scheduling Results #")

    while processes:
        
        from_new: list[Process] = []
        from_cpu: list[Process] = []
        from_io: list[Process] = []

        done = None
        demotion = None

        # [X] Remove completed process
        # [X] Move process between CPU and I/O

        # [X] Enqueue newly arriving processes
        # [X] Enqueue process from CPU
        # [X] Enqueue processes from I/O
        # [X] Context switch to new process

        for process in processes:
            # Remove process if completed
            if not (process.curr_cpu or process.curr_io or process.cpu_bursts or process.io_bursts):
                done = process.name
                process.completion_time = time
                completed.append(process)
                if process == cpu:
                    cpu = None
                    curr_cs = context_switch
                elif process in io: io.remove(process)
                processes.remove(process)
                continue

            # Handle process from new arrivals
            if process.arrival_time == time:
                from_new.append(process)
            
            # Handle process from CPU
            if process == cpu:
                # Process exceeds time allotment
                if process.uptime == queues[process.priority].time_allotment:
                    demotion = process.name
                    print(f"[DEBUG] {process.name} DEMOTED")
                    process.priority += 1
                    process.uptime = 0
                    cpu = None
                    curr_cs = context_switch
                    from_cpu.append(process)
                    if process.curr_cpu: process.cpu_bursts.insert(0, process.curr_cpu)

                # Process completes RR quantum
                elif process.priority == 0 and process.uptime == 4:
                    cpu = None
                    curr_cs = context_switch
                    from_cpu.append(process)
                    if process.curr_cpu: process.cpu_bursts.insert(0, process.curr_cpu)

                # Process completes CPU burst
                if process.curr_cpu == 0:
                    if process.io_bursts:
                        process.curr_io = process.io_bursts.pop(0)
                        process.uptime = 0
                        io.append(process)
                    cpu = None
                    curr_cs = context_switch

            # Handle process from I/O
            if process in io:
                if process.curr_io == 0 and process.cpu_bursts:
                    io.remove(process)
                    from_io.append(process)
                else: process.curr_io -= 1
        
        # Enqueue newly arriving processes
        enqueue(queues, sorted(from_new, key=lambda Process: Process.name))
        # Enqueue process from CPU
        enqueue(queues, sorted(from_cpu, key=lambda Process: Process.name))
        # Enqueue processes from I/O
        enqueue(queues, sorted(from_io, key=lambda Process: Process.name))

        # Context switch to new process
        if curr_cs > 0:
            print(f"[DEBUG] CONTEXT SWITCH TIME LEFT: {curr_cs}")
            curr_cs -= 1
        else:
            if cpu:
                for queue in queues:
                    if queue.priority < cpu.priority and queue.processes:
                        print("[DEBUG] Preempting CPU for a higher-priority process.")
                        # Save current CPU process state
                        if cpu:
                            # Put remaining burst back
                            if cpu.curr_cpu > 0:
                                cpu.cpu_bursts.insert(0, cpu.curr_cpu)
                            # Reset uptime (do not change priority)
                            cpu.uptime = 0
                            # Re-insert CPU process into its appropriate queue
                            queues[cpu.priority].processes.append(cpu)

                        # Switch to the higher-priority process
                        cpu = queue.processes.pop(0)
                        cpu.curr_cpu = cpu.cpu_bursts.pop(0)
                        curr_cs = context_switch
                        break

            if not cpu:
                for queue in queues:
                    if queue.processes:
                        cpu = queue.processes.pop(0)
                        cpu.curr_cpu = cpu.cpu_bursts.pop(0)
                        break

            if cpu:
                cpu.curr_cpu -= 1
                cpu.uptime += 1
                
        # [X] Output time
        # [X] Output newly arriving processes
        # [X] Output process done
        # [X] Output queue states
        # [X] Output process in CPU
        # [X] Output processes in I/O
        # [X] Output process demotion

        # [DEBUG]
        # for process in processes: print(process)
        
        # Output time
        print(f"At Time = {time}")
        # Output newly arriving processes
        if from_new: print(f"Arriving : [{', '.join(process.name for process in from_new)}]")
        # Output process done
        if done: print(f"{done} DONE")
        # Output queue states
        queue_status = [f"[{', '.join(process.name for process in queue.processes)}]" for queue in queues]
        print(f"Queues : {';'.join(queue_status)}")
        # Output process in CPU
        if cpu: print(f"CPU : {cpu.name}")
        else: print("CPU : []")
        # Output processes in I/O
        if io: print(f"I/O : [{', '.join(process.name for process in io)}]")
        # Output process demotion
        if demotion: print(f"{demotion} DEMOTED")
        print()

        time += 1

    print("SIMULATION DONE\n")

    # [X] Compute and output turn-around time for each process
    # [X] Compute and output average turn-around time
    # [X] Compute waiting time for each process

    turnaround_times: list[int] = []

    completed = sorted(completed, key=lambda process: process.name)

    # Compute and output turn-around time for each process
    for process in completed:
        turnaround_time = process.completion_time - process.arrival_time
        turnaround_times.append(turnaround_time)
        print(f"Turn-around time for Process {process.name} : {process.completion_time} - {process.arrival_time} = {turnaround_time} ms")
    
    # Compute and output average turn-around time
    print(f"Average Turn-around time = {round((sum(turnaround_times)/num_processes), 2)} ms")

    # Compute waiting time for each process
    for process in completed: print(f"Waiting time for Process {process.name} : {process.completion_time - process.arrival_time - process.total_burst} ms")

def main():
    queues, processes, num_processes, context_switch = get_input()
    mlfq(queues, processes, num_processes, context_switch)

if __name__ == "__main__":
    main()