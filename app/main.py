from __future__ import annotations


class Cargo:
    def __init__(self, weight: float) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
            self,
            name: str,
            weight: float,
            coords: list = None
    ) -> None:
        self.name = name
        self.weight = weight
        if coords is None:
            self.coords = [0, 0]
        else:
            self.coords = [coords[0], coords[1]]

    def go_forward(self, step: float = 1) -> None:
        self.coords[1] += step

    def go_back(self, step: float = 1) -> None:
        self.coords[1] -= step

    def go_right(self, step: float = 1) -> None:
        self.coords[0] += step

    def go_left(self, step: float = 1) -> None:
        self.coords[0] -= step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: float,
            coords: list = None
    ) -> None:

        if coords is None:
            coords_xyz = [0, 0, 0]
        else:
            coords_xyz = [coords[0], coords[1], coords[2]]

        super().__init__(
            name,
            weight,
            [coords_xyz[0], coords_xyz[1]]
        )
        self.coords.append(coords_xyz[2])

    def go_up(self, step: float = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: float = 1) -> None:
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):

    def __init__(
            self,
            name: str,
            weight: float,
            max_load_weight: float,
            current_load: float,
            coords: list = None,
    ) -> None:

        if coords is None:
            coords_xyz = [0, 0, 0]
        else:
            coords_xyz = [coords[0], coords[1], coords[2]]

        super().__init__(
            name,
            weight,
            [coords_xyz[0], coords_xyz[1], coords_xyz[2]]
        )
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
