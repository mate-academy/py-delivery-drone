class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int,
                 coords: list | None = None) -> None:
        self.coords = list(coords or [0, 0])
        self.name = name
        self.weight = weight

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
    def __init__(self, name: str, weight: int,
                 coords: list | None = None) -> None:
        xxx = yyy = zzz = 0
        if coords is not None:
            if len(coords) == 2:
                xxx = coords[0]
                yyy = coords[1]
                zzz = 0
            elif len(coords) == 3:
                xxx, yyy, zzz = coords
        super().__init__(name, weight, coords=[xxx, yyy])
        self.coords.append(zzz)

    def go_up(self, steps: int = 1) -> None:
        self.coords[2] += steps

    def go_down(self, steps: int = 1) -> None:
        self.coords[2] -= steps


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str, weight: int,
                 max_load_weight: int, current_load: Cargo | None = None,
                 coords: list | None = None) -> None:
        super().__init__(name, weight, coords=coords)
        self.max_load_weight = max_load_weight
        self.current_load = None
        if current_load is not None:
            self.hook_load(current_load)

    def hook_load(self, cargo: Cargo) -> None:
        if (self.current_load is None and cargo.weight
                <= self.max_load_weight):
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
