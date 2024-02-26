from typing import List


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
        self,
        name: str,
        weight: int,
        coords: List[int] = None,
    ) -> None:
        if coords is None:
            coords = [0, 0]
        self.name = name
        self.weight = weight
        self.coords = coords
        # not unpacking, because while take FlyingRobot coords have a error
        self.x = coords[0]
        self.y = coords[1]

    def go_forward(self, step: int = 1) -> None:
        self.y += step
        self.coords[1] = self.y

    def go_back(self, step: int = 1) -> None:
        self.y -= step
        self.coords[1] = self.y

    def go_right(self, step: int = 1) -> None:
        self.x += step
        self.coords[0] = self.x

    def go_left(self, step: int = 1) -> None:
        self.x -= step
        self.coords[0] = self.x

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        coords: List[int] = None,

    ) -> None:
        if coords is None:
            coords = [0, 0, 0]
        self.z = coords[2]
        super().__init__(name=name, weight=weight, coords=coords)

    def go_up(self, step: int = 1) -> None:
        self.z += step
        self.coords[2] = self.z

    def go_down(self, step: int = 1) -> None:
        self.z -= step
        self.coords[2] = self.z


class DeliveryDrone(FlyingRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        max_load_weight: int,
        current_load: Cargo | None = None,
        coords: List[int] = None,
    ) -> None:
        if coords is None:
            coords = [0, 0, 0]
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if not self.current_load and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
