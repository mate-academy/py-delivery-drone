class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list[int] | None = None
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
            coords: list[int] | None = None
    ) -> None:
        # Normalize coords to always be 3D before passing to BaseRobot
        if coords is None:
            parent_coords = [0, 0, 0]
        elif len(coords) == 2:
            parent_coords = coords + [0]
        else:
            parent_coords = coords
        super().__init__(name, weight, parent_coords)

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        max_load_weight: int,
        cargo: Cargo | None = None,
        coords: list[int] | None = None,
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = None
        if cargo is not None:
            self.hook_load(cargo)

    def hook_load(self, cargo: Cargo) -> None:
        if (self.current_load is None
                and cargo.weight <= self.max_load_weight):
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
