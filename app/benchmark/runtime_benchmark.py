# app/benchmark/runtime_benchmark.py

import time

from app.models.benchmark_result import (
    BenchmarkResult,
)


class RuntimeBenchmark:

    @staticmethod
    def measure(
        algorithm_name,
        solver_function,
    ):

        start_time = (
            time.perf_counter()
        )

        route = solver_function()

        end_time = (
            time.perf_counter()
        )

        execution_time = (
            end_time
            - start_time
        )

        return (
            BenchmarkResult(
                algorithm_name=algorithm_name,
                execution_time=execution_time,
                memory_usage=0,
                route_cost=route.cost,
            )
        )