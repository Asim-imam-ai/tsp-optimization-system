import os
import matplotlib.pyplot as plt


class RoutePlot:

    @staticmethod
    def plot_route(
        cities,
        route,
        title="TSP Route",
        output_path=None,
        show=True,
    ):
        """Plot a TSP route and optionally save it to disk."""
        if not cities:
            raise ValueError("Cities list is empty.")

        if not route:
            raise ValueError("Route is empty.")

        plt.figure(figsize=(10, 7))

        for city in cities:
            plt.scatter(city.x, city.y, s=100)
            plt.text(city.x, city.y, str(city.city_id))

        for i in range(len(route) - 1):
            city1 = cities[route[i]]
            city2 = cities[route[i + 1]]
            plt.plot(
                [city1.x, city2.x],
                [city1.y, city2.y],
                linewidth=2,
            )

        plt.title(title)
        plt.xlabel("X Coordinate")
        plt.ylabel("Y Coordinate")
        plt.grid(True)

        if output_path:
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            plt.savefig(output_path, dpi=300, bbox_inches="tight")

        if show:
            plt.show()

        plt.close()


#         else:

#             plt.show()

#         plt.close()



import matplotlib.pyplot as plt


class RoutePlot:

    @staticmethod
    def plot_route(
        cities,
        route,
        title="TSP Route",
        output_path=None,
        show=True,
    ):
        """
        Plot TSP route and optionally save + show.

        Parameters
        ----------
        cities : list
            List of City objects

        route : list[int]
            Order of visiting cities

        title : str
            Plot title

        output_path : str | None
            If provided → saves image

        show : bool
            If True → show on desktop
        """

        if not cities:
            raise ValueError("Cities list is empty")

        if not route:
            raise ValueError("Route is empty")

        plt.figure(figsize=(10, 7))

        # -------------------------
        # Plot cities
        # -------------------------
        for city in cities:
            plt.scatter(city.x, city.y, s=100)
            plt.text(city.x, city.y, str(city.city_id))

        # -------------------------
        # Plot route
        # -------------------------
        for i in range(len(route) - 1):

            city1 = cities[int(route[i])]
            city2 = cities[int(route[i + 1])]

            plt.plot(
                [city1.x, city2.x],
                [city1.y, city2.y],
                linewidth=2,
            )

        # -------------------------
        # Styling
        # -------------------------
        plt.title(title)
        plt.xlabel("X Coordinate")
        plt.ylabel("Y Coordinate")
        plt.grid(True)

        # -------------------------
        # Save image
        # -------------------------
        if output_path:
            plt.savefig(
                output_path,
                dpi=300,
                bbox_inches="tight",
            )
            print(f"Saved image → {output_path}")

        # -------------------------
        # Show on desktop
        # -------------------------
        if show:
            plt.show()

        plt.close()

    @staticmethod
    def plot_cities(
        cities,
        title="Cities",
        output_path=None,
        show=True,
    ):
        """
        Plot only cities (no route)
        """

        if not cities:
            raise ValueError("Cities list is empty")

        plt.figure(figsize=(10, 7))

        for city in cities:
            plt.scatter(city.x, city.y, s=100)
            plt.text(city.x, city.y, str(city.city_id))

        plt.title(title)
        plt.xlabel("X Coordinate")
        plt.ylabel("Y Coordinate")
        plt.grid(True)

        # Save
        if output_path:
            plt.savefig(
                output_path,
                dpi=300,
                bbox_inches="tight",
            )
            print(f"Saved image → {output_path}")

        # Show
        if show:
            plt.show()

        plt.close()