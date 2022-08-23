# input
a, b = map(int, input().split())

# compute
ans = 0
if -b < a <= b:
    ans = 1
elif a > b:
    ans = 2
else:
    ans = 3

# output
print(ans)
