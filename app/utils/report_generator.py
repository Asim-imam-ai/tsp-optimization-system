import pandas as pd


class ReportGenerator:

    @staticmethod
    def create_dataframe(results):

        data = []

        for result in results:

            data.append({
                "Algorithm":
                    result.algorithm_name,

                "Execution Time":
                    result.execution_time,

                "Memory Usage":
                    result.memory_usage,

                "Cost":
                    result.route_cost,
            })

        return pd.DataFrame(data)

    @staticmethod
    def save_csv(df, filepath):

        df.to_csv(
            filepath,
            index=False,
        )
    @staticmethod
    def save_excel(df, filepath):

        df.to_excel(
            filepath,
            index=False,
    )