from __future__ import annotations
from typing import Iterable, Optional


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
        self,
        name: str,
        weight: int,
        coords: Optional[Iterable[int]] = None,
    ) -> None:
        self.name = name
        self.weight = weight
        # Fresh list per instance; keep whatever dimensionality is passed
        self.coords: list[int] = list(coords) if coords is not None else [0, 0]

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
        coords: Optional[Iterable[int]] = None,
    ) -> None:
        # Default [0,0,0]; ensure exactly 3 values; do not mutate caller list
        base3 = [0, 0, 0] if coords is None else list(coords)
        base3 = (base3 + [0, 0, 0])[:3]
        super().__init__(name, weight, base3)

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        # Allow negatives (tests expect [-1] after going down from 0)
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        max_load_weight: int,
        current_load: Optional[Cargo] = None,
        coords: Optional[Iterable[int]] = None,
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load: Optional[Cargo] = None
        if current_load is not None:
            self.hook_load(current_load)

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
