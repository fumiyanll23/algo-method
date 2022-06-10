# input
N, M = map(int, input().split())
Ds = [*map(int, input().split())]

# compute
dp = [False] * (N+1)
for ni in range(N+1):
    if ni == 0:
        dp[ni] = True
    for D in Ds:
        if ni >= D:
            dp[ni] = dp[ni] or dp[ni-D]

# output
print("Yes" if dp[-1] else "No")
