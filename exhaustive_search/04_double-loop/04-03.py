# input
L, R = map(int, input().split())

# compute

# output
print(sum(str(i) == str(i)[::-1] for i in range(L, R+1)))
