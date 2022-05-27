# input
N, M, K = map(int, input().split())
As = [*map(int, input().split())]
Bs = [*map(int, input().split())]

# compute

# output
print(sum(A + B == K for A in As for B in Bs))
