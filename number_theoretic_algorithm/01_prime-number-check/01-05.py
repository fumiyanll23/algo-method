def is_prime(n: int):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def is_Goldbach(n: int):
    for i in range(2, n):
        if is_prime(i) and is_prime(n - i):
            return i
    return -1


# input
N = int(input())

# compute

# output
print(is_Goldbach(N))
