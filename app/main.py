class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot(Cargo):
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        super().__init__(weight)
        self.name = name
        if not coords:
            self.coords = [0, 0]

    def go_forward(self, parameter: int = 1):
        self.coords[1] += parameter

    def go_back(self, parameter: int = 1):
        self.coords[1] -= parameter

    def go_right(self, parameter: int = 1):
        self.coords[0] += parameter

    def go_left(self, parameter: int = 1):
        self.coords[0] -= parameter

    def get_info(self):
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        if not coords:
            coords = [0, 0, 0]
        super().__init__(name, weight, coords)

    def go_up(self, parameter: int = 1):
        self.coords += parameter

    def go_down(self, parameter: int = 1):
        self.coords -= parameter



