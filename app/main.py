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
        self.coords = coords if coords is not None else [0, 0]

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list | None = None
    ) -> None:
        if coords is None:
            coords = [0, 0, 0]
        super().__init__(
            name=name,
            weight=weight,
            coords=coords
        )

    def go_up(self, z_cord: int = 1) -> None:
        self.coords[2] += z_cord

    def go_down(self, z_cord: int = 1) -> None:
        self.coords[2] -= z_cord


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            max_load_weight: int,
            coords: list | None = None,
            current_load: Cargo | None = None
    ) -> None:
        if coords is None:
            coords = [0, 0, 0]
        super().__init__(name=name, weight=weight, coords=coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, other: Cargo) -> None:
        if isinstance(other, Cargo):
            if other.weight <= self.max_load_weight:
                if self.current_load is None:
                    self.current_load = other

    def unhook_load(self) -> None:
        self.current_load = None
