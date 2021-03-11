def get_prime_factorization(number):
    factors = set()
    prime_factors = set()
    for possible_factor in range(1, int(number ** 0.5) + 1):
        if number % possible_factor == 0:
            factors.add(possible_factor)
            factors.add(number//possible_factor)

    for possible_prime in factors:
        if is_prime(possible_prime):
            prime_factors.add(possible_prime)
    return prime_factors


def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False

    for x in range(3, int(number ** 0.5) + 1, 2):
        if number % x == 0:
            return False
    return True


if __name__ == '__main__':
    example_solution = get_prime_factorization(13195)
    print(f'The prime factorization of 13195 is {example_solution}')

    question_solution = get_prime_factorization(600851475143)
    print(f'The prime factorization of 600851475143 is {question_solution}')
