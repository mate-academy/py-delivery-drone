class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, weight: int, name: str, coords: list | None = None) -> None:
        self.weight = weight
        self.name = name
        self.coords = coords if coords is not None else [0, 0]

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, weight: int, name: str, coords: list | None = None) -> None:
        if coords is None:
            coords = [0, 0, 0]
        super().__init__(weight, name, coords[:2])
        self.z = coords[2]

    def go_up(self, step: int = 1) -> None:
        self.z += step

    def go_down(self, step: int = 1) -> None:
        self.z -= step


class DeliveryDrone(FlyingRobot):
    def __init__(self, weight: int, name: str,
                 coords: list | None = None, max_load_weight: int = 0,
                 current_load: Cargo | None = None) -> None:
        super().__init__(weight, name, coords)
        self.max_load_weight = max_load_weight
        self.current_load = None

        if current_load is not None:
            self.hook_load(current_load)

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and self.max_load_weight >= cargo.weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
