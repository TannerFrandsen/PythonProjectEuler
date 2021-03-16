# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.
import itertools


def prime_generator():
    yield 2
    yield 3

    not_prime = True
    for num in itertools.count(5, 2):
        not_prime = False
        for possible_factor in range(2, int(num ** 0.5) + 1):
            if num % possible_factor == 0:
                not_prime = True
                break
        if not_prime:
            continue
        else:
            yield num


def find_sum_of_primes_under_target(target):
    sum = 0
    for x in prime_generator():
        if x > target:
            break
        sum = sum + x
    return sum


if __name__ == '__main__':
    print(f'The product of prime numbers under 10 is {find_sum_of_primes_under_target(10)}')
    print(f'The product of prime numbers under 2000000 is {find_sum_of_primes_under_target(2000000)}')
