# input
N = int(input())
Ss = [input() for _ in range(N)]

# compute

# output
print(sum(S == S[::-1] for S in Ss))
