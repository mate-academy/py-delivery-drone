from __future__ import annotations


class Cargo:
    def __init__(
        self,
        weight: int,
    ) -> None:

        self.weight = weight


class BaseRobot:

    def __init__(
        self,
        name: str,
        weight: int,
        coords=[0, 0]
    ) -> None:

        self.name = name
        self.weight = weight
        self.coords = coords

    def go_forward(self, step=1) -> None:
        self.coords[1] += step

    def go_back(self, step=1) -> None:
        self.coords[1] -= step

    def go_right(self, step=1) -> None:
        self.coords[0] += step

    def go_left(self, step=1) -> None:
        self.coords[0] -= step

    def get_info(self):
        info = f"Robot: {self.name}, Weight: {self.weight}"
        return info


class FlyingRobot(BaseRobot):

    def __init__(
        self,
        name: str,
        weight: int,
        coords=[0, 0]
    ) -> None:

        if len(coords) == 2:
            coords.append(0)
        super().__init__(name, weight, coords)

    def go_up(self, step=1) -> None:
        self.coords[2] += step

    def go_down(self, step=1) -> None:
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):

    def __init__(
        self,
        name: str,
        weight: int,
        coords=[0, 0],
        max_load_weight=None,
        current_load=None,
    ) -> None:

        if len(coords) == 2:
            coords.append(0)
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo):
        if not self.current_load and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self):
        self.current_load = None
