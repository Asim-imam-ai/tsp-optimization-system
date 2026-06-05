# app/benchmark/scalability_test.py

import time

from app.services.route_generator import (
    RouteGenerator,
)

from app.services.distance_calculator import (
    DistanceCalculator,
)

from app.services.tsp_solver import (
    TSPSolver,
)


class ScalabilityTest:

    @staticmethod
    def run():

        city_sizes = [
            5,
            8,
            10,
            12,
        ]

        results = []

        for size in city_sizes:

            cities = (
                RouteGenerator.generate_random_cities(
                    size
                )
            )

            matrix = (
                DistanceCalculator.create_distance_matrix(
                    cities
                )
            )

            solver = TSPSolver(
                matrix
            )

            start = time.perf_counter()

            result = (
                solver.solve_greedy()
            )

            end = time.perf_counter()

            results.append(
                {
                    "cities": size,
                    "time": (
                        end - start
                    ),
                    "cost": result.cost,
                }
            )

        return results