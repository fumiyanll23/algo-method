# input
N, M = map(int, input().split())
As = [*map(int, input().split())]
Bs = [*map(int, input().split())]

# compute
ans = 0
for A in As:
    for B in Bs:
        if A > B:
            ans += 1

# output
print(ans)
