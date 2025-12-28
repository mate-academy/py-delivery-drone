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
        self.name = name
        self.weight = weight
        self.coords = coords if coords is not None else [0, 0]

    def go_forward(self, value: int = 1) -> None:
        self.coords[1] += value

    def go_back(self, value: int = 1) -> None:
        self.coords[1] -= value

    def go_left(self, value: int = 1) -> None:
        self.coords[0] -= value

    def go_right(self, value: int = 1) -> None:
        self.coords[0] += value

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list[int] | None = None
    ) -> None:
        if coords is None:
            base_coords = [0, 0]
            full_coords = [0, 0, 0]
        else:
            coords = list(coords)
            if len(coords) == 2:
                base_coords = coords[:]
                full_coords = [coords[0], coords[1], 0]
            elif len(coords) == 3:
                base_coords = coords[:2]
                full_coords = coords[:]
            else:
                raise ValueError("coords must be a 2- or 3-element sequence")

        super().__init__(name=name, weight=weight, coords=base_coords)
        self.coords = full_coords

    def go_up(self, value: int = 1) -> None:
        self.coords[2] += value

    def go_down(self, value: int = 1) -> None:
        self.coords[2] -= value


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list[int] | None = None,
            max_load_weight: int = 0,
            current_load: Cargo | None = None
    ) -> None:
        super().__init__(name=name, weight=weight, coords=coords)
        self.max_load_weight = max_load_weight
        self.current_load = None

        if current_load is not None:
            self.hook_load(current_load)

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
