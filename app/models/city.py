from dataclasses import dataclass


@dataclass
class City:
    city_id: int
    x: float
    y: float

    def to_dict(self) -> dict:
        return {
            "city_id": self.city_id,
            "x": self.x,
            "y": self.y,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            city_id=data["city_id"],
            x=data["x"],
            y=data["y"],
        )

    def __str__(self):
        return (
            f"City(id={self.city_id}, "
            f"x={self.x}, y={self.y})"
        )