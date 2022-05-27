# input
S = input()
c = input()

# compute
ans = 'No'
for s in S:
    if s == c:
        ans = 'Yes'
        break

# output
print(ans)
