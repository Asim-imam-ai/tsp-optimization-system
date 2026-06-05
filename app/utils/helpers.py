# app/utils/helpers.py

from typing import List


def calculate_route_cost(
    route: List[int],
    distance_matrix: List[List[float]],
) -> float:
    """
    Calculate total route cost
    """

    total_cost = 0.0

    for i in range(len(route) - 1):
        total_cost += distance_matrix[
            route[i]
        ][route[i + 1]]

    return total_cost


def format_execution_time(
    seconds: float,
) -> str:
    return f"{seconds:.6f} sec"


def format_memory(
    memory_mb: float,
) -> str:
    return f"{memory_mb:.2f} MB"