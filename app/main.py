from typing import Optional, List


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
        self,
        name: str,
        weight: int,
        coords: Optional[List[int]] = None,
    ) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords if coords is not None else [0, 0]  # [x, y]

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
    def __init__(
        self,
        name: str,
        weight: int,
        coords: Optional[List[int]] = None,
    ) -> None:
        if coords is None:
            coords3d = [0, 0, 0]
        else:
            if len(coords) >= 3:
                coords3d = coords[:3]
            elif len(coords) == 2:
                coords3d = [coords[0], coords[1], 0]
            elif len(coords) == 1:
                coords3d = [coords[0], 0, 0]
            else:
                coords3d = [0, 0, 0]

        # Pass only (x, y) to BaseRobot; keep full (x, y, z) here.
        super().__init__(name, weight, coords3d[:2])
        self.coords3d: List[int] = coords3d

    def go_forward(self, step: int = 1) -> None:
        super().go_forward(step)
        self.coords3d[1] = self.coords[1]

    def go_back(self, step: int = 1) -> None:
        super().go_back(step)
        self.coords3d[1] = self.coords[1]

    def go_right(self, step: int = 1) -> None:
        super().go_right(step)
        self.coords3d[0] = self.coords[0]

    def go_left(self, step: int = 1) -> None:
        super().go_left(step)
        self.coords3d[0] = self.coords[0]

    def go_up(self, step: int = 1) -> None:
        self.coords3d[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords3d[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        max_load_weight: int,
        coords: Optional[List[int]] = None,
        current_load: Optional[Cargo] = None,
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight

        self.current_load: Optional[Cargo] = None
        if current_load is not None:
            self.hook_load(current_load)

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
