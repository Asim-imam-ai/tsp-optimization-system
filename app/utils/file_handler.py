# app/utils/file_handler.py

import csv
from pathlib import Path

from app.models.city import City


class FileHandler:

    @staticmethod
    def save_cities_to_csv(
        cities,
        filepath,
    ):

        filepath = Path(filepath)

        with open(
            filepath,
            mode="w",
            newline="",
        ) as file:

            writer = csv.writer(file)

            writer.writerow(
                [
                    "city_id",
                    "x",
                    "y",
                ]
            )

            for city in cities:
                writer.writerow(
                    [
                        city.city_id,
                        city.x,
                        city.y,
                    ]
                )

    @staticmethod
    def load_cities_from_csv(
        filepath,
    ):

        filepath = Path(filepath)

        cities = []

        with open(
            filepath,
            mode="r",
        ) as file:

            reader = csv.DictReader(
                file
            )

            for row in reader:

                cities.append(
                    City(
                        city_id=int(
                            row["city_id"]
                        ),
                        x=float(
                            row["x"]
                        ),
                        y=float(
                            row["y"]
                        ),
                    )
                )

        return cities