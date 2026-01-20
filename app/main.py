class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int,
                 coords: list | None = None) -> None:
        self.name = name
        self.weight = weight
        self.coords = [0, 0] if coords is None else coords

    def go_forward(self, y_step: int = 1) -> None:
        self.coords[1] += y_step

    def go_back(self, y_step: int = 1) -> None:
        self.coords[1] -= y_step

    def go_right(self, x_step: int = 1) -> None:
        self.coords[0] += x_step

    def go_left(self, x_step: int = 1) -> None:
        self.coords[0] -= x_step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int,
                 coords: list | None = None) -> None:

        if coords is None:
            coords = [0, 0, 0]
        while len(coords) < 3:
            coords.append(0)

        super().__init__(name=name, weight=weight, coords=coords)

    def go_up(self, z_step: int = 1) -> None:
        self.coords[2] += z_step

    def go_down(self, z_step: int = 1) -> None:
        self.coords[2] -= z_step


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str, weight: int, max_load_weight: int,
                 coords: list | None = None,
                 current_load: Cargo | None = None) -> None:

        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = None
        if current_load is not None:
            self.hook_load(current_load)

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None:
            if cargo.weight <= self.max_load_weight:
                self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
