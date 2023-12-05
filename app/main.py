from __future__ import annotations
class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords=None | list) -> None:
        if coords is None:
            coords = [0, 0]
        self.name = name
        self.weight = weight
        self.coords = coords

    def go_forward(self, step=1 | int):
        x, y, *z = self.coords
        y += step
        self.coords = [x, y, *z]
        return self.coords

    def go_back(self, step=1 | int):
        x, y, *z = self.coords
        y -= step
        self.coords = [x, y, *z]
        return self.coords

    def go_right(self, step=1 | int):
        x, y, *z = self.coords
        x += step
        self.coords = [x, y, *z]
        return self.coords

    def go_left(self, step=1 | int):
        x, y, *z = self.coords
        x -= step
        self.coords = [x, y, *z]
        return self.coords

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords=None | list) -> None:
        if coords is None:
            coords = [0, 0, 0]
        super().__init__(name, weight, coords)

    def go_up(self, step=1 | int):
        x, y, z = self.coords
        z += step
        self.coords = [x, y, z]
        return self.coords

    def go_down(self, step=1 | int):
        x, y, z = self.coords
        z -= step
        self.coords = [x, y, z]
        return self.coords


class DeliveryDrone(FlyingRobot):
    def __init__(self,
                 name: str,
                 weight: int,
                 max_load_weight: int,
                 coords=None | list,
                 current_load=None | int) -> None:
        if coords is None:
            coords = [0, 0, 0]
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo):
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self):
        self.current_load = None
