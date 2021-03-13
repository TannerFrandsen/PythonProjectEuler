from ProjectEuler.problem_007.problem007 import find_nth_prime


def test_problem_007_example():
    assert(13 == find_nth_prime(6))


def test_problem_007_solution():
    assert(104743 == find_nth_prime(10001))
