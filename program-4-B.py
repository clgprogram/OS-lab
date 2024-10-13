def priority_scheduling(processes, burst_times, priorities):
    n = len(processes)
    
    # Initialize waiting and turnaround times
    waiting_times = [0] * n
    turnaround_times = [0] * n

    # Sort processes based on priority (lower number means higher priority)
    sorted_processes = sorted(zip(processes, burst_times, priorities), key=lambda x: x[2])

    # Calculate waiting time for each process
    for i in range(1, n):
        waiting_times[i] = waiting_times[i - 1] + sorted_processes[i - 1][1]

    # Calculate turnaround time for each process
    for i in range(n):
        turnaround_times[i] = waiting_times[i] + sorted_processes[i][1]

    # Calculate average waiting and turnaround times
    avg_waiting_time = sum(waiting_times) / n
    avg_turnaround_time = sum(turnaround_times) / n

    # Print the process details
    print(f"{'Process':<10} {'Burst Time':<15} {'Priority':<10} {'Waiting Time':<15} {'Turnaround Time':<15}")
    for i in range(n):
        print(f"{sorted_processes[i][0]:<10} {sorted_processes[i][1]:<15} {sorted_processes[i][2]:<10} {waiting_times[i]:<15} {turnaround_times[i]:<15}")

    # Print average times
    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")

# Driver code
processes = ['P1', 'P2', 'P3', 'P4']
burst_times = [10, 1, 2, 1]
priorities = [3, 1, 4, 2]

priority_scheduling(processes, burst_times, priorities)
