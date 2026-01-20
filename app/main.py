class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str,
                 weight: int,
                 coords: list = None
                 ) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords if coords is not None else [0, 0]

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step  # Y-axis (forward/backward)

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step  # Y-axis (forward/backward)

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step  # X-axis (right/left)

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step  # X-axis (right/left)

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        super().__init__(name, weight, coords[:2] if coords else [0, 0])

        if coords is not None and len(coords) == 3:
            self.coords = coords.copy()
        else:
            self.coords = [*self.coords, 0]  # Add Z=0 to make 3D

    def go_up(self, step: int = 1) -> None:
        if len(self.coords) < 3:
            self.coords.append(0)
        self.coords[2] += step  # Z-axis (go up)

    def go_down(self, step: int = 1) -> None:
        if len(self.coords) < 3:
            self.coords.append(0)
        self.coords[2] -= step  # Z-axis (go down)


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str,
                 weight: int,
                 max_load_weight: int,
                 coords: list = None,
                 current_load: Cargo = None
                 ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = None
        if current_load is not None:
            self.hook_load(current_load)

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
