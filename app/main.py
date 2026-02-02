from __future__ import annotations

from typing import List, Optional


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
        self,
        name: str,
        weight: int,
        coords: Optional[List[int]] = None,
    ) -> None:
        self.name = name
        self.weight = weight

        if coords is None:
            self.coords = [0, 0]
        else:
            self.coords = coords

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
    def __init__(
        self,
        name: str,
        weight: int,
        coords: Optional[List[int]] = None,
    ) -> None:
        if coords is None:
            x_coord = 0
            y_coord = 0
            z_coord = 0
        elif len(coords) == 3:
            x_coord = coords[0]
            y_coord = coords[1]
            z_coord = coords[2]
        else:
            x_coord = coords[0]
            y_coord = coords[1]
            z_coord = 0

        super().__init__(
            name=name,
            weight=weight,
            coords=[x_coord, y_coord],
        )
        self.coords = [x_coord, y_coord, z_coord]

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        max_load_weight: int,
        coords: Optional[List[int]] = None,
        current_load: Optional[Cargo] = None,
    ) -> None:
        super().__init__(
            name=name,
            weight=weight,
            coords=coords,
        )

        self.max_load_weight = max_load_weight
        self.current_load: Optional[Cargo] = None

        if current_load is not None:
            self.hook_load(current_load)

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is not None:
            return

        if cargo.weight > self.max_load_weight:
            return

        self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
