class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        self.name = name
        self. weight = weight
        self.coords = coords or [0, 0]

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        super().__init__(name, weight, coords=coords or [0, 0, 0])

    def go_up(self, *args) -> None:
        if args:
            self.coords[2] += sum(args)
        else:
            self.coords[2] += 1

    def go_down(self, *args) -> None:
        if args:
            self.coords[2] -= sum(args)
        else:
            self.coords[2] -= 1


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            max_load_weight: int,
            current_load: object,
            coords: list = None
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: object) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        if self.current_load:
            self.current_load = None
