class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


stepkinds = {
    "forward": (0, 1),
    "back": (0, -1),
    "right": (1, 0),
    "left": (-1, 0),
    "up": (0, 0, 1),
    "down": (0, 0, -1)
}


class BaseRobot:
    def __init__(
            self, name: str,
            weight: int,
            coords: list | None = None
    ) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords if coords is not None else [0, 0]

    def go_forward(self, step: int = 1) -> None:
        self.coords[0] += stepkinds["forward"][0] * step
        self.coords[1] += stepkinds["forward"][1] * step

    def go_back(self, step: int = 1) -> None:
        self.coords[0] += stepkinds["back"][0] * step
        self.coords[1] += stepkinds["back"][1] * step

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += stepkinds["right"][0] * step
        self.coords[1] += stepkinds["right"][1] * step

    def go_left(self, step: int = 1) -> None:
        self.coords[0] += stepkinds["left"][0] * step
        self.coords[1] += stepkinds["left"][1] * step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
            self, name: str,
            weight: int,
            coords: list | None = None
    ) -> None:
        if coords is None:
            coords = [0, 0, 0]
        super().__init__(name, weight, coords)

    def go_up(self, step: int = 1) -> None:
        self.coords[0] += stepkinds["up"][0] * step
        self.coords[1] += stepkinds["up"][1] * step
        self.coords[2] += stepkinds["up"][2] * step

    def go_down(self, step: int = 1) -> None:
        self.coords[0] += stepkinds["down"][0] * step
        self.coords[1] += stepkinds["down"][1] * step
        self.coords[2] += stepkinds["down"][2] * step


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
        if current_load:
            self.hook_load(current_load)

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
