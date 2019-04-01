import math


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6

    return True


def num_factors(n):
    factor_exponent = []
    i = math.floor(n/2)
    for j in range(2, i):
        if is_prime(j):
            factor_count = 0
            num = n
            while num % j == 0:
                factor_count += 1
                num /= j
            if factor_count > 0:
                factor_exponent.append(factor_count+1)

    prod = 1
    for x in factor_exponent:
        prod *= x

    return prod


j = 28
m = 8
while num_factors(j) <= 500:
    j += m
    m += 1
    print("Num factors: " + str(num_factors(j)) + ", number: " + str(j) + ", m: " + str(m))