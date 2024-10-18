numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
no_primes = []
for i in range(2, len(numbers) + 1):
    is_prime = 0
    for j in range(2, i + 1):
        if i % j == 0 and i != j and j != 1:
            is_prime += 1
    if is_prime == 0:
        primes.append(i)
    else:
        no_primes.append(i)
print('Primes:', primes)
print('Not Primes: ', no_primes)
