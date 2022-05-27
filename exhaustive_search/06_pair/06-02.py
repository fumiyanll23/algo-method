# input
L, R = map(int, input().split())

# compute

# output
print(sum(i%10 == j%10 for i in range(L, R+1) for j in range(i+1, R+1)))
