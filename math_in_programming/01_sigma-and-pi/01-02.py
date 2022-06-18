# input
L, R = map(int, input().split())

# compute

# output
print(sum(pow(2*i - 1, 2) for i in range(L, R+1)))
