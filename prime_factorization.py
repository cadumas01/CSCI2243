import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def prime_factorization(n):
    factors = []
    while not is_prime(n):
        i = 2
        while i < int(math.sqrt(n) + 1):
            if n % i == 0:
                factors.append(i)
                n = n / i
                i = 2
            else:
                i += 1
    factors.append(int(n))
    return factors


if __name__ == "__main__":
    while True:
        n = int(input('> '))
        print(prime_factorization(n))

# my comment