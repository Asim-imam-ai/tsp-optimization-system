# # app/utils/excel_report.py
# import os
# import pandas as pd


# class ExcelReport:

#     @staticmethod
#     def generate(
#         csv_file,
#         excel_file,
#     ):
#         """
#         Convert benchmark CSV
#         into formatted Excel report.
#         """

#         if not os.path.exists(csv_file):
#             raise FileNotFoundError(
#                 f"CSV file not found: {csv_file}"
#             )

#         df = pd.read_csv(csv_file)
#         df.columns = df.columns.str.strip()
        
#         print("columns are found")
#         print(df.columns.tolist())
        

#         os.makedirs(
#             os.path.dirname(excel_file),
#             exist_ok=True,
#         )

#         with pd.ExcelWriter(
#             excel_file,
#             engine="openpyxl",
#         ) as writer:

#             # Main Results Sheet
#             df.to_excel(
#                 writer,
#                 sheet_name="Benchmark Results",
#                 index=False,
#             )

#             # Summary Sheet
#             summary = pd.DataFrame(
#                 {
#                     "Metric": [
#                         "Total Experiments",
#                         "Best Cost",
#                         "Worst Cost",
#                         "Fastest Time",
#                         "Highest Memory",
#                     ],
#                     "Value": [
#                         len(df),
#                         df["Cost"].min(),
#                         df["Cost"].max(),
#                         df["Execution Time (sec)"].min(),
#                         df["Memory Usage (MB)"].max(),
#                     ],
#                 }
#             )

#             summary.to_excel(
#                 writer,
#                 sheet_name="Summary",
#                 index=False,
#             )

#         print(
#             f"Excel report saved: "
#             f"{excel_file}"
#         )



import os
import pandas as pd


class ExcelReport:

    @staticmethod
    def generate(
        csv_file,
        excel_file,
    ):

        if not os.path.exists(csv_file):
            print(
                f"CSV not found: {csv_file}"
            )
            return

        try:

            df = pd.read_csv(csv_file)

            # Remove accidental spaces
            df.columns = (
                df.columns.str.strip()
            )

            print("\nColumns Found:")
            print(df.columns.tolist())

            # Validate required columns
            required_columns = [
                "Algorithm",
                "Route",
                "Cost",
                "Execution Time",
                "Memory Usage",
            ]

            for column in required_columns:

                if column not in df.columns:

                    raise ValueError(
                        f"Missing column: {column}"
                    )

            # Summary statistics
            summary_df = pd.DataFrame(
                {
                    "Metric": [
                        "Minimum Cost",
                        "Maximum Cost",
                        "Average Cost",
                        "Minimum Time",
                        "Maximum Time",
                        "Average Time",
                    ],
                    "Value": [
                        df["Cost"].min(),
                        df["Cost"].max(),
                        df["Cost"].mean(),
                        df["Execution Time"].min(),
                        df["Execution Time"].max(),
                        df["Execution Time"].mean(),
                    ],
                }
            )

            os.makedirs(
                os.path.dirname(excel_file),
                exist_ok=True,
            )

            with pd.ExcelWriter(
                excel_file,
                engine="openpyxl",
            ) as writer:

                df.to_excel(
                    writer,
                    sheet_name="Results",
                    index=False,
                )

                summary_df.to_excel(
                    writer,
                    sheet_name="Summary",
                    index=False,
                )

            print(
                f"Excel report saved: {excel_file}"
            )

        except Exception as e:

            print(
                f"Excel generation failed: {e}"
            )