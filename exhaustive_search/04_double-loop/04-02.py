def count_factors(n: int):
    cnt = 0
    for i in range(1, n+1):
        if n%i == 0:
            cnt += 1
    return cnt


# input
N, K = map(int, input().split())

# compute

# output
print(sum(count_factors(i) == K for i in range(1, N+1)))
