from __future__ import annotations


class Cargo:

    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:

    def __init__(
            self,
            name: str,
            weight: int | float,
            coords: list | None = None
    ) -> None:
        self.name = name
        self.weight = weight
        # If coordinates are not passed, set [0, 0] by default
        if coords is None:
            self.coords = [0, 0]
        else:
            self.coords = coords.copy()

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):

    def __init__(
            self,
            name: str,
            weight: int | float,
            coords: list | None = None
    ) -> None:
        if coords is None:
            coords = [0, 0, 0]
        elif len(coords) == 2:
            coords = coords.copy()
            coords.append(0)
        super().__init__(name, weight, coords)

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):

    def __init__(
            self,
            name: str,
            weight: int | float,
            max_load_weight: int | float = 0,
            current_load: Cargo | None = None,
            coords: list | None = None
    ) -> None:
        pass

    def hook_load(self, cargo: Cargo | None) -> None:
        pass

    def unhook_load(self) -> None:
        pass
