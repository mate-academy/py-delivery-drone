from __future__ import annotations


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        self.name = name
        self.weight = weight
        if coords is None:
            self.coords = [0, 0]
        else:
            self.coords = coords

    def go_forward(self, step: int = 1) -> None:
        if step > 0:
            self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        if step > 0:
            self.coords[1] -= step

    def go_right(self, step: int = 1) -> None:
        if step > 0:
            self.coords[0] += step

    def go_left(self, step: int = 1) -> None:
        if step > 0:
            self.coords[0] -= step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        if coords is None:
            coords_2d = [0, 0]
        elif len(coords) == 2:
            coords_2d = coords
        else:
            coords_2d = coords[:2]

        super().__init__(name=name, weight=weight, coords=coords_2d)

        if coords is None:
            self.coords = [0, 0, 0]
        elif len(coords) == 2:
            self.coords = [coords[0], coords[1], 0]
        else:
            self.coords = coords

    def go_up(self, step: int = 1) -> None:
        if step > 0:
            self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        if step > 0:
            self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(self,
                 name: str,
                 weight: int,
                 max_load_weight: int,
                 current_load: Cargo | None,
                 coords: list = None) -> None:
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
