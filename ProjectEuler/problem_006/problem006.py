# The sum of the squares of the first ten natural numbers is,   1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,    (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the
#    first ten natural numbers and the square of the sum is   3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one
#    hundred natural numbers and the square of the sum.


def calculate_sum_of_squares(numbers):
    return sum([num**2 for num in numbers])


def calculate_square_of_sums(numbers):
    return sum(numbers) ** 2


def calculate_solution(start, end):
    provided_input = list(range(start, end+1))
    square_of_sum = calculate_square_of_sums(provided_input)
    sum_of_squares = calculate_sum_of_squares(provided_input)
    return square_of_sum - sum_of_squares


if __name__ == '__main__':
    print(f'Square of sums - sum of squares: {calculate_solution(1, 10)}')
    print(f'Square of sums - sum of squares: {calculate_solution(1, 100)}')
