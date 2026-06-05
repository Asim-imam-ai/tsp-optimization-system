# app/benchmark/memory_benchmark.py

import tracemalloc

from app.models.benchmark_result import (
    BenchmarkResult,
)


class MemoryBenchmark:

    @staticmethod
    def measure(
        algorithm_name,
        solver_function,
    ):

        tracemalloc.start()

        route = solver_function()

        current, peak = (
            tracemalloc.get_traced_memory()
        )

        tracemalloc.stop()

        memory_mb = (
            peak
            / 1024
            / 1024
        )

        return (
            BenchmarkResult(
                algorithm_name=algorithm_name,
                execution_time=0,
                memory_usage=memory_mb,
                route_cost=route.cost,
            )
        )