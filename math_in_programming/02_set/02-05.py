# input
N, M = map(int, input().split())
As = [*map(int, input().split())]
Bs = [*map(int, input().split())]

# compute

# output
for ans in (A for A in As if A not in Bs):
    print(ans)
