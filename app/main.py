class Cargo:
    def __init__(self, weight):
        self.weight = weight


class BaseRobot:

    def __init__(self, name, weight, coords: list = None):
        self.name = name
        self.weight = weight
        self.coords = [0, 0] if coords is None else coords

    def go_forward(self, step: int = 1):
        self.coords[1] += step

    def go_back(self, step: int = 1):
        self.coords[1] -= step

    def go_right(self, step: int = 1):
        self.coords[0] += step

    def go_left(self, step: int = 1):
        self.coords[0] -= step


class FlyingRobot(BaseRobot):

    def __init__(self, name, weight, coords: list = None):
        super().__init__(name, weight, coords)
        self.coords = [0, 0, 0] if coords is None else coords

    def go_up(self, step: int = 1):
        self.coords[2] += step

    def go_down(self, step: int = 1):
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):

    def __init__(self,
                 name: str,
                 weight: int = 0,
                 max_load_weight: int = 0,
                 current_load: Cargo = None,
                 coord: list = None):
        super().__init__(name, weight, coord)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo):
        if self.current_load is None and self.max_load_weight >= cargo.weight:
            self.current_load = cargo

    def unhook_load(self):
        self.current_load = None
