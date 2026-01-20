class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list | None = None) -> None:
        self.name = name
        self.weight = weight
        if coords is None:
            coords = [0, 0]
        self.coords = coords

    def go_forward(self, steps: int = 1) -> None:
        self.coords[1] += steps

    def go_back(self, steps: int = 1) -> None:
        self.coords[1] -= steps

    def go_right(self, steps: int = 1) -> None:
        self.coords[0] += steps

    def go_left(self, steps: int = 1) -> None:
        self.coords[0] -= steps

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list | None = None) -> None:
        if coords is None:
            coords = [0, 0, 0]
        super().__init__(name, weight, coords)

    def go_up(self, steps: int = 1) -> None:
        self.coords[2] += steps

    def go_down(self, steps: int = 1) -> None:
        self.coords[2] -= steps


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str, weight: int, coords: list | None = None,
                 max_load_weight: int = 10,
                 current_load: Cargo | None = None) -> None:

        if coords is None:
            coords = [0, 0, 0]

        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight

        self.current_load = None
        if isinstance(current_load, Cargo):
            self.hook_load(current_load)

    def hook_load(self, load: Cargo) -> None:
        if load.weight <= self.max_load_weight and self.current_load is None:
            self.current_load = load

    def unhook_load(self) -> None:
        self.current_load = None
