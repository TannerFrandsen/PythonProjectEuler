from ProjectEuler.problem_002.problem002 import even_fibonacci


def test_problem_001():
    assert(4613732 == sum(even_fibonacci(4000000)))
