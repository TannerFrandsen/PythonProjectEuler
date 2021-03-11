# A palindromic number reads the same both ways. The largest palindrome made from the
#   product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


def is_palendrone(num):
    forwards = str(num)
    backwards = forwards[::-1]
    return forwards == backwards


def generate_dot_product(listA, listB):
    return list(set([x * y for x in listA for y in listB]))


def find_largest_palendrone_from_list(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    for num in sorted_numbers:
        if is_palendrone(num):
            return num


def find_solution(min_num, max_num):
    numbers = generate_dot_product(list(range(min_num, max_num)), list(range(min_num, max_num)))
    return find_largest_palendrone_from_list(numbers)


if __name__ == '__main__':
    print(f'Largest palendrone of the product of 2 digit numbers: {find_solution(10, 100)}')
    print(f'Largest palendrone of the product of 2 digit numbers: {find_solution(100, 1000)}')
