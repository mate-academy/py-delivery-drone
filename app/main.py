class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None) -> None:

        self.name = name
        self.weight = weight
        self.coords = coords

        if self.coords is None:
            self.coords = [0, 0]

    def go_forward(self, number: int = 1) -> None:
        self.coords[1] += number

    def go_back(self, number: int = 1) -> None:
        self.coords[1] -= number

    def go_right(self, number: int = 1) -> None:
        self.coords[0] += number

    def go_left(self, number: int = 1) -> None:
        self.coords[0] -= number

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list = None
    ) -> None:

        super().__init__(name, weight, [0, 0, 0] if coords is None else coords)

    def go_up(self, number: int = 1) -> None:
        self.coords[2] += number

    def go_down(self, number: int = 1) -> None:
        self.coords[2] -= number


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list = None,
            max_load_weight: int = 0,
            current_load: int = None
    ) -> None:

        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo = Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
