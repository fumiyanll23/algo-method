# input
X, Y, Z = map(int, input().split())
As = [*map(int, input().split())]
Bs = [*map(int, input().split())]
Cs = [*map(int, input().split())]

# compute

# output
print(sum(A+B == C for A in As for B in Bs for C in Cs))
