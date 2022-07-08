# input
N, M = map(int, input().split())
As = [*map(int, input().split())]
Bs = [*map(int, input().split())]

# compute
As.sort()
ans = 0
idx_load = 0
for B in Bs:
    if idx_load >= N:
        break
    if As[idx_load] <= B:
        ans += 1
        idx_load += 1

# output
print(ans)
