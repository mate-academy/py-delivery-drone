class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot(Cargo):
    def __init__(self, name: str, weight: int, coords: list[int, int] = None) -> None:
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
