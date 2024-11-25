
import pytest

from gauss_elim import solve_linear


EXAMPLES = [
    (
        [
            [2, 3, 3, 3],
            [3, -2, -9, 4],
            [5, -1, -18, -1],
        ],
        [3, -2, 1]),
    (
        [
            [1, 2, 3],
            [4, 1, 5],
        ],
        [1, 1],
    ),
    (
        [
            [1, 2, 3],
            [1, 2, 3],
        ],
        [1, 1],
    ),
]

@pytest.mark.parametrize("matrix,expected", EXAMPLES)
def test_solve(matrix, expected):
    result = solve_linear(matrix)
    result = [round(x, 3) for x in result]
    assert result == expected
