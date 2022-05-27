# input
S = input()

# compute
ans = 0
ss = []
for s in S:
    if s not in ss:
        ss.append(s)
        ans += 1

# output
print(ans)
