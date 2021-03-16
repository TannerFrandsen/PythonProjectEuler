from ProjectEuler.problem_010.problem010 import find_sum_of_primes_under_target


def test_problem_010_example():
    assert(17 == find_sum_of_primes_under_target(10))


def test_problem_009_solution():
    assert(142913828922 == find_sum_of_primes_under_target(2000000))
