class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords

    def go_forward(self, step=1) -> None:
        self.coords[1] += step

    def go_back(self, step=1) -> None:
        self.coords[1] -= step

    def go_right(self, step=1) -> None:
        self.coords[0] += step

    def go_left(self, step=1) -> None:
        self.coords[0] -= step

    def get_info(self):
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list) -> None:
        coords.insert(2, 0)
        super().__init__(name, weight, coords)
        
    def go_up(self, z: int) -> None:
        self.coords[2] += z

    def go_down(self, z: int) -> None:
        self.coords[2] -= z


class DeliveryDrone(FlyingRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        coords: list,
        max_load_weight: int,
        current_load=None
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: object):
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self):
        self.current_load = None
