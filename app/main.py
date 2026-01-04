

class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list | None = None
    ) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords or [0, 0]

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"

    def go_forward(self, steps: int = 1) -> None:
        self.coords[1] += steps

    def go_back(self, steps: int = 1) -> None:
        self.coords[1] -= steps

    def go_left(self, steps: int = 1) -> None:
        self.coords[0] -= steps

    def go_right(self, steps: int = 1) -> None:
        self.coords[0] += steps


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list | None = None
    ) -> None:
        super().__init__(name, weight, coords or [0, 0, 0])

    def go_up(self, steps: int = 1) -> None:
        self.coords[2] += steps

    def go_down(self, steps: int = 1) -> None:
        self.coords[2] -= steps


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            max_load_weight: int,
            current_load: Cargo | None = None,
            coords: list | None = None
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = None
        if isinstance(current_load, Cargo):
            self.hook_load(current_load)

    def hook_load(self, obj: Cargo) -> None:
        if self.current_load is None and obj.weight <= self.max_load_weight:
            self.current_load = obj

    def unhook_load(self) -> None:
        self.current_load = None
