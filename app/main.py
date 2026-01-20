class BaseRobot:
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list | None = None
    ) -> None:
        self.name = name
        self.weight = weight
        if coords is None:
            self.coords = [0, 0]
        else:
            self.coords = coords.copy()

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
            self, name: str,
            weight: int,
            coords: list | None = None
    ) -> None:
        super().__init__(
            name,
            weight,
            [0, 0, 0] if coords is None else [coords[0], coords[1], 0]
            if len(coords) == 2 else coords
        )

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list | None = None,
            max_load_weight: int = 0,
            current_load: "Cargo | None" = None
    ) -> None:
        super().__init__(
            name,
            weight,
            [0, 0, 0] if coords is None else coords
        )
        self.max_load_weight = max_load_weight
        self.current_load = None
        if isinstance(current_load, Cargo):
            self.hook_load(current_load)

    def hook_load(self, other: "Cargo | None") -> None:
        if self.current_load is None and other.weight <= self.max_load_weight:
            self.current_load = other

    def unhook_load(self) -> None:
        self.current_load = None


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight
