import csv
import os


class ComparisonReport:

    @staticmethod
    def save_csv(
        results,
        filepath="outputs/reports/benchmark_results.csv",
    ):

        os.makedirs(
            os.path.dirname(filepath),
            exist_ok=True,
        )

        with open(
            filepath,
            "w",
            newline="",
            encoding="utf-8",
        ) as file:

            writer = csv.writer(file)

            writer.writerow(
                [
                    "Algorithm",
                    "Cost",
                    "Execution Time (sec)",
                    "Memory Usage (MB)",
                ]
            )

            for row in results:

                writer.writerow(
                    [
                        row["algorithm"],
                        round(row["cost"], 2),
                        round(row["time"], 6),
                        round(row["memory"], 6),
                    ]
                )

        print(
            f"\nCSV Saved -> {filepath}"
        )