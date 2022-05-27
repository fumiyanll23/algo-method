# input
N = int(input())
Ss = [input() for _ in range(N)]

# compute

# output
print('Yes' if any(Ss[i] == Ss[j] for i in range(N) for j in range(i+1, N)) else 'No')
