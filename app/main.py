from typing import List, Optional


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self,
                 name: str, weight: int,
                 coords: Optional[list[int]] = None) -> None:
        self.name = name
        self.weight = weight
        self.coords: List[int] = coords if coords is not None else [0, 0]

    def go_forward(self, step: int = 1) -> None:
        """Move na direção Y positiva (forward)"""
        self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        """Move na direção Y negativa (back)"""
        self.coords[1] -= step

    def go_right(self, step: int = 1) -> None:
        """Move na direção X positiva (right)"""
        self.coords[0] += step

    def go_left(self, step: int = 1) -> None:
        """Move na direção X negativa (left)"""
        self.coords[0] -= step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list | None = None) \
            -> None:
        if coords is None:
            coords_normalized = [0, 0, 0]
        elif len(coords) == 2:
            coords_normalized = coords + [0]
        else:
            coords_normalized = coords
        super().__init__(name, weight, coords_normalized)

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(self,
                 name: str,
                 weight: int,
                 coords: Optional[List[int]] = None,
                 max_load_weight: int | float = 0,
                 current_load: Optional[Cargo] = None) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load: Optional[Cargo] = None
        if current_load is not None:
            self.hook_load(current_load)

    def hook_load(self, cargo: Cargo) -> None:
        if (self.current_load is None and cargo.weight
                <= self.max_load_weight):
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
