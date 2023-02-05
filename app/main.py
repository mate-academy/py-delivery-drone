from typing import Optional


class Cargo:
    def __init__(self, weight: int | float) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
            self, name: str, weight: int, coords: Optional[list] = None
    ) -> None:
        self.name = name
        self.weight = weight
        self.coords = [0, 0] if coords is None else coords

    def go_forward(self, step_forward: int = 1) -> None:
        self.coords[1] += step_forward

    def go_back(self, step_back: int = 1) -> None:
        self.coords[1] -= step_back

    def go_right(self, step_right: int = 1) -> None:
        self.coords[0] += step_right

    def go_left(self, step_left: int = 1) -> None:
        self.coords[0] -= step_left

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
            self, name: str, weight: int, coords: Optional[list] = None
    ) -> None:
        super().__init__(name, weight, coords)
        self.coords = [0, 0, 0] if coords is None else coords

    def go_up(self, step_up: int = 1) -> None:
        self.coords[2] += step_up

    def go_down(self, step_down: int = 1) -> None:
        self.coords[2] -= step_down


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int | float,
            coords: Optional[list] = None,
            max_load_weight: int = 0,
            current_load: Cargo = None,
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
