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

rp = []
for i in range(n):
    rp.append((at[i], bt[i], i))
    
current_time = min(at)