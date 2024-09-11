from __future__ import annotations


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        self.name = name
        self.weight = weight
        if coords and len(coords) >= 2:
            self.coords = coords
        else:
            self.coords = [0, 0]    # [x, y]

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step  # [x, y + step]

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step  # [x, y - step]

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step  # [x + step, y]

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step  # [x - step, y]

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        if not (coords and len(coords) == 3):
            coords = [0, 0, 0]    # [x, y, z]
        super().__init__(name, weight, coords)

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step  # [x, y, z + step]

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step  # [x, y, z - step]


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str, weight: int, max_load_weight: int,
                 coords: list = None, current_load: Cargo = None) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        if current_load and isinstance(current_load, Cargo):
            self.current_load = current_load
        else:
            self.current_load = None

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and isinstance(cargo, Cargo) \
                and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
