# input
N = int(input())

# compute
ans = 'Yes'
if N == 1:
    ans = 'No'
else:
    for i in range(2, N):
        if N%i == 0:
            ans = 'No'
            break

# output
print(ans)
