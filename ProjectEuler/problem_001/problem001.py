# If we list all the natural numbers below 10 that are multiples of 3 or 5,
#       we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def multiples_of(multiples, max):
    for num in range(min(multiples), max):
        if any([num % multiple == 0 for multiple in multiples]):
            yield num
    return


if __name__ == "__main__":
    multiples = [3, 5]
    sum_below_10 = sum(multiples_of(multiples, max=10))
    print(f'Sum of numbers that are multiples of 3 and 5 below 10: {sum_below_10}')

    sum_below_1000 = sum(multiples_of(multiples, max=1000))
    print(f'Sum of numbers that are multiples of 3 and 5 below 1000: {sum_below_1000}')
