from app.algorithms.greedy import GreedyTSP


def test_greedy():

    matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0],
    ]

    solver = GreedyTSP(matrix)

    route, cost = solver.solve()

    assert route[0] == 0
    assert route[-1] == 0
    assert cost > 0