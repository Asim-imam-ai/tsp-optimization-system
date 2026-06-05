import random
from typing import List

from app.models.city import City


class RouteGenerator:

    @staticmethod
    def generate_random_cities(
        num_cities: int,
        min_coord: int = 0,
        max_coord: int = 100,
    ) -> List[City]:

        cities = []

        for city_id in range(num_cities):

            city = City(
                city_id=city_id,
                x=random.randint(
                    min_coord,
                    max_coord,
                ),
                y=random.randint(
                    min_coord,
                    max_coord,
                ),
            )

            cities.append(city)

        return cities