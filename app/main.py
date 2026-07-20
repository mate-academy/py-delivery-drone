class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str,
                 weight: int,
                 coords: list | None = None) -> None:
        self.name = name
        self.weight = weight
        if coords is None:
            self.coords = [0, 0]
        else:
            self.coords = coords

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"

    def go_forward(self, number: int = 1) -> None:
        self.coords[1] = self.coords[1] + number

    def go_back(self, number: int = 1) -> None:
        self.coords[1] = self.coords[1] - number

    def go_right(self, number: int = 1) -> None:
        self.coords[0] = self.coords[0] + number

    def go_left(self, number: int = 1) -> None:
        self.coords[0] = self.coords[0] - number


class FlyingRobot(BaseRobot):
    def __init__(self, name: str,
                 weight: int,
                 coords: list | None = None) -> None:
        super().__init__(name, weight, coords)
        if coords is None:
            self.coords = [0, 0, 0]
        else:
            self.coords = coords

    def go_up(self, number: int = 1) -> None:
        self.coords[2] = self.coords[2] + number

    def go_down(self, number: int = 1) -> None:
        self.coords[2] = self.coords[2] - number


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str, weight: int,
                 max_load_weight: int,
                 coords: list | None = None,
                 current_load: Cargo | None = None) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, weight_cargo: Cargo) -> None:
        if (self.current_load is None
                and weight_cargo.weight <= self.max_load_weight):
            self.current_load = weight_cargo

    def unhook_load(self) -> None:
        self.current_load = None
