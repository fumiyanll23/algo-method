# input
N, X, Y = map(int, input().split())

# compute
As = [X, Y]
for i in range(N-2):
    As.append((As[-1]+As[-2]) % 100)

# output
print(As[-1])
