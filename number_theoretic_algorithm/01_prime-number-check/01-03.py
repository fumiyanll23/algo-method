def is_prime(n: int):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


# input
N = int(input())

# compute

# output
print('Yes' if is_prime(N) else 'No')
