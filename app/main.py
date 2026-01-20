from __future__ import annotations

from typing import Any, List, Optional


class Cargo:
    def __init__(self, weight: float) -> None:
        self.weight = weight


class BaseRobot:
    """Robô que se move nos eixos X (direita/esquerda) e Y (frente/trás)."""

    def __init__(
        self,
        name: str,
        weight: float,
        coords: Optional[List[int]] = None,
    ) -> None:
        self.name = name
        self.weight = weight
        self.coords: List[int] = [0, 0] if coords is None else list(coords)

    def go_forward(self, step: int = 1) -> None:
        # +Y é frente
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
        weight: float,
        coords: Optional[List[int]] = None,
    ) -> None:
        if coords is None:
            coords3 = [0, 0, 0]
        else:
            coords_in = list(coords)
            if len(coords_in) == 2:
                coords3 = [coords_in[0], coords_in[1], 0]
            else:
                coords3 = coords_in[:3]

        super().__init__(name=name, weight=weight, coords=coords3[:2])
        self.coords = coords3

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(
        self,
        name: str,
        weight: float,
        coords: Optional[List[int]] = None,
        max_load_weight: float = 0,
        current_load: Optional[Any] = None,
    ) -> None:
        super().__init__(name=name, weight=weight, coords=coords)
        self.max_load_weight = max_load_weight
        self.current_load: Optional[Any] = None

        if current_load is not None:
            self.hook_load(current_load)

    def hook_load(self, cargo: Any) -> None:
        has_weight_attr = getattr(cargo, "weight", None) is not None
        if self.current_load is None and has_weight_attr:
            if cargo.weight <= self.max_load_weight:
                self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
