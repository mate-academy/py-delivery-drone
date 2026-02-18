class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight

class BaseRobot:
    def __init__(
            self,
            name: int,
            weight: int,
            coords: list[int] | None) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords or [0, 0]
        if len(coords) != 2:
            raise ValueError("Two coordinates must be provided")
        self.ax, self.ay = self.coords

    def go_forward(self, step: int | None) -> None:
        step = step or 1
        self.ay += step

    def go_back(self, step: int | None) -> None:
        step = step or 1
        self.ay -= step

    def go_right(self, step: int | None) -> None:
        step = step or 1
        self.ax += step

    def go_left(self, step: int | None) -> None:
        step = step or 1
        self.ax -= step

