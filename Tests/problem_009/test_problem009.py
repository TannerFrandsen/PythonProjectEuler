from ProjectEuler.problem_009.problem009 import find_Pythagorean_triplet_sum


def test_problem_009_bad_example():
    a, b, c = find_Pythagorean_triplet_sum(10)
    assert(a == 0)
    assert(b == 0)
    assert(c == 0)


def test_problem_009_example():
    a, b, c = find_Pythagorean_triplet_sum(12)
    assert(a == 3)
    assert(b == 4)
    assert(c == 5)


def test_problem_009_solution():
    a, b, c = find_Pythagorean_triplet_sum(1000)
    assert(a == 200)
    assert(b == 375)
    assert(c == 425)
