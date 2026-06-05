# app/utils/matrix_generator.py

from app.services.distance_calculator import (
    DistanceCalculator,
)


class MatrixGenerator:

    @staticmethod
    def generate(
        cities,
    ):
        return (
            DistanceCalculator.create_distance_matrix(
                cities
            )
        )