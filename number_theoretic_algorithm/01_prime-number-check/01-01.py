def is_prime(n: int):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def ceiling_prime(n: int):
    n += 1
    while not is_prime(n):
        n += 1
    return n


# input
n = 53

# compute

# output
print(ceiling_prime(n))
