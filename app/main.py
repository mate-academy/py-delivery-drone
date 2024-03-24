class Cargo:
    def __init__(self, weight: int | float) -> None:
        self.weight = weight

    @property
    def weight(self) -> int | float:
        return self._weight

    @weight.setter
    def weight(self, value: int | float) -> None:
        if not isinstance(value, (int, float)):
            raise ValueError(
                f"""Unsupported type. Expected float or int.
                Got {type(value)} instead."""
            )
        self._weight = value


class BaseRobot(Cargo):
    def __init__(
            self,
            name: str,
            weight: int | float,
            coords: list = None
    ) -> None:
        super().__init__(weight)
        self.name = name
        self.coords = [0, 0] if not coords else coords

    def go_right(self, parameter: int | float = 1) -> None:
        self.coords[0] += parameter

    def go_left(self, parameter: int | float = 1) -> None:
        self.coords[0] -= parameter

    def go_forward(self, parameter: int | float = 1) -> None:
        self.coords[1] += parameter

    def go_back(self, parameter: int | float = 1) -> None:
        self.coords[1] -= parameter

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: int | float,
            coords: list = None
    ) -> None:
        coords = [0, 0, 0] if not coords else coords
        super().__init__(name, weight, coords)

    def go_up(self, parameter: int | float = 1) -> None:
        self.coords[2] += parameter

    def go_down(self, parameter: int | float = 1) -> None:
        self.coords[2] -= parameter


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int | float,
            current_load: int | None,
            max_load_weight: int,
            coords: list = None
    ) -> None:
        super().__init__(name, weight, coords)
        self.current_load = current_load
        self.max_load_weight = max_load_weight

    def hook_load(self, cargo: Cargo) -> None:
        if (
            not self.current_load
            and isinstance(cargo, Cargo)
            and self.max_load_weight >= cargo.weight
        ):
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
