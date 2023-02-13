class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list = None
    ) -> None:
        self.name = name
        self.weight = weight
        self.coords = [0, 0] if coords is None else coords

    def go_forward(self, y_coordinate: int = 1) -> list:
        self.coords[1] += y_coordinate
        return self.coords

    def go_back(self, y_coordinate: int = 1) -> list:
        self.coords[1] -= y_coordinate
        return self.coords

    def go_right(self, x_coordinate: int = 1) -> list:
        self.coords[0] += x_coordinate
        return self.coords

    def go_left(self, x_coordinate: int = 1) -> list:
        self.coords[0] -= x_coordinate
        return self.coords

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list = None
    ) -> None:
        super().__init__(name, weight)
        self.coords = [0, 0, 0] if coords is None else coords

    def go_up(self, z_coordinate: int = 1) -> list:
        self.coords[2] += z_coordinate
        return self.coords

    def go_down(self, z_coordinate: int = 1) -> list:
        self.coords[2] -= z_coordinate
        return self.coords


class DeliveryDrone(FlyingRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        max_load_weight: int,
        current_load: int | None,
        coords: list = None
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
