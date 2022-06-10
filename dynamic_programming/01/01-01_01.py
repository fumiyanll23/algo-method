# input
N, X, Y = map(int, input().split())

# compute
As = [0] * N
As[0], As[1] = X, Y
for i in range(2, N):
    As[i] = (As[i-2]+As[i-1]) % 100

# output
print(As[-1])
