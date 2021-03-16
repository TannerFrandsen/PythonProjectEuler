import os
from ProjectEuler.problem_008.problem008 import largest_product_with_window, read_input


def test_problem_008_example():
    data = read_input(f'.{os.path.sep}ProjectEuler{os.path.sep}problem_008{os.path.sep}input.dat')
    assert(5832 == largest_product_with_window(data, 4))


def test_problem_008_solution():
    data = read_input(f'.{os.path.sep}ProjectEuler{os.path.sep}problem_008{os.path.sep}input.dat')
    assert(23514624000 == largest_product_with_window(data, 13))
