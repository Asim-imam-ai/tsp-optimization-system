import sys
from pathlib import Path

import streamlit as st  # type: ignore[import]
import pandas as pd

# Ensure repository root is on sys.path when Streamlit loads this file directly.
ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from app.services.tsp_solver import TSPSolver
from app.services.distance_calculator import DistanceCalculator
from app.services.route_generator import RouteGenerator
from app.services.comparison_service import ComparisonService
from app.utils.csv_loader import CSVLoader
from app.utils.report_generator import ReportGenerator
from app.visualization.route_plot import RoutePlot
from app.visualization.performance_chart import PerformanceChart
from app.visualization.comparison_chart import ComparisonChart


st.set_page_config(
    page_title="TSP Optimization System",
    layout="wide"
)

st.title("🚀 TSP Optimization Dashboard")

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.header("Settings")

input_mode = st.sidebar.selectbox(
    "Input Type",
    ["Random Cities", "CSV Dataset"]
)

num_cities = st.sidebar.slider(
    "Number of Cities (Random)",
    5, 30, 10
)

run_type = st.sidebar.selectbox(
    "Mode",
    ["Single Algorithm", "Full Comparison"]
)

algorithm = st.sidebar.selectbox(
    "Algorithm",
    ["Greedy", "Brute Force", "Dynamic Programming", "Branch and Bound"]
)

# -----------------------------
# LOAD CITIES
# -----------------------------
if input_mode == "Random Cities":
    cities = RouteGenerator.generate_random_cities(num_cities)

else:
    file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

    if file:
        cities = CSVLoader.load(file)
    else:
        st.warning("Upload CSV file")
        st.stop()

# -----------------------------
# SOLVER
# -----------------------------
distance_matrix = DistanceCalculator.create_distance_matrix(cities)
solver = TSPSolver(distance_matrix)

# -----------------------------
# RUN BUTTON
# -----------------------------
if st.button("🚀 Run TSP"):

    st.info("Processing...")

    # ---------------- SINGLE ALGO ----------------
    if run_type == "Single Algorithm":

        if algorithm == "Greedy":
            result = solver.solve_greedy()

        elif algorithm == "Brute Force":
            result = solver.solve_brute_force()

        elif algorithm == "Dynamic Programming":
            result = solver.solve_dynamic_programming()

        else:
            result = solver.solve_branch_and_bound()

        st.success("Done!")

        st.write("### 📊 Result")
        st.write("Cost:", result.cost)
        st.write("Route:", result.path)

        # Save + Show Plot
        RoutePlot.plot_route(
            cities,
            result.path,
            "TSP Route",
            "outputs/routes/streamlit_route.png",
            show=False
        )

        st.image("outputs/routes/streamlit_route.png")

    # ---------------- FULL COMPARISON ----------------
    else:

        results = ComparisonService.compare_all(solver)

        df = pd.DataFrame(results)

        st.write("### 📊 Comparison Table")
        st.dataframe(df)

        ReportGenerator.save_csv(df, "outputs/reports/streamlit_results.csv")
        ReportGenerator.save_excel(df, "outputs/reports/streamlit_results.xlsx")

        algorithms = [row["algorithm"] for row in results]
        execution_times = [row["time"] for row in results]
        memory_values = [row["memory"] for row in results]
        costs = [row["cost"] for row in results]

        PerformanceChart.execution_time_chart(
            algorithms,
            execution_times,
            "outputs/graphs/execution_time.png",
        )

        PerformanceChart.memory_usage_chart(
            algorithms,
            memory_values,
            "outputs/graphs/memory_usage.png",
        )

        ComparisonChart.plot_cost_comparison(
            algorithms,
            costs,
            "outputs/graphs/cost_comparison.png",
        )

        st.write("### 📈 Execution Time")
        st.image("outputs/graphs/execution_time.png")

        st.write("### 🧠 Memory Usage")
        st.image("outputs/graphs/memory_usage.png")

        st.write("### 💰 Cost Comparison")
        st.image("outputs/graphs/cost_comparison.png")