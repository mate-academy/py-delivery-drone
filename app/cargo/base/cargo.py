class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight

    def __str__(self) -> str:
        return f"Cargo: {self.weight}"
