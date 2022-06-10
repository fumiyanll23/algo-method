# input
N = int(input())
As = [*map(int, input().split())]

# compute
dp = [1<<20] * N
for i in range(N):
    if i == 0:
        dp[i] = 0
    elif i == 1:
        dp[i] = dp[i-1] + As[i]
    else:
        dp[i] = min(dp[i-1] + As[i], dp[i-2] + 2*As[i])

# output
print(dp[-1])
