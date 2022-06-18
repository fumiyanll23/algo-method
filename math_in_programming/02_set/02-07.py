# input
N, X, Y = map(int, input().split())
As = [*map(int, input().split())]
Bs = [*map(int, input().split())]

# compute

# output
print(sum(i not in As and i not in Bs for i in range(1, N+1)))
