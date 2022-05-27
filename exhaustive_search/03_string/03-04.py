# input
N = int(input())
S = input()
T = input()

# compute

# output
print(sum(s != t for s, t in zip(S, T)))
