
from copy import deepcopy
import numpy as np

def solve_linear(data: list[float]) -> list[float]:
    """solves linear equations with the Gauss Elimination method"""
    nrows = len(data)
    ncols = len(data[0])
    M = deepcopy(data)
    for i in range(ncols - 1):
        # normalize each row by position i
        for row in M[i:]:
            first = row[i]
            for j in range(i, ncols):
                row[j] = row[j] / first
        # subtract equation i from all
        for j in range(i + 1, nrows):
            for k in range(i, ncols):
                M[j][k] -= M[i][k]
    
    # retrieve coefficients from triangular form
    coef = [0.0] * nrows
    for i in range(nrows - 1, -1, -1):  # process rows in reverse order
        temp = 0.0
        for j in range(i + 1, ncols - 1):
            temp -= M[i][j] * coef[j]
        temp += M[i][-1]
        coef[i] = temp

    return coef


def create_linear_equation_sys(size):
    """creates a solvable linear equation system"""
    A = np.random.rand(size, size)
    # Ensure matrix A is invertible by checking the determinant
    while np.linalg.det(A) == 0:
        A = np.random.rand(size, size)

    solution = np.random.randint(-100, 100, size=size)  # random solution vector

    b = np.dot(A, solution)  # right-hand-side vector

    mtx = np.hstack([A, b.reshape(-1, 1)])
    return mtx

def round_output(v, digits=3):
    return [round(x, digits) for x in v]

if __name__ == '__main__':
    # solve subsequent tasks (slow)
    tasks = [create_linear_equation_sys(200) for _ in range(10)]
    for i, M in enumerate(tasks, 1):
        print(f"\ntask {i}")
        result = round_output(solve_linear(M))
        print("done")
