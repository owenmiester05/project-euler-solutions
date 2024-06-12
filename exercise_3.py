'''What is the largest prime factor of the number 600851475143'''

def get_prime_factors(num: int):
    if num == 1:
        return [1]
    n = 2
    factors = []
    while n**2 <= num:
        if num % n == 0:
            factors.append(n)
            num //= n
        else: n += 1
    if num > 1:
        factors.append(num)
    return factors

print(max(get_prime_factors(600851475143)))

