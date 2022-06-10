# input
N, M = map(int, input().split())
As = [*map(int, input().split())]

# compute
dp = [1<<30] * N
for ni in range(N):
    if ni == 0:
        dp[ni] = 0
    for mj in range(1, M+1):
        if ni >= mj:
            dp[ni] = min(dp[ni], dp[ni-mj] + mj*As[ni])

# output
print(dp[-1])
