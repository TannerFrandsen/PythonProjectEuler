# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import itertools


def find_magic_number(divisors):
    for possible_magic_number in itertools.count(max(divisors), max(divisors)):
        failed = False
        for required_divisior in reversed(divisors):
            if not (possible_magic_number % required_divisior == 0):
                failed = True
                break

        if failed:
            continue

        return possible_magic_number


if __name__ == '__main__':
    print(f'smallest magic number of divisors for 1-10: {find_magic_number(list(range(1, 11)))}')
    print(f'smallest magic number of divisors for 1-20: {find_magic_number(list(range(1, 21)))}')
