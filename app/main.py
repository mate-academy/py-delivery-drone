class Cargo:
    def __init__(self, weight):
        self.weight = weight


class BaseRobot:
    def __init__(self, name, weight, coords=None):
        self.name = name
        self.weight = weight
        self.coords = coords
        if coords is None:
            self.coords = [0, 0]

    def go_forward(self, step=1):
        self.coords[1] = self.coords[1] + step

    def go_back(self, step=1):
        self.coords[1] = self.coords[1] - step

    def go_right(self, step=1):
        self.coords[0] = self.coords[0] + step

    def go_left(self, step=1):
        self.coords[0] = self.coords[0] - step

    def get_info(self):
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name, weight, coords=None):
        super().__init__(name, weight, coords)
        if coords is None:
            self.coords = [0, 0, 0]

    def go_up(self, step=1):
        self.coords[-1] = self.coords[-1] + step

    def go_down(self, step=1):
        self.coords[-1] = self.coords[-1] - step


class DeliveryDrone(FlyingRobot):
    def __init__(self, max_load_weight, current_load,
                 name, weight, coords=None):
        self.max_load_weight = max_load_weight
        self.current_load = current_load
        super().__init__(name, weight, coords)

    def hook_load(self, Cargo):
        if self.current_load is None and Cargo.weight <= self.max_load_weight:
            self.current_load = Cargo

    def unhook_load(self):
        self.current_load = None
