from dataclasses import dataclass


@dataclass
class ComparisonResult:
    algorithm: str
    cost: float
    execution_time: float
    memory_usage: float