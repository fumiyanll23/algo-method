# input
X, d = map(int, input().split())

# compute
ans = 0
if d == 0:
    ans = 1
elif d > 0:
    ans = 2
else:
    ans = 3

# output
print(ans)
