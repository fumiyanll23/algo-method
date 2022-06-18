# input
N, X = map(int, input().split())

# compute
MONEY = 500

# output
for _ in range(N+1):
    print(X)
    X += MONEY
