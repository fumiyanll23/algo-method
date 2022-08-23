# input
a, b = map(int, input().split())

# compute
ans = "inf"
if b > 0:
    ans = "inf"
elif b == 0:
    ans = a
else:
    ans = "-inf"

# output
print(ans)
