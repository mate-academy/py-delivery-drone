from __future__ import annotations


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight : int,
                 coords: list[int] | None = None) -> None:
        if coords is None:
            coords = [0, 0]
        self.name = name
        self.weight = weight
        self.coords = coords

    def go_forward(self, step: int = 1) -> None:
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
    def __init__(self, name: str, weight: int,
                 coords: list[int] | None = None) -> None:
        if coords is not None:
            if len(coords) != 3:
                raise ValueError(f"Expected 3 coordinates, got {coords}")
            if not all(isinstance(x, int) for x in coords):
                raise TypeError("coords must contain ints")
        real_coords = coords if coords is not None else [0, 0, 0]
        super().__init__(name, weight, real_coords)

    def go_up(self, step: int = 1) -> None:
        if len(self.coords) < 3:
            raise ValueError("coords must contain at least 3 coordinates")
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        if len(self.coords) < 3:
            raise ValueError("coords must contain at least 3 coordinates")
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(
            self, name: str, weight: int,
            coords: list[int] | None = None, max_load_weight: int = 0,
            current_load: Cargo | None = None) -> None:

        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = None
        if current_load is not None:
            self.hook_load(current_load)

    def hook_load(self, cargo: "Cargo") -> None:
        if self.current_load is not None:
            return
        if cargo.weight > self.max_load_weight:
            return
        self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
