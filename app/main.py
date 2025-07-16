class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        self.weight = weight
        self.name = name
        if coords is None:
            coords = [0, 0]
        self.coords = coords
        self.x, self.y = coords

    def go_forward(self, step: int = 1) -> None:
        self.y += step
        self.coords = [self.x, self.y]

    def go_back(self, step: int = 1) -> None:
        self.y -= step
        self.coords = [self.x, self.y]

    def go_right(self, step: int = 1) -> None:
        self.x += step
        self.coords = [self.x, self.y]

    def go_left(self, step: int = 1) -> None:
        self.x -= step
        self.coords = [self.x, self.y]

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list = [0, 0, 0]
    ) -> None:

        super().__init__(name, weight, coords)
        self.x, self.y, self.z = coords

    def go_up(self, step: int = 1) -> None:
        self.z += step

    def go_down(self, step: int = 1) -> None:
        self.z -= step


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list = [0, 0, 0]
    ) -> None:

        super().__init__(name, weight, coords)
