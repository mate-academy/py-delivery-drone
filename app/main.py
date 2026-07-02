class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int,
                 coords: list | None = None) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords or [0, 0]

    y_axis = 1
    x_axis = 0
    z_axis = 2

    def go_forward(self, step: int = 1) -> None:
        self.coords[self.y_axis] += step

    def go_back(self, step: int = 1) -> None:
        self.coords[self.y_axis] -= step

    def go_left(self, step: int = 1) -> None:
        self.coords[self.x_axis] -= step

    def go_right(self, step: int = 1) -> None:
        self.coords[self.x_axis] += step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int,
                 coords: list | None = None) -> None:
        if coords is None:
            coords = [0, 0, 0]
        super().__init__(name, weight, coords)

    def go_up(self, step: int = 1) -> None:
        self.coords[self.z_axis] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[self.z_axis] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str, weight: int, max_load_weight: int,
                 current_load: Cargo | None = None, coords: list | None = None
                 ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = None
        if current_load:
            self.hook_load(current_load)

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
