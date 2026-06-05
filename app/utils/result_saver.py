
# # import csv
# # import os


# # class ResultSaver:

# #     @staticmethod
# #     def save_csv(
# #         algorithm,
# #         route,
# #         cost,
# #         execution_time,
# #         memory_usage,
# #         filepath,
# #     ):

# #         os.makedirs(
# #             os.path.dirname(filepath),
# #             exist_ok=True,
# #         )

# #         file_exists = os.path.isfile(filepath)

# #         with open(
# #             filepath,
# #             "a",
# #             newline="",
# #             encoding="utf-8",
# #         ) as file:

# #             writer = csv.writer(file)

# #             if not file_exists:
# #                 writer.writerow([
# #                     "Algorithm",
# #                     "Route",
# #                     "Cost",
# #                     "Execution Time (sec)",
# #                     "Memory Usage (MB)",
# #                 ])

# #             writer.writerow([
# #                 algorithm,
# #                 str(route),
# #                 round(cost, 2),
# #                 round(execution_time, 6),
# #                 round(memory_usage, 6),
# #             ])

# #         print(
# #             f"Results saved to: {filepath}"
# #         )



# # import csv
# # import os


# # class ResultSaver:

# #     HEADER = [
# #         "Algorithm",
# #         "Route",
# #         "Cost",
# #         "Execution Time (sec)",
# #         "Memory Usage (MB)",
# #     ]

# #     @staticmethod
# #     def create_new_csv(filepath):
# #         """
# #         Create a fresh CSV file and write header.
# #         Existing file will be overwritten.
# #         """

# #         os.makedirs(
# #             os.path.dirname(filepath),
# #             exist_ok=True,
# #         )

# #         with open(
# #             filepath,
# #             mode="w",
# #             newline="",
# #             encoding="utf-8",
# #         ) as file:

# #             writer = csv.writer(file)

# #             writer.writerow(
# #                 ResultSaver.HEADER
# #             )

# #         print(
# #             f"Created fresh CSV: {filepath}"
# #         )

# #     @staticmethod
# #     def append_result(
# #         filepath,
# #         algorithm,
# #         route,
# #         cost,
# #         execution_time,
# #         memory_usage,
# #     ):
# #         """
# #         Add one algorithm result.
# #         """

# #         with open(
# #             filepath,
# #             mode="a",
# #             newline="",
# #             encoding="utf-8",
# #         ) as file:

# #             writer = csv.writer(file)

# #             writer.writerow([
# #                 algorithm,
# #                 str(route),
# #                 round(cost, 2),
# #                 round(execution_time, 6),
# #                 round(memory_usage, 6),
# #             ])

# #         print(
# #             f"Saved result: {algorithm}"
# #         )



# import csv
# import os


# class ResultSaver:

#     @staticmethod
#     def create_csv(filepath):

#         os.makedirs(
#             os.path.dirname(filepath),
#             exist_ok=True,
#         )

#         with open(
#             filepath,
#             "w",
#             newline="",
#             encoding="utf-8",
#         ) as file:

#             writer = csv.writer(file)

#             writer.writerow([
#                 "Algorithm",
#                 "Route",
#                 "Cost",
#                 "Execution Time",
#                 "Memory Usage",
#             ])



import csv
import os


class ResultSaver:

    @staticmethod
    def create_csv(filepath: str) -> None:
        """
        Creates a fresh CSV file and writes the structural header row.
        Any existing file at the path will be overwritten.
        """
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
            writer.writerow([
                "Algorithm",
                "Route",
                "Cost",
                "Execution Time",
                "Memory Usage",
            ])

        print(f"Created fresh CSV report structure at: {filepath}")

    @staticmethod
    def append_result(
        filepath: str,
        algorithm: str,
        route: list,
        cost: float,
        execution_time: float,
        memory_usage: float,
    ) -> None:
        """
        Appends a single algorithm execution metric row to the designated CSV tracker.
        """
        with open(
            filepath,
            "a",
            newline="",
            encoding="utf-8",
        ) as file:
            writer = csv.writer(file)
            writer.writerow([
                algorithm,
                str(route),
                round(cost, 2),
                round(execution_time, 6),
                round(memory_usage, 6),
            ])

        print(f"Metrics saved cleanly for: {algorithm}")