class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
        self, name: str, weight: int, coords: list[int] = [0, 0]
    ) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords
    # def go_forward(self) -> None:
