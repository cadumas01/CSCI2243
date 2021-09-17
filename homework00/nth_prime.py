import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


# key = n, value = nth_prime
primes = {1: 2}


def nth_prime(n):
    if n in primes:
        return primes[n]
    i = 2
    prime_count = 1
    while prime_count < n:
        i += 1
        if is_prime(i):
            prime_count += 1
            primes[prime_count] = i

    return i


if __name__ == "__main__":
    while True:
        n = int(input('> '))
        print(nth_prime(n))
