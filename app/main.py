from __future__ import annotations


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight

# write your code here


class BaseRobot:
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list[int] = None) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords if (
            coords is not None and len(coords) < 2) else [0, 0]

    def go_forward(self, step: int = 1) -> None:
        self.coords = [self.coords[0], self.coords[1] + step]

    def go_back(self, step: int = 1) -> None:
        self.coords = [self.coords[0], self.coords[1] - step]

    def go_right(self, step: int = 1) -> None:
        self.coords = [self.coords[0] + step, self.coords[1]]

    def go_left(self, step: int = 1) -> None:
        self.coords = [self.coords[0] - step, self.coords[1]]

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list[int] = None) -> None:
        super().__init__(name, weight, coords if (
            coords is not None and len(coords) < 3) else [0, 0, 0])

    def go_up(self, step: int = 1) -> None:
        self.coords[3] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[3] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            max_load_weight: int,
            current_load: Cargo,
            coords: list[int] = None) -> None:
        super().__init__(name, weight, coords if (
            coords is not None and len(coords) < 3) else [0, 0, 0])
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
