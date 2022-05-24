class Cargo:
    def __init__(self, weight):
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None):
        self.name = name
        self. weight = weight
        self.coords = coords
        if self.coords is None:
            self.coords = [0, 0]

    def go_forward(self, step: int = 1):
        self.coords[1] += step
        return self.coords

    def go_back(self, step: int = 1):
        self.coords[1] -= step
        return self.coords

    def go_right(self, step: int = 1):
        self.coords[0] += step
        return self.coords

    def go_left(self, step: int = 1):
        self.coords[0] -= step
        return self.coords

    def get_info(self):
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None):
        super(FlyingRobot, self).__init__(name, weight, coords)
        if coords is None:
            self.coords = [0, 0, 0]

    def go_up(self, step: int = 1):
        self.coords[2] += step
        return self.coords

    def go_down(self, step: int = 1):
        self.coords[2] -= step
        return self.coords


class DeliveryDrone(FlyingRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        max_weight_load: int,
        current_load: int = None,
        coords: list = None
    ):
        super(DeliveryDrone, self).__init__(name, weight, coords)
        self.max_weight_load = max_weight_load
        self.current_load = current_load

    def hook_load(self, cargo: Cargo):
        if not self.current_load and cargo.weight <= self.max_weight_load:
            self.current_load = cargo

    def unhook_load(self):
        self.current_load = None
