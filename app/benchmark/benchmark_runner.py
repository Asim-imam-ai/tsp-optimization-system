import time
import tracemalloc
import pandas as pd

from app.models.benchmark_result import BenchmarkResult


class BenchmarkRunner:

    @staticmethod
    def run(
        algorithm_name,
        algorithm_function,
    ):

        tracemalloc.start()

        start_time = time.perf_counter()

        route = algorithm_function()

        end_time = time.perf_counter()

        current, peak = tracemalloc.get_traced_memory()

        tracemalloc.stop()

        execution_time = end_time - start_time

        memory_mb = peak / (1024 * 1024)

        return BenchmarkResult(
            algorithm_name=algorithm_name,
            execution_time=execution_time,
            memory_usage=memory_mb,
            route_cost=route.cost,
        )