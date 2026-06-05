import matplotlib.pyplot as plt


class CityPlot:

    @staticmethod
    def plot(cities):

        plt.figure(figsize=(8, 6))

        for city in cities:

            plt.scatter(
                city.x,
                city.y,
            )

            plt.text(
                city.x,
                city.y,
                str(city.city_id),
            )

        plt.title("Cities")

        plt.xlabel("X")

        plt.ylabel("Y")

        plt.grid(True)

        plt.show()