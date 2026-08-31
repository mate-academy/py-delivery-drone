class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot(Cargo):
    def __init__(self, name: int, weight: int, coords: bool = None) -> None:
        super().__init__(weight)
        self.name = name
        self.coords = coords

        if coords is None:
            self.coords = [0, 0]
        else:
            self.coords = list(coords)

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: int, weight: int, coords: bool = None) -> None:
        super().__init__(name, weight, coords)

        if coords is None:
            self.coords = [0, 0, 0]
        else:
            super().__init__(name, weight, coords)

    def go_up(self, go: int = 1) -> None:
        self.coords[2] += go

    def go_down(self, go: int = 1) -> None:
        self.coords[2] -= go


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: int, weight: int, max_load_weight: int,
                 coords: list = [0, 0, 0],
                 current_load: bool = None) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: int) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
