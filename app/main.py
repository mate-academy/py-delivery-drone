from typing import Optional


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot (object):
    def __init__(self,
                 name: str,
                 weight: int,
                 coords: Optional[list[int]] = None) -> None:
        self.name = name
        self.weight = weight
        self.coords = [0, 0] if coords is None else coords

    def go_forward(self,
                   step: int = 1) -> None:
        self.coords[1] += step

    def go_back(self,
                step: int = 1) -> None:
        self.coords[1] -= step

    def go_right(self,
                 step: int = 1) -> None:
        self.coords[0] += step

    def go_left(self,
                step: int = 1) -> None:
        self.coords[0] -= step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self,
                 name: str,
                 weight: int,
                 coords: Optional[list[int]] = None) -> None:

        super().__init__(name=name,
                         weight=weight,
                         coords=[0, 0, 0] if coords is None else coords)

    def go_up(self,
              step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self,
                step: int = 1) -> None:
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(self,
                 name: str,
                 weight: int,
                 max_load_weight: int,
                 current_load: Optional[Cargo] = None,
                 coords: Optional[list[int]] = None) -> None:

        super().__init__(name=name,
                         weight=weight,
                         coords=coords)

        self.max_load_weight = max_load_weight
        self.current_load = None
        self.hook_load(current_load)

    def hook_load(self,
                  current_load: Optional[Cargo]) -> None:
        if self.current_load is not None:
            return
        if current_load is None:
            return
        if self.max_load_weight < current_load.weight:
            return

        self.current_load = current_load

    def unhook_load(self) -> None:
        self.current_load = None
