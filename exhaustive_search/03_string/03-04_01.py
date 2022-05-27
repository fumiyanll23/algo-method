# input
N = int(input())
S = input()
T = input()

# compute
ans = 0
for s, t in zip(S, T):
    if s != t:
        ans += 1

# output
print(ans)
