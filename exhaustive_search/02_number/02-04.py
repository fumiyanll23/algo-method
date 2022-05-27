# input
A, B = map(int, input().split())

# compute
ans = 1
for i in range(1, min(A, B)+1):
    if A%i == 0 and B%i == 0:
        ans = i

# output
print(ans)
