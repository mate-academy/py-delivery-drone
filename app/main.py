from __future__ import annotations


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
            self,
            name: str,
            weight: int, coords: list | None = None
    ) -> None:
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
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list | None = None
    ) -> None:
        if coords is None:
            coords3 = [0, 0, 0]
        elif len(coords) == 2:
            coords3 = coords + [0]
        elif len(coords) == 3:
            coords3 = coords
        else:
            raise ValueError

        super().__init__(name=name, weight=weight, coords=coords3)

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(
            self, name: str,
            weight: int,
            coords: list | None = None,
            max_load_weight: int | None = None,
            current_load: Cargo | None = None
    ) -> None:
        super().__init__(name=name, weight=weight, coords=coords)
        self.max_load_weight = max_load_weight
        self.current_load = None

        if current_load is not None:
            self.hook_load(current_load)

    def hook_load(self, obj: Cargo) -> None:
        if isinstance(obj, Cargo):
            if (self.current_load is None
                    and self.max_load_weight is not None
                    and obj.weight <= self.max_load_weight):
                self.current_load = obj

    def unhook_load(self) -> None:
        self.current_load = None
