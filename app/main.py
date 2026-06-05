
# from app.services import (
#     RouteGenerator,
#     DistanceCalculator,
#     TSPSolver,
# )

# from app.visualization import RoutePlot
# from app.visualization.performance_chart import PerformanceChart
# from app.visualization.comparison_chart import ComparisonChart

# from app.services.comparison_service import ComparisonService
# from app.utils.result_saver import ResultSaver
# from app.utils.logger import Logger
# from app.utils.table_printer import TablePrinter
# from app.utils.excel_report import ExcelReport
# from app.utils.csv_loader import CSVLoader


# def run():

#     Logger.info("TSP Project Started")

#     # STEP 1: Generate Cities
#     cities = RouteGenerator.generate_random_cities(10)

#     # STEP 2: Distance Matrix
#     distance_matrix = DistanceCalculator.create_distance_matrix(cities)

#     # STEP 3: Solver
#     solver = TSPSolver(distance_matrix)

#     # MENU
#     print("\n===== TSP MENU =====")
#     print("1. Greedy")
#     print("2. Brute Force")
#     print("3. Dynamic Programming")
#     print("4. Branch and Bound")
#     print("5. Compare All Algorithms")

#     choice = input("\nSelect Algorithm: ")

#     # -----------------------------
#     # SINGLE ALGORITHM MODE
#     # -----------------------------

#     if choice in ["1", "2", "3", "4"]:
#         # Ensure algorithm variable is always defined to avoid possible unbound errors
#         algorithm = "Unknown"
#         result = None

#         if choice == "1":
#             result = solver.solve_greedy()
#             algorithm = "Greedy"

#         elif choice == "2":
#             result = solver.solve_brute_force()
#             algorithm = "Brute Force"

#         elif choice == "3":
#             result = solver.solve_dynamic_programming()
#             algorithm = "Dynamic Programming"

#         elif choice == "4":
#             result = solver.solve_branch_and_bound()
#             algorithm = "Branch & Bound"

#         if result is None:
#             Logger.error("No solution was produced by the selected algorithm.")
#             print("\nNo result available. Please try again.")
#             return

#         # Print result
#         print("\n===== RESULT =====")
#         print(f"Algorithm : {algorithm}")
#         print(f"Route     : {result.path}")
#         print(f"Cost      : {result.cost:.2f}")

#         # Save route image
#         RoutePlot.plot_route(
#             cities,
#             result.path,
#             f"{algorithm} Route",
#             f"outputs/routes/{algorithm.lower().replace(' ', '_')}_route.png",
#         )

#         # Save CSV
#         csv_path = "outputs/reports/benchmark_results.csv"

#         # ResultSaver may not accept positional args in constructor
#         saver = ResultSaver()
#         # pass csv path to create_csv/append_result to be compatible with both designs
#         saver.create_csv(csv_path)
#         saver.append_result(
#             algorithm=algorithm,
#             route=result.path,
#             cost=result.cost,
#             execution_time=0.0,
#             memory_usage=0.0,
#             filepath=csv_path,
#         )

#         # Excel report
#         ExcelReport.generate(
#             csv_file=csv_path,
#             excel_file="outputs/reports/experiment_summary.xlsx",
#         )

#         Logger.info(f"{algorithm} executed successfully")

#     # -----------------------------
#     # COMPARE ALL MODE
#     # -----------------------------

#     elif choice == "5":

#         results = ComparisonService.compare_all(solver)

#         # Print table
#         TablePrinter.print_results(results)

#         # Save CSV
#         csv_path = "outputs/reports/benchmark_results.csv"
#         saver = ResultSaver()
#         saver.create_csv(csv_path)
#         for result in results:
#             saver.append_result(
#                 algorithm=result["algorithm"],
#                 route=result["route"],
#                 cost=result["cost"],
#                 execution_time=result["time"],
#                 memory_usage=result["memory"],
#                 filepath=csv_path,
#             )

#         # Save Excel
#         ExcelReport.generate(
#             csv_file=csv_path,
#             excel_file="outputs/reports/experiment_summary.xlsx",
#         )

#         # REAL DATA extraction (IMPORTANT FIX)
#         algorithms = [r["algorithm"] for r in results]
#         execution_times = [r["time"] for r in results]
#         memory_values = [r["memory"] for r in results]
#         costs = [r["cost"] for r in results]

#         # 1. Execution Time Graph
#         PerformanceChart.execution_time_chart(
#             algorithms,
#             execution_times,
#             "outputs/graphs/execution_time.png",
#         )

#         # 2. Memory Usage Graph
#         PerformanceChart.memory_usage_chart(
#             algorithms,
#             memory_values,
#             "outputs/graphs/memory_usage.png",
#         )

#         # 3. Cost Comparison Graph
#         ComparisonChart.plot_cost_comparison(
#             algorithms,
#             costs,
#         )

#         Logger.info("All algorithms compared successfully")

#     else:
#         print("Invalid Choice")


# if __name__ == "__main__":
#     run()



import time
from app.services import (
    RouteGenerator,
    DistanceCalculator,
    TSPSolver,
)

from app.visualization import RoutePlot
from app.visualization.performance_chart import PerformanceChart
from app.visualization.comparison_chart import ComparisonChart

from app.services.comparison_service import ComparisonService
from app.utils.result_saver import ResultSaver
from app.utils.logger import Logger
from app.utils.table_printer import TablePrinter
from app.utils.excel_report import ExcelReport

# Custom components for dataset loading and profiling
from app.utils.csv_loader import CSVLoader
from app.benchmark.memory_benchmark import MemoryBenchmark



def run():
    Logger.info("TSP Project Started")

    # ==========================================
    # PHASE 1: DATA INGESTION SELECTION
    # ==========================================
    print("\n===== DATA INPUT SELECTION =====")
    print("1. Generate Random City Coordinates")
    print("2. Load Static CSV Dataset File")
    
    input_choice = input("\nSelect Input Data Source (1/2): ").strip()
    cities = []

    if input_choice == "1":
        cities = RouteGenerator.generate_random_cities(10)
        Logger.info("Generated 10 random node coordinates.")
        
    elif input_choice == "2":
        filepath = input("Enter relative or full path to the CSV dataset: ").strip()
        try:
            cities = CSVLoader.load(filepath)
        except Exception as e:
            print(f"\n❌ Ingestion failure: {str(e)}")
            return
    else:
        print("\n❌ Invalid data choice. Halting execution.")
        return

    # Matrix Calculations
    distance_matrix = DistanceCalculator.create_distance_matrix(cities)

    # Instantiate Solver Core
    solver = TSPSolver(distance_matrix)

    # ==========================================
    # PHASE 2: ALGORITHM TUNING MENU
    # ==========================================
    print("\n===== TSP EXECUTION MENU =====")
    print("1. Greedy")
    print("2. Brute Force")
    print("3. Dynamic Programming")
    print("4. Branch and Bound")
    print("5. Compare All Algorithms")
  

    choice = input("\nSelect Operational Mode: ").strip()

    # -----------------------------
    # SINGLE ALGORITHM PROCESSING MODE
    # -----------------------------
    if choice in ["1", "2", "3", "4"]:
        algorithm = "Unknown"
        func = None

        if choice == "1":
            func = solver.solve_greedy
            algorithm = "Greedy"
        elif choice == "2":
            func = solver.solve_brute_force
            algorithm = "Brute Force"
        elif choice == "3":
            func = solver.solve_dynamic_programming
            algorithm = "Dynamic Programming"
        elif choice == "4":
            func = solver.solve_branch_and_bound
            algorithm = "Branch & Bound"

        if func is None:
            Logger.error("Target execution function mapping failed.")
            return

        # Profile runtime metrics cleanly
        start_time = time.time()
        result = func()
        end_time = time.time()
        execution_time = end_time - start_time

        # Profile memory usage state
        memory = MemoryBenchmark.measure(algorithm, func)

        # Print layout summaries to shell
        print("\n===== RESULT PROFILES =====")
        print(f"Algorithm       : {algorithm}")
        print(f"Optimal Path    : {result.path}")
        print(f"Computed Cost   : {result.cost:.2f}")
        print(f"Execution Time  : {execution_time:.6f} sec")
        print(f"Memory Footprint: {memory.memory_usage:.6f} MB")

        # Save geographical trajectory plot
        RoutePlot.plot_route(
            cities,
            result.path,
            f"{algorithm} Route",
            f"outputs/routes/{algorithm.lower().replace(' ', '_')}_route.png",
        )

        # Save Metrics using clean static methods
        csv_path = "outputs/reports/benchmark_results.csv"
        ResultSaver.create_csv(csv_path)
        ResultSaver.append_result(
            filepath=csv_path,
            algorithm=algorithm,
            route=result.path,
            cost=result.cost,
            execution_time=execution_time,
            memory_usage=memory.memory_usage,
        )

        # Build dynamic Spreadsheet representation
        ExcelReport.generate(
            csv_file=csv_path,
            excel_file="outputs/reports/experiment_summary.xlsx",
        )

        Logger.info(f"{algorithm} individual engine cycle completed.")

    # -----------------------------
    # COMPARATIVE EXPERIMENT TESTING MODE (FIXED FOR DICTIONARIES)
    # -----------------------------
    elif choice == "5":
        results = ComparisonService.compare_all(solver)

        # Print layout table to terminal
        TablePrinter.print_results(results)

        # Process automated output pipelines
        csv_path = "outputs/reports/benchmark_results.csv"
        ResultSaver.create_csv(csv_path)
        
        # FIXED: Using dictionary lookup notation r[...] instead of object attribute r....
        for r in results:
            ResultSaver.append_result(
                filepath=csv_path,
                algorithm=r["algorithm"],
                route=r["route"],
                cost=r["cost"],
                execution_time=r["time"],
                memory_usage=r["memory"],
            )

        # Sync data summaries to spreadsheet
        ExcelReport.generate(
            csv_file=csv_path,
            excel_file="outputs/reports/experiment_summary.xlsx",
        )

        # FIXED: Extract data correctly via dictionary lookup keys for charting utilities
        algorithms = [r["algorithm"] for r in results]
        execution_times = [r["time"] for r in results]
        memory_values = [r["memory"] for r in results]
        costs = [r["cost"] for r in results]

        # 1. Generate runtime complexity metrics graph
        PerformanceChart.execution_time_chart(
            algorithms,
            execution_times,
            "outputs/graphs/execution_time.png",
        )

        # 2. Generate memory allocation overhead graph
        PerformanceChart.memory_usage_chart(
            algorithms,
            memory_values,
            "outputs/graphs/memory_usage.png",
        )

        # 3. Generate combinatorial cost variance comparison graph
        ComparisonChart.plot_cost_comparison(
            algorithms,
            costs,
        )

        Logger.info("Aggregated comparative matrix execution completed successfully.")

    else:
        print("❌ Choice option not mapped within terminal menu scopes.")


if __name__ == "__main__":
    run()