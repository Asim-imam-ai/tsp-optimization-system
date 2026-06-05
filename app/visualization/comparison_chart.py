import os
import matplotlib.pyplot as plt


class ComparisonChart:

    @staticmethod
    def plot_cost_comparison(
        algorithm_names,
        costs,
        output_path=None,
    ):

        plt.figure(figsize=(8, 6))

        plt.bar(
            algorithm_names,
            costs,
        )

        plt.title(
            "Algorithm Cost Comparison"
        )

        plt.xlabel("Algorithm")

        plt.ylabel("Route Cost")

        plt.grid(True)

        if output_path:
            os.makedirs(
                os.path.dirname(output_path),
                exist_ok=True,
            )
            plt.tight_layout()
            plt.savefig(
                output_path,
                dpi=300,
                bbox_inches="tight",
            )
        else:
            plt.show()

        plt.close()