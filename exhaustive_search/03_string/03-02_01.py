# input
S = input()

# compute
ans = 'Yes'
for s, t in zip(S, reversed(S)):
    if s != t:
        ans = 'No'
        break

# output
print(ans)
