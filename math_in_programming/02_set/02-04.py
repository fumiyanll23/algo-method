# input
N, X, Y = map(int, input().split())

# compute

# output
print(sum(not (i % X) and not (i % Y) for i in range(1, N+1)))
