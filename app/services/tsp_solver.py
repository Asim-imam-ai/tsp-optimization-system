from app.algorithms.greedy import GreedyTSP
from app.algorithms.brute_force import BruteForceTSP
from app.algorithms.dynamic_programming import (
    DynamicProgrammingTSP,
)
from app.algorithms.branch_and_bound import (
    BranchAndBoundTSP,
)

from app.models.route import Route


class TSPSolver:

    def __init__(self, distance_matrix):

        self.distance_matrix = distance_matrix

    def solve_greedy(self):

        solver = GreedyTSP(
            self.distance_matrix
        )

        path, cost = solver.solve()

        if path is None:
            path = []

        return Route(path, cost)

    def solve_brute_force(self):

        solver = BruteForceTSP(
            self.distance_matrix
        )

        path, cost = solver.solve()

        if path is None:
            path = []

        return Route(path, cost)

    def solve_dynamic_programming(self):

        solver = DynamicProgrammingTSP(
            self.distance_matrix
        )

        path, cost = solver.solve()

        if path is None:
            path = []

        return Route(path, cost)

    def solve_branch_and_bound(self):

        solver = BranchAndBoundTSP(
            self.distance_matrix
        )

        path, cost = solver.solve()

        if path is None:
            path = []

        return Route(path, cost)