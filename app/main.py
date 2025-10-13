from __future__ import annotations


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
        self,
        name: str,
        weight: int,
        coords: list[int] | None = None,
    ) -> None:
        if coords is None:
            coords = [0, 0]
        self.name = name
        self.weight = weight
        self.x, self.y = coords
        self.coords = [self.x, self.y]

    def _sync(self) -> None:
        if hasattr(self, "z"):
            # type: ignore[attr-defined]
            self.coords = [self.x, self.y, self.z]
        else:
            self.coords = [self.x, self.y]

    def go_forward(self, dist: int = 1) -> None:
        self.y += dist
        self._sync()

    def go_back(self, dist: int = 1) -> None:
        self.y -= dist
        self._sync()

    def go_right(self, dist: int = 1) -> None:
        self.x += dist
        self._sync()

    def go_left(self, dist: int = 1) -> None:
        self.x -= dist
        self._sync()

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        coords: list[int] | None = None,
    ) -> None:
        if coords is None:
            coords = [0, 0, 0]
        x, y, z = coords
        super().__init__(name, weight, [x, y])
        self.z = z
        self._sync()

    def go_up(self, dist: int = 1) -> None:
        self.z += dist
        self._sync()

    def go_down(self, dist: int = 1) -> None:
        self.z -= dist
        self._sync()


class DeliveryDrone(FlyingRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        max_load_weight: int,
        current_load: Cargo | None = None,
        coords: list[int] | None = None,
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
