class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        self.name = name
        self.weight = weight
        if coords is None:
            self.coords = [0, 0]
        else:
            self.coords = coords

    def go_forward(self, distance: int = 1) -> None:
        self.coords[1] += distance

    def go_back(self, distance: int = 1) -> None:
        self.coords[1] -= distance

    def go_right(self, distance: int = 1) -> None:
        self.coords[0] += distance

    def go_left(self, distance: int = 1) -> None:
        self.coords[0] -= distance

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        super().__init__(name, weight, coords)
        if coords is None:
            self.coords = [0, 0, 0]
        else:
            self.coords = coords

    def go_up(self, distance: int = 1) -> None:
        self.coords[2] += distance

    def go_down(self, distance: int = 1) -> None:
        self.coords[2] -= distance


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            max_load_weight: int,
            current_load: Cargo | None,
            **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None:
            if cargo.weight <= self.max_load_weight:
                self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
