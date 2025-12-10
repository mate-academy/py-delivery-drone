from typing import Optional


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list[int] | None = None) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords or [0, 0]

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
        coords: list[int] | None = None,
        altitude: int | None = 0,
    ) -> None:
        # Використовуємо коротке присвоєння coords і altitude
        super().__init__(name, weight, coords)
        self.altitude = altitude or 0

        # Забезпечуємо coords у форматі [x, y, z]
        if len(self.coords) == 2:
            self.coords.append(self.altitude)

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        max_load_weight: int,
        current_load: Optional[Cargo] = None,
        coords: list[int] | None = None,
        altitude: int | None = 0,
    ) -> None:
        super().__init__(name, weight, coords, altitude)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> str:
        if self.current_load is not None:
            return "Already have load"

        weight = cargo.weight

        if weight > self.max_load_weight:
            return "Load is too heavy"

        if weight == self.max_load_weight:
            self.current_load = cargo
            return "Load equals max weight — be careful!"

        self.current_load = cargo
        return "Load hooked"

    def unhook_load(self) -> str:
        if self.current_load is None:
            return "Nothing to unhook"

        self.current_load = None
        return "Load unhooked"