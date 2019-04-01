import time

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


primes = [2, 3, 5]
prime_sum = 10
j = 7

t1 = time.time()
while j < 2000000:
    if j % 2 != 0 and j % 3 != 0 and j % 5 != 0:
        if is_prime(j):
            prime_sum += j
    j += 2
t2 = time.time()
print(prime_sum)
print("Seconds: " + str(t2-t1))