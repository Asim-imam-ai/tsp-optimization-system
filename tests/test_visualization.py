from app.services import (
    RouteGenerator,
)

from app.visualization import (
    CityPlot,
)


def test_city_plot():

    cities = (
        RouteGenerator.generate_random_cities(
            5
        )
    )

    assert len(cities) == 5