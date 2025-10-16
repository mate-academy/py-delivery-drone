class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self,
                 name: str,
                 weight: int,
                 coords: list[int] = None
                 ) -> None:
        self.name = name
        self.weight = weight

        coords = coords or []
        x_coord = coords[0] if len(coords) > 0 else 0
        y_coord = coords[1] if len(coords) > 1 else 0
        self.coords = [x_coord, y_coord]

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
    def __init__(self,
                 name: str,
                 weight: int,
                 coords: list[int] = None
                 ) -> None:

        coords = coords or []
        x_coord = coords[0] if len(coords) > 0 else 0
        y_coord = coords[1] if len(coords) > 1 else 0
        z_coord = coords[2] if len(coords) > 2 else 0
        norm_coords = [x_coord, y_coord, z_coord]

        super().__init__(name=name, weight=weight, coords=[x_coord, y_coord])
        self.coords = norm_coords

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(self,
                 name: str,
                 weight: int,
                 max_load_weight: int,
                 coords: list[int] = None,
                 current_load: Cargo | None = None
                 ) -> None:

        super().__init__(name=name, weight=weight, coords=coords)
        self.max_load_weight = max_load_weight
        self.current_load = None
        if isinstance(current_load, Cargo):
            self.hook_load(current_load)

    def hook_load(self, cargo: "Cargo") -> None:
        if cargo.weight <= self.max_load_weight and self.current_load is None:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
