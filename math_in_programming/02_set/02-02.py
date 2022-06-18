# input
N, M = map(int, input().split())
As = [*map(int, input().split())]
Bs = [*map(int, input().split())]

# compute

# output
for ans in sorted(set(As) | set(Bs)):
    print(ans)
