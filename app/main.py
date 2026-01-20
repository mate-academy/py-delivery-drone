from __future__ import annotations


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self,
                 name: str,
                 weight: int,
                 coords: list[int] = None) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords if coords is not None else [0, 0]

    def go_forward(self, coord: int = 1) -> None:
        self.coords[1] += coord

    def go_back(self, coord: int = 1) -> None:
        self.coords[1] -= coord

    def go_right(self, coord: int = 1) -> None:
        self.coords[0] += coord

    def go_left(self, coord: int = 1) -> None:
        self.coords[0] -= coord

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self,
                 name: str,
                 weight: int,
                 coords: list[int] = None) -> None:
        coords_3d = coords if coords is not None else [0, 0, 0]
        super().__init__(name=name,
                         weight=weight,
                         coords=coords_3d)

    def go_up(self, coord: int = 1) -> None:
        self.coords[2] += coord

    def go_down(self, coord: int = 1) -> None:
        self.coords[2] -= coord


class DeliveryDrone(FlyingRobot):
    def __init__(self,
                 name: str,
                 weight: int,
                 max_load_weight: int,
                 current_load: Cargo | None = None,
                 coords: list[int] = None) -> None:
        super().__init__(name=name, weight=weight, coords=coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, kg: Cargo) -> None:
        if self.current_load is None and kg.weight <= self.max_load_weight:
            self.current_load = kg

    def unhook_load(self) -> None:
        self.current_load = None
