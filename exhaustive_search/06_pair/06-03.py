# input
N = int(input())
As = [*map(int, input().split())]

# compute

# output
print(sum(max(As[i], As[j], As[k]) == As[j] for i in range(N) for j in range(i+1, N) for k in range(j+1, N)))
