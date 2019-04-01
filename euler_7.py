primes = [2, 3]
i = 3
while len(primes) < 10001:
    i += 2
    is_prime = True
    for j in primes:
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)

print(primes[10000])