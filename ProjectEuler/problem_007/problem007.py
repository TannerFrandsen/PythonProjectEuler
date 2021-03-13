# 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10001st prime number?
import itertools


def find_nth_prime(n):
    found = 0
    for possible_prime in itertools.count(0):
        if is_prime(possible_prime):
            found += 1
            if found == n:
                return possible_prime


def is_prime(number):
    if number <= 1:
        return False
    elif number == 2: 
        return True
    elif number % 2 == 0:
        return False

    for x in range(3, int(number** 0.5)+1):
        if number % x == 0:
            return False
    return True

if __name__ == '__main__':
    print(f'The 6th prime number is {find_nth_prime(6)}')
    print(f'The 10001st prime number is {find_nth_prime(10001)}')