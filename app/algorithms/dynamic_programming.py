# app/algorithms/dynamic_programming.py

from functools import lru_cache


class DynamicProgrammingTSP:

    def __init__(self, distance_matrix):
        self.distance_matrix = distance_matrix
        self.num_cities = len(distance_matrix)

    def solve(self, start_city=0):

        @lru_cache(maxsize=None)
        def tsp(current_city, visited_mask):

            if visited_mask == (
                1 << self.num_cities
            ) - 1:

                return (
                    self.distance_matrix[
                        current_city
                    ][start_city],
                    [start_city],
                )

            minimum_cost = float("inf")
            best_path = []

            for next_city in range(
                self.num_cities
            ):

                if visited_mask & (
                    1 << next_city
                ):
                    continue

                cost, path = tsp(
                    next_city,
                    visited_mask | (
                        1 << next_city
                    ),
                )

                total_cost = (
                    self.distance_matrix[
                        current_city
                    ][next_city]
                    + cost
                )

                if total_cost < minimum_cost:

                    minimum_cost = total_cost

                    best_path = [
                        next_city
                    ] + path

            return minimum_cost, best_path

        cost, path = tsp(
            start_city,
            1 << start_city,
        )

        route = [start_city] + path

        return route, cost