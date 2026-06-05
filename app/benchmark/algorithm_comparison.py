from app.benchmark.benchmark_runner import (
    BenchmarkRunner,
)


class AlgorithmComparison:

    @staticmethod
    def compare(solver):

        results = []

        results.append(
            BenchmarkRunner.run(
                "Greedy",
                solver.solve_greedy,
            )
        )

        results.append(
            BenchmarkRunner.run(
                "Brute Force",
                solver.solve_brute_force,
            )
        )

        results.append(
            BenchmarkRunner.run(
                "Dynamic Programming",
                solver.solve_dynamic_programming,
            )
        )

        results.append(
            BenchmarkRunner.run(
                "Branch and Bound",
                solver.solve_branch_and_bound,
            )
        )

        return results