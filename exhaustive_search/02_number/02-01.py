# input
N = int(input())

# compute
ans = 0
for i in range(1, N + 1):
    if (i%2 != 0) and (i%3 != 0) and (i%5 != 0):
        ans += 1

# output
print(ans)
