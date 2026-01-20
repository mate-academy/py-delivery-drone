class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot(Cargo):
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        super().__init__(weight)
        self.name = name
        if isinstance(self, FlyingRobot):
            self.coords = coords if coords is not None else [0, 0, 0]
        else:
            self.coords = coords if coords is not None else [0, 0]

    def go_forward(self, step: float = 1) -> None:
        self.coords[1] += step

    def go_back(self, step: float = 1) -> None:
        self.coords[1] -= step

    def go_right(self, step: float = 1) -> None:
        self.coords[0] += step

    def go_left(self, step: float = 1) -> None:
        self.coords[0] -= step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):

    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        super().__init__(name, weight, coords)

    def go_up(self, step: float = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: float = 1) -> None:
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):

    def __init__(
            self,
            name: str,
            weight: int,
            max_load_weight: float,
            coords: list = None,
            current_load: Cargo | None = None
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = None
        if current_load is not None:
            self.hook_load(current_load)

    def hook_load(self, load: Cargo) -> None:
        if self.current_load is None:
            if load.weight <= self.max_load_weight:
                self.current_load = load

    def unhook_load(self) -> None:
        self.current_load = None
