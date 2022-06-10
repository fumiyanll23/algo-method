# input
N = int(input())

# compute
dp = [0] * N
for i in range(N):
    if i == 0:
        dp[i] = 1
    elif i == 1:
        dp[i] = 2
    elif i == 2:
        dp[i] = 4
    else:
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

# output
print(dp[-1])
