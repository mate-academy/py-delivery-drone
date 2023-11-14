class Cargo:
    def __init__(
            self,
            weight: int
    ) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
            self,
            name: str,
            weight: int,
            coords=None
    ) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords if (
                coords is not None) else [0, 0]

    def go_forward(self, step=1):
        self.coords[1] += step

    def go_back(self, step=1):
        self.coords[1] -= step

    def go_right(self, step=1):
        self.coords[0] += step

    def go_left(self, step=1):
        self.coords[0] -= step

    def get_info(self):
        return (f"Robot: {self.name}, "
                f"Weight: {self.weight}")


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords=None,
            coordsThird=None
    ) -> None:
        if coords is None:
            coords = [0, 0, 0]
        if coordsThird is None:
            coordsThird = [0, 0, 0]
        super().__init__(name, weight, coords)
        self.coordsThird = coordsThird

    def go_up(self, step=1):
        self.coordsThird[2] += step
        self.coords = (self.coords[:2]
                       + [self.coordsThird[2]])

    def go_down(self, step=1):
        self.coordsThird[2] -= step
        self.coords = (self.coords[:2]
                       + [self.coordsThird[2]])


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords=None,
            coordsThird=None,
            max_load_weight: int = 0,
            current_load=None
    ) -> None:
        if coords is None:
            coords = [0, 0, 0]
        if coordsThird is None:
            coordsThird = [0, 0, 0]
        super().__init__(name, weight, coords, coordsThird)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo):
        if (self.current_load is None
                and cargo.weight <= self.max_load_weight):
            self.current_load = cargo

    def unhook_load(self):
        self.current_load = None
