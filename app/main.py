class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
            self,
            name: str,
            weight: int = 1,
            coords: list[int] | None = None
    ) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords or [0, 0]

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
    def __init__(
            self,
            name: str,
            weight: int = 1,
            coords: list[int] | None = None
    ) -> None:
        if coords is None:
            super().__init__(name=name, weight=weight, coords=[0, 0, 0])
        else:
            super().__init__(name=name, weight=weight, coords=coords)

    def go_up(self, steps: int = 1) -> None:
        self.coords[2] += steps

    def go_down(self, steps: int = 1) -> None:
        self.coords[2] -= steps


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int = 1,
            coords: list[int] | None = None,
            max_load_weight: int = 0,
            current_load: Cargo | None = None
    ) -> None:
        super().__init__(name=name, weight=weight, coords=coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if not self.current_load and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
