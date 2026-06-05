import math
from typing import List

from app.models.city import City


class DistanceCalculator:

    @staticmethod
    def calculate_distance(
        city1: City,
        city2: City,
    ) -> float:

        return math.sqrt(
            (city1.x - city2.x) ** 2
            + (city1.y - city2.y) ** 2
        )

    @staticmethod
    def create_distance_matrix(
        cities: List[City],
    ):

        n = len(cities)

        matrix = [
            [0.0 for _ in range(n)]
            for _ in range(n)
        ]

        for i in range(n):
            for j in range(n):

                if i != j:
                    matrix[i][j] = (
                        DistanceCalculator.calculate_distance(
                            cities[i],
                            cities[j],
                        )
                    )

        return matrix