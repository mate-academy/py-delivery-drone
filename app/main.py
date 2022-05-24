class Cargo:
    def __init__(self, weight):
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None):
        self.name = name
        self.weight = weight
        self.coords = coords
        if coords is None:
            self.coords = [0, 0]

    def go_forward(self, step: int = 1):
        self.coords[1] += step

    def go_back(self, step: int = 1):
        self.coords[1] -= step

    def go_right(self, step: int = 1):
        self.coords[0] += step

    def go_left(self, step: int = 1):
        self.coords[0] -= step

    def get_info(self):
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None):
        super().__init__(name, weight, coords)
        if coords is None:
            self.coords = [0, 0, 0]

    def go_up(self, step: int = 1):
        self.coords[2] += step

    def go_down(self, step: int = 1):
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(self,
                 name: str,
                 weight: int,
                 max_weight_load: int,
                 current_load: Cargo,
                 coords: list = None):
        super().__init__(name, weight, coords)
        self.max_weight_load = max_weight_load
        self.current_load = current_load

    def hook_load(self, other: Cargo):
        if self.current_load is None and other.weight <= self.max_weight_load:
            self.current_load = other

    def unhook_load(self):
        if self.current_load is not None:
            self.current_load = None
