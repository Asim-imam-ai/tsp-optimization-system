class TablePrinter:

    @staticmethod
    def print_results(results):

        print("\n" + "=" * 75)

        print(
            f"{'Algorithm':<25}"
            f"{'Cost':<15}"
            f"{'Time':<15}"
            f"{'Memory':<15}"
        )

        print("=" * 75)

        for row in results:

            print(
                f"{row['algorithm']:<25}"
                f"{row['cost']:<15.2f}"
                f"{row['time']:<15.6f}"
                f"{row['memory']:<15.6f}"
            )

        print("=" * 75)