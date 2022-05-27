# input
S = input()
T = input()

# compute
n = len(S)
m = len(T)
ans = 'No'
for i in range(n - m + 1):
    if S[i:i+m] == T:
        ans = 'Yes'
        break

# output
print(ans)
