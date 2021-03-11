from ProjectEuler.problem_001.problem001 import multiples_of


def test_problem_001():
    assert(23 == sum(multiples_of([3, 5], 10)))
    assert(233168 == sum(multiples_of([3, 5], 1000)))
