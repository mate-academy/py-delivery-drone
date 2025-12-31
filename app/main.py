class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list[int, int] = [0, 0]
    ) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords

    def go_forward(self, step: int = 1) -> None:
        x_coord, y_coord, *z_coord = self.coords
        self.coords = [x_coord, y_coord + step, *z_coord]

    def go_back(self, step: int = 1) -> None:
        x_coord, y_coord, *z_coord = self.coords
        self.coords = [x_coord, y_coord - step, *z_coord]

    def go_right(self, step: int = 1) -> None:
        x_coord, y_coord, *z_coord = self.coords
        self.coords = [x_coord + step, y_coord, *z_coord]

    def go_left(self, step: int = 1) -> None:
        x_coord, y_coord, *z_coord = self.coords
        self.coords = [x_coord - step, y_coord, *z_coord]

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
        self, name: str, weight: int, coords: list[int, int, int] = [0, 0, 0]
    ) -> None:
        super().__init__(name, weight, coords)

    def go_up(self, step: int = 1) -> None:
        x_coord, y_coord, z_coord = self.coords
        self.coords = [x_coord, y_coord, z_coord + step]

    def go_down(self, step: int = 1) -> None:
        x_coord, y_coord, z_coord = self.coords
        self.coords = [x_coord, y_coord, z_coord - step]


class DeliveryDrone(FlyingRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        max_load_weight: int,
        current_load: Cargo | None = None,
        coords: list[int, int, int] = [0, 0, 0],
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, current_load: Cargo) -> None:
        if all([self.current_load is None,
               current_load.weight <= self.max_load_weight]):
            self.current_load = current_load

    def unhook_load(self) -> Cargo | None:
        self.current_load = None
