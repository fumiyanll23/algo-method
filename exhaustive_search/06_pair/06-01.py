# input
N, K = map(int, input().split())
As = [*map(int, input().split())]

# compute

# output
print(sum(As[i]+As[j] <= K for i in range(N) for j in range(i+1, N)))
