import os
import matplotlib.pyplot as plt


class ComparisonChart:

    @staticmethod
    def execution_time_chart(
        algorithms,
        execution_times,
        output_path,
    ):
        """
        Compare algorithm execution times.
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
            "TSP Algorithm Comparison"
        )

        plt.xlabel(
            "Algorithms"
        )

        plt.ylabel(
            "Execution Time (seconds)"
        )

        plt.grid(
            axis="y"
        )

        plt.savefig(
            output_path,
            dpi=300,
            bbox_inches="tight",
        )

        print(
            f"Comparison graph saved -> {output_path}"
        )

        plt.show()

        plt.close()