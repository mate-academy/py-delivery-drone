from __future__ import annotations


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
            self: BaseRobot,
            name: str,
            weight: int,
            coords: list[int] | None = None
    ) -> None:
        if coords is None:
            coords = [0, 0]
        self.name = name
        self.weight = weight
        self.coords = coords

    def go_forward(
            self: BaseRobot,
            step: int = 1
    ) -> None:
        self.coords[1] += step

    def go_back(
            self: BaseRobot,
            step: int = 1
    ) -> None:
        self.coords[1] -= step

    def go_right(
            self: BaseRobot,
            step: int = 1
    ) -> None:
        self.coords[0] += step

    def go_left(
            self: BaseRobot,
            step: int = 1
    ) -> None:
        self.coords[0] -= step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
            self: FlyingRobot,
            name: str,
            weight: int,
            coords: list[int] | None = None
    ) -> None:
        if coords is None:
            coords = [0, 0, 0]
        super().__init__(name, weight, coords)

    def go_up(self: FlyingRobot, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self: FlyingRobot, step: int = 1) -> None:
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(
            self: DeliveryDrone,
            name: str,
            weight: int,
            max_load_weight: int,
            current_load: Cargo | None,
            coords: list[int] | None = None
    ) -> None:
        if coords is None:
            coords = [0, 0, 0]
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = None
        if current_load is not None:
            self.hook_load(current_load)

    def hook_load(
            self: DeliveryDrone,
            cargo: Cargo | None
    ) -> None:
        if self.current_load is None:
            if cargo.weight <= self.max_load_weight:
                self.current_load = cargo

    def unhook_load(self: DeliveryDrone) -> None:
        self.current_load = None
