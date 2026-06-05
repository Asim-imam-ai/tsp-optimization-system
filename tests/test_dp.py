from app.algorithms.dynamic_programming import (
    DynamicProgrammingTSP,
)


def test_dynamic_programming():

    matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0],
    ]

    solver = DynamicProgrammingTSP(
        matrix
    )

    route, cost = solver.solve()

    assert cost == 80