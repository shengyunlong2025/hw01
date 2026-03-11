import pytest
from hw01.src.solver import EightQueensSolver

@pytest.mark.parametrize("n, expected_count", [
    (4, 2),
    (5, 10),
    (8, 92)
])
def test_n_queens_solution_count(n, expected_count):
    solver = EightQueensSolver(n)
    solutions = solver.solve()
    assert len(solutions) == expected_count

def test_solution_validity():
    solver = EightQueensSolver(8)
    solutions = solver.solve()
    for sol in solutions:
        n = len(sol)
        for i in range(n):
            for j in range(i+1, n):
                assert sol[i] != sol[j]
                assert abs(sol[i] - sol[j]) != j - i

