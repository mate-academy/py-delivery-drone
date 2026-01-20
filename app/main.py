class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
        self,
        name: str,
        weight: int,
        coords: list[int] | None = None
    ) -> None:
        if weight <= 0:
            raise ValueError("Weight must be a positive integer")

        if coords is None:
            coords = [0, 0]
        elif not isinstance(coords, list):
            raise ValueError("Coords must be a list of integers")
        elif len(coords) not in {2, 3}:
            raise ValueError("Coords must be a list of two or three integers")

        self.name = name
        self.weight = weight
        self.coords = coords

    def go_forward(self, step: int = 1) -> None:
        self._validate_step(step)
        self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        self._validate_step(step)
        self.coords[1] -= step

    def go_right(self, step: int = 1) -> None:
        self._validate_step(step)
        self.coords[0] += step

    def go_left(self, step: int = 1) -> None:
        self._validate_step(step)
        self.coords[0] -= step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"

    @staticmethod
    def _validate_step(step: int) -> None:
        if not isinstance(step, int) or step <= 0:
            raise ValueError("Step must be a positive integer")


class FlyingRobot(BaseRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        coords: list[int] | None = None
    ) -> None:
        if coords is None:
            coords = [0, 0, 0]
        elif len(coords) == 2:
            coords = [*coords, 0]

        super().__init__(name, weight, coords)

    def go_up(self, step: int = 1) -> None:
        self._validate_step(step)
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self._validate_step(step)
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        max_load_weight: int,
        coords: list[int] | None = None,
        current_load: Cargo | None = None
    ) -> None:
        super().__init__(name, weight, coords)

        if max_load_weight <= 0:
            raise ValueError("max_load_weight must be a positive integer")

        self.max_load_weight = max_load_weight
        self.current_load = None

        if current_load is not None:
            self.hook_load(current_load)

    def hook_load(self, cargo: Cargo) -> None:
        if (
                self.current_load is None
                and cargo.weight <= self.max_load_weight
        ):
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
