# input
N = int(input())
As = [*map(int, input().split())]

# compute
ans = 1
for A in As:
    ans = ans * A % 10

# output
print(ans)
