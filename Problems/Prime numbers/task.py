prime_numbers = [2]
for n in range(3, 1001):
    if all([n % i for i in range(2, n)]):
        prime_numbers.append(n)

