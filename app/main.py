class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        self.name = name
        self.weight = weight
        if coords is None:
            self.coords = [0, 0]
        else:
            self.coords = coords

    def go_forward(self, steep: int = 1) -> None:
        self.coords[1] += steep

    def go_back(self, steep: int = 1) -> None:
        self.coords[1] -= steep

    def go_right(self, steep: int = 1) -> None:
        self.coords[0] += steep

    def go_left(self, steep: int = 1) -> None:
        self.coords[0] -= steep

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        super().__init__(name, weight)
        if coords is None:
            self.coords = [0, 0, 0]
# I don't know how to do it differently
# If there is any other way to solve this
# I will gladly hear about it from you :)
        else:
            self.coords = coords

    def go_up(self, steep: int = 1) -> None:
        self.coords[2] += steep

    def go_down(self, steep: int = 1) -> None:
        self.coords[2] -= steep


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str,
                 weight: int,
                 max_load_weight: int,
                 current_load: int,
                 coords: list = None,
                 ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and self.max_load_weight >= cargo.weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
