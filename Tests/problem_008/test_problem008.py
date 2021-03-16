from ProjectEuler.problem_008.problem008 import largest_product_with_window, read_input


def test_problem_008_example():
    data = read_input(r'.\ProjectEuler\problem_008\input.dat')
    assert(5832 == largest_product_with_window(data, 4))


def test_problem_008_solution():
    data = read_input(r'.\ProjectEuler\problem_008\input.dat')
    assert(23514624000 == largest_product_with_window(data, 13))
