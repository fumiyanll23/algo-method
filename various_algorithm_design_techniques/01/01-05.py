# input
N = int(input())

# compute
ans = 0
while N > 0:
    if N%3 == 0:
        N //= 3
    else:
        N -= 1
    ans += 1

# output
print(ans)
