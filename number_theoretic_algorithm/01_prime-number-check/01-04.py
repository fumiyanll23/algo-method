def is_prime(n: int):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def floor_prime(n: int):
    while not is_prime(n):
        n -= 1
    return n


# input
N = int(input())

# compute

# output
print(floor_prime(N))
