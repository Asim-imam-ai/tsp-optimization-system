# app/algorithms/brute_force.py

from itertools import permutations


class BruteForceTSP:

    def __init__(self, distance_matrix):
        self.distance_matrix = distance_matrix
        self.num_cities = len(distance_matrix)

    def calculate_cost(self, route):

        total_cost = 0

        for i in range(len(route) - 1):
            total_cost += self.distance_matrix[
                route[i]
            ][route[i + 1]]

        return total_cost

    def solve(self, start_city=0):

        cities = list(range(self.num_cities))
        cities.remove(start_city)

        best_route = None
        minimum_cost = float("inf")

        for perm in permutations(cities):

            current_route = (
                [start_city]
                + list(perm)
                + [start_city]
            )

            current_cost = self.calculate_cost(
                current_route
            )

            if current_cost < minimum_cost:
                minimum_cost = current_cost
                best_route = current_route

        return best_route, minimum_cost