class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str,
                 weight: int,
                 coords: list | None = None) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords or [0, 0]

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str,
                 weight: int,
                 coords: list | None = None) -> None:
        coords_to_pass = []
        coords_for_self = []
        if coords is None:
            coords_for_self = [0, 0, 0]
            coords_to_pass = [0, 0]
        elif len(coords) == 2:
            coords_for_self = [coords[0], coords[1], 0]
            coords_to_pass = [coords[0], coords[1]]
        elif len(coords) == 3:
            coords_for_self = list(coords)
            coords_to_pass = [coords[0], coords[1]]
        else:
            raise ValueError("coords must be None or list of length 2 or 3")
        super().__init__(name, weight, coords_to_pass)
        self.coords = coords_for_self

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str,
                 weight: int,
                 max_load_weight: int,
                 current_load: Cargo | None = None,
                 coords: list | None = None) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = None
        if current_load is not None:
            self.hook_load(current_load)

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None:
            if cargo.weight <= self.max_load_weight:
                self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
