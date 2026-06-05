# from app.benchmark.runtime_benchmark import RuntimeBenchmark
# from app.benchmark.memory_benchmark import MemoryBenchmark


# class ComparisonService:

#     @staticmethod
#     def compare_all(solver):

#         algorithms = {
#             "Greedy": solver.solve_greedy,
#             "Brute Force": solver.solve_brute_force,
#             "Dynamic Programming": solver.solve_dynamic_programming,
#             "Branch and Bound": solver.solve_branch_and_bound,
#         }

#         results = []

#         for name, func in algorithms.items():

#             route_result = func()

#             runtime = RuntimeBenchmark.measure(
#                 name,
#                 func,
#             )

#             memory = MemoryBenchmark.measure(
#                 name,
#                 func,
#             )

#             results.append(
#                 {
#                     "algorithm": name,
#                     "route": route_result.path,
#                     "cost": route_result.cost,
#                     "time": runtime.execution_time,
#                     "memory": memory.memory_usage,
#                 }
#             )

#         return results



# import time
# from app.benchmark.runtime_benchmark import RuntimeBenchmark
# from app.benchmark.memory_benchmark import MemoryBenchmark


# class ComparisonService:

#     @staticmethod
#     def compare_all(solver):

#         results = []

#         algorithms = [
#             ("Greedy", solver.solve_greedy),
#             ("Brute Force", solver.solve_brute_force),
#             ("Dynamic Programming", solver.solve_dynamic_programming),
#             ("Branch & Bound", solver.solve_branch_and_bound),
#         ]

#         for name, func in algorithms:

#             start_time = time.time()

#             result = func()

#             end_time = time.time()

#             execution_time = end_time - start_time

#             memory = MemoryBenchmark.measure(
#                 name,
#                 func,
#             )

#             # Return a plain dict so existing consumers (reports, printers)
#             # that expect mapping keys like 'algorithm', 'cost', 'time', 'memory'
#             # continue to work without changes.
#             results.append(
#                 {
#                     "algorithm": name,
#                     "route": list(result.path),
#                     "cost": float(result.cost),
#                     "time": execution_time,
#                     "memory": memory.memory_usage,
#                 }
#             )

#         return results


import time
from app.benchmark.runtime_benchmark import RuntimeBenchmark
from app.benchmark.memory_benchmark import MemoryBenchmark


class ComparisonService:

    @staticmethod
    def compare_all(solver):

        results = []

        algorithms = [
            ("Greedy", solver.solve_greedy),
            ("Brute Force", solver.solve_brute_force),
            ("Dynamic Programming", solver.solve_dynamic_programming),
            ("Branch & Bound", solver.solve_branch_and_bound),
        ]

        for name, func in algorithms:

            start_time = time.time()

            result = func()

            end_time = time.time()

            execution_time = end_time - start_time

            memory = MemoryBenchmark.measure(
                name,
                func,
            )

            # Return a plain dict so existing consumers (reports, printers)
            # that expect mapping keys like 'algorithm', 'cost', 'time', 'memory'
            # continue to work without changes.
            results.append(
                {
                    "algorithm": name,
                    "route": list(result.path),
                    "cost": float(result.cost),
                    "time": execution_time,
                    "memory": memory.memory_usage,
                }
            )

        return results