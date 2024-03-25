class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None):
        self.name = name
        self.weight = weight
        if coords is None:
            self.coords = [0, 0]
        else:
            self.coords = coords[:2]

    def go_forward(self, step: int = 1) -> None:
        x, y = self.coords
        y += step
        self.coords = [x, y]

    def go_back(self, step: int = 1) -> None:
        x, y = self.coords
        y -= step
        self.coords = [x, y]

    def go_right(self, step: int = 1) -> None:
        x, y = self.coords
        x += step
        self.coords = [x, y]

    def go_left(self, step: int = 1) -> None:
        x, y = self.coords
        x -= step
        self.coords = [x, y]

    def get_info(self) -> str:
        return (f"Robot: {self.name}, "
                f"Weight: {self.weight}")


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None):
        super().__init__(name, weight)
        if coords is None:
            self.coords = [0, 0, 0]
        else:
            self.coords = coords

    def go_up(self, step: int = 1) -> None:
        x, y, z = self.coords
        z += step
        self.coords = [x, y, z]

    def go_down(self, step: int = 1) -> None:
        x, y, z = self.coords
        z -= step
        self.coords = [x, y, z]


class DeliveryDrone(FlyingRobot):
    def __init__(self,
                 name: str,
                 weight: int,
                 coords: list = None,
                 max_load_weight: int = 0,
                 current_load: Cargo = None):
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
