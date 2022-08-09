class Cargo:
    def __init__(self, weight):
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight, coords=None):
        if coords is None:
            coords = [0, 0]
        self.name = name
        self.weight = weight
        self.coords = coords

    def go_forward(self, step: int = 1):
        self.coords[1] += step
        return self

    def go_back(self, step: int = 1):
        self.coords[1] -= step
        return self

    def go_right(self, step: int = 1):
        self.coords[0] += step
        return self

    def go_left(self, step: int = 1):
        self.coords[0] -= step
        return self

    def get_info(self):
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None):
        if coords is None:
            coords = [0, 0, 0]
        super().__init__(name, weight, coords)
        self.coords = coords

    def go_up(self, step: int = 1):
        self.coords[2] += step
        return self

    def go_down(self, step: int = 1):
        self.coords[2] -= step
        return self


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str, weight: int, max_load_weight, current_load):
        super().__init__(name, weight, coords=None)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cls):
        if cls.weight <= self.max_load_weight and self.current_load is None:
            self.current_load = cls
            return self

    def unhook_load(self):
        self.current_load = None
        return self
