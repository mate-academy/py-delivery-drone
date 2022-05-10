class Cargo:
    def __init__(self, weight: int):
        self.weight = weight


class BaseRobot:
    def __init__(self,
                 name: str,
                 weight: int,
                 coords: list = None):
        self.name = name
        self.weight = weight
        self.coords = [0, 0] if coords is None else coords

    def go_forward(self, step=1):
        self.coords[1] += step

    def go_back(self, step=1):
        self.coords[1] -= step

    def go_right(self, step=1):
        self.coords[0] += step

    def go_left(self, step=1):
        self.coords[0] -= step

    def get_info(self):
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self,
                 name: str,
                 weight: int,
                 coords: list = None):
        super().__init__(name, weight, coords)
        if coords is None:
            self.coords = [0, 0, 0]

    def go_up(self, step=1):
        self.coords[2] += step

    def go_down(self, step=1):
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(self,
                 name: str,
                 weight: int,
                 max_load_weight: int,
                 current_load: int,
                 coords: list = None):
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo_product: Cargo):
        if self.current_load is None and \
                cargo_product.weight <= self.max_load_weight:
            self.current_load = cargo_product

    def unhook_load(self):
        self.current_load = None
