class Cargo:
    def __init__(self, weight: int):
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None):
        self.name = name
        self.weight = weight
        self.coords = [0, 0] if coords is None else coords

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


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None):
        super(FlyingRobot, self).__init__(name, weight)
        self.coords = [0, 0, 0] if coords is None else coords

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
            max_load_weight: int,
            current_load: int,
            coords: list = None
    ):
        self.max_load_weight = max_load_weight
        self.current_load = current_load
        super(DeliveryDrone, self).__init__(name, weight, coords)

    def hook_load(self, cargo: Cargo):
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo
        return self.current_load

    def unhook_load(self):
        self.current_load = None
        return self.current_load
