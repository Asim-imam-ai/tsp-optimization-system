import csv
import io
import os


class City:

    def __init__(self, city_id, x, y):
        self.city_id = int(city_id)
        self.x = float(x)
        self.y = float(y)


class CSVLoader:

    @staticmethod
    def load(filepath):
        """
        Load cities from CSV file or file-like object.
        """

        if hasattr(filepath, "read"):
            file_obj = filepath
            if isinstance(file_obj.read(0), bytes):
                file_obj = io.TextIOWrapper(
                    filepath,
                    encoding="utf-8",
                )
        else:
            if not os.path.exists(filepath):
                raise FileNotFoundError(
                    f"CSV file not found: {filepath}"
                )
            file_obj = open(filepath, mode="r", newline="", encoding="utf-8")

        cities = []

        with file_obj as file:
            reader = csv.DictReader(file)

            for row in reader:
                city = City(
                    city_id=row["city_id"],
                    x=row["x"],
                    y=row["y"],
                )
                cities.append(city)

        if len(cities) < 2:
            raise ValueError(
                "CSV must contain at least 2 cities"
            )

        print(
            f"Loaded {len(cities)} cities from {filepath}"
        )

        return cities