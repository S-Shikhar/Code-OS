# Get the number of processes
n = int(input('Enter number of processes: '))

# Get the arrival times for each process
at = list(map(int, input(f'Enter arrival times for {n} processes: ').split()))

# Get the burst times for each process
bt = list(map(int, input(f'Enter burst times for {n} processes: ').split()))

# Get the priorities for each process
priority = list(map(int, input(f'Enter priorities for {n} processes: ').split()))

# Initialize waiting times and turnaround times
wt = [0] * n
tat = [0] * n

# Sort processes by priority (higher number indicates higher priority)
processes = sorted(range(n), key=lambda i: (-priority[i], at[i]))

# Calculate waiting times and turnaround times
t = 0
for i in processes:
    if t < at[i]:
        t = at[i]
    wt[i] = t - at[i]
    t += bt[i]
    tat[i] = wt[i] + bt[i]

# Print the results
print('Process\tPriority\tBurst Time\tWaiting Time\tTurnaround Time')
for i in range(n):
    print(f'{i+1}\t{priority[i]}\t\t{bt[i]}\t\t{wt[i]}\t\t{tat[i]}')

# Calculate and print average waiting time and turnaround time
avg_wt = sum(wt) / n
avg_tat = sum(tat) / n
print(f'Average Waiting Time: {avg_wt}')
print(f'Average Turnaround Time: {avg_tat}')