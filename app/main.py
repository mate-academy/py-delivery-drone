class Cargo:
    def __init__(self, weight):
        self.weight = weight


class BaseRobot(Cargo):
    def __init__(self, name: str, weight: int, coords: list = None):
        super().__init__(weight=weight)
        self.name = name
        self.coords = coords if coords else [0, 0]

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step

    def get_info(self):
        return f'Robot: {self.name}, Weight: {self.weight}'


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None):
        super().__init__(name=name, weight=weight, coords=coords)
        self.coords = coords if coords else [0, 0, 0]

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(self,
                 name: str,
                 weight: int,
                 max_load_weight: int,
                 current_load: Cargo = None,
                 coords: list = None):
        super().__init__(name=name, weight=weight, coords=coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, load: Cargo) -> None:
        if not self.current_load and load.weight <= self.max_load_weight:
            self.current_load = load

    def unhook_load(self) -> None:
        self.current_load = None
