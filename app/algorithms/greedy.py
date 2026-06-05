# app/algorithms/greedy.py

class GreedyTSP:
    """
    Nearest Neighbor TSP
    """

    def __init__(self, distance_matrix):
        self.distance_matrix = distance_matrix
        self.num_cities = len(distance_matrix)

    def solve(self, start_city=0):
        visited = [False] * self.num_cities

        route = [start_city]
        visited[start_city] = True

        current_city = start_city
        total_cost = 0

        for _ in range(self.num_cities - 1):

            nearest_city = None
            nearest_distance = float("inf")

            for city in range(self.num_cities):

                if (
                    not visited[city]
                    and self.distance_matrix[current_city][city]
                    < nearest_distance
                ):
                    nearest_distance = self.distance_matrix[current_city][city]
                    nearest_city = city

            if nearest_city is None:
                raise ValueError("No unvisited city found")

            route.append(nearest_city)
            visited[nearest_city] = True

            total_cost += nearest_distance
            current_city = nearest_city

        total_cost += self.distance_matrix[current_city][start_city]

        route.append(start_city)

        return route, total_cost