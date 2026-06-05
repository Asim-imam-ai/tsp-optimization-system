from dataclasses import dataclass


@dataclass
class BenchmarkResult:
    algorithm_name: str
    execution_time: float
    memory_usage: float
    route_cost: float

    def to_dict(self):
        return {
            "algorithm_name": self.algorithm_name,
            "execution_time": self.execution_time,
            "memory_usage": self.memory_usage,
            "route_cost": self.route_cost,
        }