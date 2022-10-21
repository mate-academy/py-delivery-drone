class Cargo:
    def __init__(self, weight):
        self.weight = weight
        

class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        self.name = name
        self.weight = weight
        if coords is None:
            self.coords = [0, 0]
        else:
            self.coords = coords

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        super().__init__(name, weight, coords)
        if coords is None:
            self.coords = [0, 0, 0]
        else:
            self.coords = coords

    def go_up(self, step) -> None:
        self.coords[2] += step

    def go_down(self, step):
        self.coords[2] -= step
