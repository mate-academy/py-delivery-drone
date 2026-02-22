class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list | None = None,
    ) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords or [0, 0]

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
            coords: list | None = None,
    ) -> None:
        coords = coords or [0, 0, 0]
        if len(coords) == 2:
            coords.append(0)
        super().__init__(name, weight, coords[:2])
        self.coords = coords

    def go_up(self, z_coord: int = 1) -> None:
        self.coords[2] += z_coord

    def go_down(self, z_coord: int = 1) -> None:
        self.coords[2] -= z_coord


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            max_load_weight: int,
            coords: list | None = None,
            current_load: Cargo | None = None
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = None
        if isinstance(current_load, Cargo):
            self.hook_load(current_load)

    def hook_load(self, load: Cargo) -> None:
        if self.current_load is None and load.weight <= self.max_load_weight:
            self.current_load = load

    def unhook_load(self) -> None:
        self.current_load = None
