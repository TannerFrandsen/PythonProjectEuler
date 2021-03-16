# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a2 + b2 = c2
# For example, 3^2 + 4^2 = 25   5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import itertools


def Pythagorean_triplet_generator():
    natural_squares = set()
    for natural_num in itertools.count(1):
        c_sqr = natural_num ** 2
        natural_squares.add(c_sqr)

        for a_sqr in natural_squares:
            b_sqr = c_sqr - a_sqr
            if b_sqr in natural_squares and a_sqr < b_sqr < c_sqr:
                yield (a_sqr ** 0.5, b_sqr ** 0.5, c_sqr ** 0.5)


def find_Pythagorean_triplet_sum(target):
    for a, b, c in Pythagorean_triplet_generator():
        if a + b + c == target:
            return (a, b, c)

        elif a > target:
            return (0, 0, 0)


if __name__ == '__main__':
    a, b, c = find_Pythagorean_triplet_sum(12)
    print(f'The product of the natural squares that sum to 12 is {a * b * c}')

    a, b, c = find_Pythagorean_triplet_sum(1000)
    print(f'The product of the natural squares that sum to 1000 is {a * b * c}')
