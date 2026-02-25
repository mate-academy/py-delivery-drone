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
        pass

    def go_forward(self, step: int = 1) -> None:
        pass

    def go_right(self, step: int = 1) -> None:
        pass

    def go_left(self, step: int = 1) -> None:
        pass

    def go_back(self, step: int = 1) -> None:
        pass

    def get_info(self) -> str:
        pass


class FlyingRobot(BaseRobot):

    def __init__(
            self,
            name: str,
            weight: int | float,
            coords: list | None = None
    ) -> None:
        pass

    def go_up(self, step: int = 1) -> None:
        pass

    def go_down(self, step: int = 1) -> None:
        pass


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
