n = int(input("Enter the number of processes: "))

# at, bt = [], []

# for i in range(n):
#     at.append(int(input(f"Enter the arrival time of process P{i}: ")))

# for i in range(n):
#     bt.append(int(input(f"Enter the burst time of process P{i}: ")))

at = [int(input(f"Enter the arrival time of process P{i}: "))for i in range(n)]
bt = [int(input(f"Enter the burst time of process P{i}: "))for i in range(n)]

# wt = [0] * n
# ct = [0] * n
# tat = [0] * n

wt, ct, tat = [0] * n, [0] * n, [0] * n

#remaining processes
rp = []
for i in range(n):
    rp.append((at[i], bt[i], i))
    
current_time = min(at)

while rp:
    available_processes = []
    for i in range(len(rp)):
        if rp[i][0] <= current_time:
            available_processes.append(rp[i])
    
    if not available_processes:
        current_time = min(rp)[0]
        continue
    
    process = min(available_processes, key=lambda x: x[1])
    pid = process[0]
    ct[pid] = current_time + process[1]
    tat[pid] = ct[pid] - at[pid]
    wt[pid] = tat[pid] - bt[pid]
    current_time = ct[pid]
    rp.remove(process)
    
total_wt = sum(wt)
total_tat = sum(tat)
average_wt = total_wt / n
average_tat = total_tat / n