max = int(input("prime numbers up to what number? : "))
primes = []
for possiblePrime in range(2, max + 1):
    isPrime = True
    for num in range(2, int(possiblePrime ** 0.5) + 1):
        if possiblePrime % num == 0:
            isPrime = False
            break

    if isPrime:
        primes.append(possiblePrime)
print(primes)
