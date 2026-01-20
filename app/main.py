class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords if coords is not None else [0, 0]

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
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        # If the coords list has 2 elements (x, y), append 0 for z
        if coords:
            coords = coords + [0] if len(coords) == 2 else coords
        else:
            coords = [0, 0, 0]  # Default to [0, 0, 0] if coords is None
        super().__init__(name, weight, coords)

    def go_up(self, z_coord: int = 1) -> None:
        self.coords[2] += z_coord

    def go_down(self, z_coord: int = 1) -> None:
        self.coords[2] -= z_coord


class DeliveryDrone(FlyingRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        max_load_weight: int,
        coords: list = None,
        current_load: object = None
    ) -> None:
        # Ensure coords is a list of 3 elements: [x, y, z]
        if coords:
            coords = coords[:2] + [0] if len(coords) == 2 else coords
        else:
            coords = [0, 0, 0]  # Default to [0, 0, 0] if coords is None
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: object) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
