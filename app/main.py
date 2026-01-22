class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: float, coords: list = None) -> None:
        if coords is None:
            coords = [0, 0]  # Default coordinates if None is passed
        self.name = name
        self.weight = weight
        self.coords = coords

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step  # Positive Y-axis means forward

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step  # Negative Y-axis means backward

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step  # Positive X-axis means right

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step  # Negative X-axis means left

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: float, coords: list = None) -> None:
        if coords is None:
            coords = [0, 0, 0]  # Default coordinates if None is passed
        super().__init__(name, weight, coords)

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step  # Positive Z-axis means up

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step  # Negative Z-axis means down


class DeliveryDrone(FlyingRobot):
    def __init__(
        self,
        name: str,
        weight: float,
        coords: list = None,
        max_load_weight: float = 10.0,
        current_load: Cargo | None = None
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
