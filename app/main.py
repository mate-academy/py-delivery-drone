from __future__ import annotations
from typing import Optional


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight: int = weight


class BaseRobot:
    def __init__(
        self,
        name: str,
        weight: int,
        coords: Optional[list[int]] = None,
    ) -> None:
        self.name: str = name
        self.weight: int = weight
        self.coords: list[int] = coords.copy() if coords else [0, 0]

    def go_forward(self, steps: int = 1) -> None:
        self.coords[1] += steps

    def go_back(self, steps: int = 1) -> None:
        self.coords[1] -= steps

    def go_right(self, steps: int = 1) -> None:
        self.coords[0] += steps

    def go_left(self, steps: int = 1) -> None:
        self.coords[0] -= steps

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        coords: Optional[list[int]] = None,
    ) -> None:
        if coords is None:
            super().__init__(name, weight)
            self.coords.append(0)
        else:
            x_coord, y_coord = coords[0], coords[1]
            z_coord = coords[2] if len(coords) > 2 else 0
            super().__init__(name, weight, [x_coord, y_coord])
            self.coords = [x_coord, y_coord, z_coord]

    def go_up(self, steps: int = 1) -> None:
        self.coords[2] += steps

    def go_down(self, steps: int = 1) -> None:
        self.coords[2] -= steps


class DeliveryDrone(FlyingRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        coords: Optional[list[int]] = None,
        max_load_weight: int = 0,
        current_load: Optional[Cargo] = None,
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight: int = max_load_weight
        self.current_load: Optional[Cargo] = None

        if current_load:
            self.hook_load(current_load)

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
