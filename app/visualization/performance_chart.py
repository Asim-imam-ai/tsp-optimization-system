# import matplotlib.pyplot as plt


# class PerformanceChart:

#     @staticmethod
#     def execution_time_chart(
#         city_counts,
#         execution_times,
#         algorithm_name,
#     ):

#         plt.figure(figsize=(8, 6))

#         plt.plot(
#             city_counts,
#             execution_times,
#             marker="o",
#         )

#         plt.title(
#             f"{algorithm_name} Execution Time"
#         )

#         plt.xlabel("Number of Cities")

#         plt.ylabel("Time (seconds)")

#         plt.grid(True)

#         plt.show()

#     @staticmethod
#     def memory_chart(
#         city_counts,
#         memory_usage,
#         algorithm_name,
#     ):

#         plt.figure(figsize=(8, 6))

#         plt.plot(
#             city_counts,
#             memory_usage,
#             marker="o",
#         )

#         plt.title(
#             f"{algorithm_name} Memory Usage"
#         )

#         plt.xlabel("Number of Cities")

#         plt.ylabel("Memory (MB)")

#         plt.grid(True)

#         plt.show()









# import matplotlib.pyplot as plt


# class PerformanceChart:

#     @staticmethod
#     def execution_time_chart(
#         results,
#         output_path,
#     ):

#         algorithms = [
#             r.algorithm_name
#             for r in results
#         ]

#         times = [
#             r.execution_time
#             for r in results
#         ]

#         plt.figure(figsize=(10, 6))

#         plt.bar(
#             algorithms,
#             times,
#         )

#         plt.title(
#             "Execution Time Comparison"
#         )

#         plt.xlabel(
#             "Algorithms"
#         )

#         plt.ylabel(
#             "Time (Seconds)"
#         )

#         plt.grid(True)

#         plt.savefig(
#             output_path,
#             dpi=300,
#             bbox_inches="tight",
#         )

#         plt.close()



# import os
# import matplotlib.pyplot as plt


# class PerformanceChart:

#     @staticmethod
#     def execution_time_chart(
#         algorithms,
#         execution_times,
#         output_path,
#         show=True,
#     ):
#         """
#         Create execution time comparison chart.

#         Parameters
#         ----------
#         algorithms : list[str]

#         execution_times : list[float]

#         output_path : str

#         show : bool
#         """

#         os.makedirs(
#             os.path.dirname(output_path),
#             exist_ok=True,
#         )

#         plt.figure(
#             figsize=(10, 6)
#         )

#         plt.bar(
#             algorithms,
#             execution_times,
#         )

#         plt.title(
#             "Execution Time Comparison"
#         )

#         plt.xlabel(
#             "Algorithms"
#         )

#         plt.ylabel(
#             "Execution Time (seconds)"
#         )

#         plt.grid(
#             axis="y"
#         )

#         plt.tight_layout()

#         plt.savefig(
#             output_path,
#             dpi=300,
#             bbox_inches="tight",
#         )

#         print(
#             f"Execution time graph saved: "
#             f"{output_path}"
#         )

#         if show:
#             plt.show()

#         plt.close()



# import os
# import matplotlib.pyplot as plt


# class PerformanceChart:

#     @staticmethod
#     def memory_usage_chart(
#         algorithms,
#         memory_values,
#         output_path,
#     ):
#         """
#         Create memory usage bar chart.
#         """

#         os.makedirs(
#             os.path.dirname(output_path),
#             exist_ok=True,
#         )

#         plt.figure(figsize=(10, 6))

#         plt.bar(
#             algorithms,
#             memory_values,
#         )

#         plt.title(
#             "Memory Usage Comparison"
#         )

#         plt.xlabel(
#             "Algorithms"
#         )

#         plt.ylabel(
#             "Memory Usage (MB)"
#         )

#         plt.grid(
#             axis="y"
#         )

#         plt.savefig(
#             output_path,
#             dpi=300,
#             bbox_inches="tight",
#         )

#         print(
#             f"Memory graph saved -> {output_path}"
#         )

#         plt.show()

#         plt.close()



import os
import matplotlib.pyplot as plt


class PerformanceChart:

    @staticmethod
    def execution_time_chart(
        algorithms,
        execution_times,
        output_path,
    ):
        """
        Create execution time graph.
        """

        os.makedirs(
            os.path.dirname(output_path),
            exist_ok=True,
        )

        plt.figure(figsize=(10, 6))

        plt.bar(
            algorithms,
            execution_times,
        )

        plt.title(
            "Execution Time Comparison"
        )

        plt.xlabel(
            "Algorithms"
        )

        plt.ylabel(
            "Execution Time (Seconds)"
        )

        plt.grid(axis="y")

        plt.tight_layout()

        plt.savefig(
            output_path,
            dpi=300,
            bbox_inches="tight",
        )

        print(
            f"Execution time graph saved -> {output_path}"
        )

        plt.show()

        plt.close()

    @staticmethod
    def memory_usage_chart(
        algorithms,
        memory_values,
        output_path,
    ):
        """
        Create memory usage graph.
        """

        os.makedirs(
            os.path.dirname(output_path),
            exist_ok=True,
        )

        plt.figure(figsize=(10, 6))

        plt.bar(
            algorithms,
            memory_values,
        )

        plt.title(
            "Memory Usage Comparison"
        )

        plt.xlabel(
            "Algorithms"
        )

        plt.ylabel(
            "Memory Usage (MB)"
        )

        plt.grid(axis="y")

        plt.tight_layout()

        plt.savefig(
            output_path,
            dpi=300,
            bbox_inches="tight",
        )

        print(
            f"Memory graph saved -> {output_path}"
        )

        plt.show()

        plt.close()