from ProjectEuler.problem_005.problem005 import find_magic_number


def test_problem_005_example():
    assert(2520 == find_magic_number(list(range(1, 11))))


def test_problem_005_solution():
    assert(232792560 == find_magic_number(list(range(1, 21))))
