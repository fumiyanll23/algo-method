# input
N, X, r = map(int, input().split())
MOD = pow(10, 9)

# compute

# output
print(X * (pow(r, N, MOD) - 1) % MOD)
