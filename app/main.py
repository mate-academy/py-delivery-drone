from enum import IntEnum
from abc import ABC


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


# region Support
class ArgumentException(ValueError):
    pass


class Axis(IntEnum):
    Xc = 0
    Yc = 1
    Zc = 2

    def __int__(self) -> int:
        return super().__int__()
# endregion


class BaseRobot(ABC):
    def __init__(
        self,
        name: str,
        weight: int,
        coords: list[int] = None
    ) -> None:
        self._name: str = name
        self._weight: int = weight
        self._coords: list[int] = coords if coords is not None else [0, 0]

    def go_forward(self, step: int = 1) -> None:
        self._coords[Axis.Yc] += step

    def go_back(self, step: int = 1) -> None:
        self._coords[Axis.Yc] -= step

    def go_right(self, step: int = 1) -> None:
        self._coords[Axis.Xc] += step

    def go_left(self, step: int = 1) -> None:
        self._coords[Axis.Xc] -= step

    def get_info(self) -> str:
        return f"Robot: {self._name}, Weight: {self._weight}"

    @property
    def name(self) -> str:
        return self._name

    @property
    def weight(self) -> int:
        return self._weight

    @property
    def coords(self) -> list[int]:
        return self._coords


class FlyingRobot(BaseRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        coords: list[int] = None
    ) -> None:
        if coords is None:
            coords = [0, 0, 0]
        elif len(coords) < 3:
            raise ArgumentException("You have to provide a 3d point (x, y and "
                                    "z components) as list of integers for "
                                    "the 'coords' parameter")
        super().__init__(name, weight, coords)

    def go_up(self, step: int = 1) -> None:
        self._coords[Axis.Zc] += step

    def go_down(self, step: int = 1) -> None:
        self._coords[Axis.Zc] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        max_load_weight: int,
        current_load: int,
        coords: list[int] = None
    ) -> None:
        super().__init__(name, weight, coords)
        self.current_load = current_load
        self.max_load_weight = max_load_weight

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is not None:
            return
        if cargo is None or cargo.weight > self.max_load_weight:
            return
        self.current_load = cargo

    def unhook_load(self) -> None:
        if self.current_load is None:
            return
        self.current_load = None
