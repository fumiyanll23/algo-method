# input
N, X = map(int, input().split())

# compute

# output
print(sum(not (i % X) for i in range(1, N+1)))
