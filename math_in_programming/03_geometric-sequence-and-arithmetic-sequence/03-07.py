# input
N = int(input())

# compute
X = 1
R = 2

# output
print(sum(X * pow(R, i) for i in range(N)))
