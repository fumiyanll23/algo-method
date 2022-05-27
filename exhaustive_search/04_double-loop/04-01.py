def is_prime(n: int):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# input
N = int(input())
As = [*map(int, input().split())]

# compute

# output
print(sum(map(is_prime, As)))
