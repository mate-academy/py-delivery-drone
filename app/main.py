from __future__ import annotations


class Cargo:
    def __init__(
            self,
            weight: int
    ) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list | None = None
    ) -> None:
        coords = coords if coords is not None else [0, 0]
        self.name = name
        self.weight = weight
        self.coords = list(coords)

    def go_forward(self, step: int = 1) -> None:
        y_coord = self.coords[1]
        y_coord += step
        self.coords[1] = y_coord

    def go_back(self, step: int = 1) -> None:
        y_coord = self.coords[1]
        y_coord -= step
        self.coords[1] = y_coord

    def go_right(self, step: int = 1) -> None:
        x_coord = self.coords[0]
        x_coord += step
        self.coords[0] = x_coord

    def go_left(self, step: int = 1) -> None:
        x_coord = self.coords[0]
        x_coord -= step
        self.coords[0] = x_coord

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list | None = None
    ) -> None:
        coords = coords if coords is not None else [0, 0, 0]
        super().__init__(name, weight, coords)

    def go_up(self, step: int = 1) -> None:
        z_coord = self.coords[2]
        z_coord += step
        self.coords[2] = z_coord

    def go_down(self, step: int = 1) -> None:
        z_coord = self.coords[2]
        z_coord -= step
        self.coords[2] = z_coord


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            max_load_weight: int,
            current_load: Cargo | None,
            coords: list | None = None
    ) -> None:
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
