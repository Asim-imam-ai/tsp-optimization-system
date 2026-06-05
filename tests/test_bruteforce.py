from app.algorithms.brute_force import (
    BruteForceTSP,
)


def test_bruteforce():

    matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0],
    ]

    solver = BruteForceTSP(matrix)

    route, cost = solver.solve()

    assert cost == 80