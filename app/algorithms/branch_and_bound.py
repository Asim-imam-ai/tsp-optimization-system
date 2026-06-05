# app/algorithms/branch_and_bound.py

class BranchAndBoundTSP:

    def __init__(self, distance_matrix):
        self.distance_matrix = distance_matrix
        self.num_cities = len(distance_matrix)

        self.best_cost = float("inf")
        self.best_route = []

    def solve(self, start_city=0):

        visited = [False] * self.num_cities
        visited[start_city] = True

        self._search(
            current_city=start_city,
            start_city=start_city,
            visited=visited,
            route=[start_city],
            current_cost=0,
        )

        return (
            self.best_route,
            self.best_cost,
        )

    def _search(
        self,
        current_city,
        start_city,
        visited,
        route,
        current_cost,
    ):

        if len(route) == self.num_cities:

            total_cost = (
                current_cost
                + self.distance_matrix[
                    current_city
                ][start_city]
            )

            if total_cost < self.best_cost:

                self.best_cost = total_cost

                self.best_route = (
                    route + [start_city]
                )

            return

        if current_cost >= self.best_cost:
            return

        for next_city in range(
            self.num_cities
        ):

            if not visited[next_city]:

                visited[next_city] = True

                route.append(next_city)

                self._search(
                    next_city,
                    start_city,
                    visited,
                    route,
                    current_cost
                    + self.distance_matrix[
                        current_city
                    ][next_city],
                )

                route.pop()

                visited[next_city] = False