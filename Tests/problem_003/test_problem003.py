from ProjectEuler.problem_003.problem003 import get_prime_factorization


def test_problem_003_example():
    example_baseline = set([5, 7, 13, 29])
    res = get_prime_factorization(13195)
    assert(set() == res ^ example_baseline)


def test_problem_003_solution():
    baseline = set([71, 839, 1471, 6857])
    res = get_prime_factorization(600851475143)
    assert(set() == res ^ baseline)
