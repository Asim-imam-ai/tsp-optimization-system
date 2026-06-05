from dataclasses import dataclass
from typing import List


@dataclass
class Route:
    path: List[int]
    cost: float

    def to_dict(self):
        return {
            "path": self.path,
            "cost": self.cost,
        }

    def __str__(self):
        return (
            f"Route(path={self.path}, "
            f"cost={self.cost:.2f})"
        )