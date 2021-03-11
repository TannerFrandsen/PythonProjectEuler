from ProjectEuler.problem_006.problem006 import calculate_solution


def test_problem_005_example():
    assert(2640 == calculate_solution(1, 10))


def test_problem_005_solution():
    assert(25164150 == calculate_solution(1, 100))
