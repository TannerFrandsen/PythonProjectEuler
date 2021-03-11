from ProjectEuler.problem_004.problem004 import find_solution


def test_problem_004_example():
    assert(9009 == find_solution(10, 100))


def test_problem_004_solution():
    assert(906609 == find_solution(100, 1000))
