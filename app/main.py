from typing import List, Optional


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
            self,
            name: str,
            weight: int,
            coords: Optional[List[int]] = None
    ) -> None:
        if coords is None:
            coords = [0, 0]

        self.name = name
        self.weight = weight
        self.coords = coords
        self.cargo = None

    def go_forward(self, steps: int = 1) -> None:
        self.coords[1] += steps

    def go_back(self, steps: int = 1) -> None:
        self.coords[1] -= steps

    def go_right(self, steps: int = 1) -> None:
        self.coords[0] += steps

    def go_left(self, steps: int = 1) -> None:
        self.coords[0] -= steps

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"

    def take_cargo(self, cargo: Cargo) -> None:
        if self.cargo is None:
            self.cargo = cargo


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: Optional[List[int]] = None
    ) -> None:
        if coords is None:
            coords = [0, 0, 0]

        if len(coords) == 3:
            super().__init__(name, weight, coords[:2])
        else:
            coords.append(0)
            super().__init__(name, weight, coords[:2])
        self.coords = coords

    def go_up(self, steps: int = 1) -> None:
        self.coords[2] += steps

    def go_down(self, steps: int = 1) -> None:
        self.coords[2] -= steps


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            max_load_weight: int,
            coords: Optional[List[int]] = None,
            current_load: Optional[Cargo] = None,
    ) -> None:
        if coords is None:
            coords = [0, 0, 0]
        elif len(coords) == 2:
            coords = coords + [0]

        super().__init__(name, weight, coords)

        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None:
            if cargo.weight <= self.max_load_weight:
                self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
