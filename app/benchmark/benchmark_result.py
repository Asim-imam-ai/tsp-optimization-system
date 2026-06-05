class BenchmarkResult:
    def __init__(
        self,
        algorithm_name,
        path,
        cost,
        execution_time,
        memory_usage,
    ):
        self.algorithm_name = algorithm_name
        self.path = path
        self.cost = cost
        self.execution_time = execution_time
        self.memory_usage = memory_usage