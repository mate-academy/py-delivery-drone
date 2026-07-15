class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, cords: list[int] = [0, 0]) -> None:
        self.name = name
        self.weight = weight
        self.cords = cords

    def go_forward(self, step: int = 1) -> None:
        self.cords[1] += step

    def go_back(self, step: int = 1) -> None:
        self.cords[1] -= step

    def go_right(self, step: int = 1) -> None:
        self.cords[0] += step

    def go_left(self, step: int = 1) -> None:
        self.cords[0] -= step


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, cords: list[int] = [0, 0, 0]) -> None:
        super().__init__(name, weight, cords)

    def go_up(self, step: int = 1) -> None:
        self.cords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.cords[2] -= step
