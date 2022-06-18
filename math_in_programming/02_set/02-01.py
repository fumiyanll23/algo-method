# input
N, M = map(int, input().split())
As = [*map(int, input().split())]
Bs = [*map(int, input().split())]

# compute

# output
for A in As:
    if A in Bs:
        print(A)
