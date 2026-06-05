from app.algorithms.branch_and_bound import (
    BranchAndBoundTSP,
)


def test_branch_and_bound():

    matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0],
    ]

    solver = BranchAndBoundTSP(
        matrix
    )

    route, cost = solver.solve()

    assert cost == 80