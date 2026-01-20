from __future__ import annotations
from typing import Any, Union


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str,
                 weight: int,
                 coords: list | None = None) -> None:
        if coords is None:
            coords = [0, 0]
        self.coords = coords
        self.weight = weight
        self.name = name

    def go_forward(self, step: int = 1) -> Any:
        self.coords[1] += step

    def go_back(self, step: int = 1) -> Any:
        self.coords[1] -= step

    def go_left(self, step: int = 1) -> Any:
        self.coords[0] -= step

    def go_right(self, step: int = 1) -> Any:
        self.coords[0] += step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str,
                 weight: int,
                 coords: list | None = None) -> None:
        if coords is None:
            coords = [0, 0, 0]
        super().__init__(name, weight, coords)

    def go_up(self, step: int = 1) -> Any:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> Any:
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str,
                 weight: int,
                 max_load_weight: Union[int, float],
                 current_load: Cargo | None = None,
                 coords: list | None = None) -> None:
        if coords is None:
            coords = [0, 0, 0]
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None


cargo = Cargo(14)
drone = DeliveryDrone(
    name="Jim",
    weight=18,
    coords=[11, -4, 16],
    max_load_weight=20,
    current_load=None,
)
drone.hook_load(cargo)
# drone.current_load is cargo
print(drone.current_load)

# cargo2 = Cargo(2)
# drone.hook_load(cargo2)
# # drone.current_load is cargo
# # didn't hook cargo2, cargo already in current load
