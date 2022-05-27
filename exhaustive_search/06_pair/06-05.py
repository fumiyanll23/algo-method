# input
N = int(input())
S = input()

# compute

# output
print(sum(S[i] == S[j] for i in range(N) for j in range(i+1, N)))
