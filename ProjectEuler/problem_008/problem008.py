# The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
# Input in input.dat file
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
# What is the value of this product?

def read_input(file_path):
    with open(file_path, 'r') as file_handle:
        file_data = file_handle.readlines()
        provided_data = ''.join(file_data)
        provided_data = provided_data.replace('\n', '')
        return provided_data


def largest_product_with_window(number, window_length):
    options = []
    for idx in range(len(number)):
        if idx + window_length > len(number):
            break
        options.append(number[idx: idx + window_length])

    products = []
    for num in options:
        product = 1
        for x in num:
            product = product * int(x)
        products.append(product)

    return max(products)


if __name__ == '__main__':
    data = read_input(r'.\ProjectEuler\problem_008\input.dat')
    print(f'Largest product with a window length of 4 is {largest_product_with_window(data, 4)}')
    print(f'Largest product with a window length of 13 is {largest_product_with_window(data, 13)}')
