# input
A, B, X, Y = map(int, input().split())

# compute
d = (Y - X) // (B - A)

# output
print(X - A*d)
