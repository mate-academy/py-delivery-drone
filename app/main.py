class Cargo:
    def __init__(self, weight):
        self.weight = weight


class BaseRobot:
    def __init__(self,
                 name: str,
                 weight: int,
                 coords: list[int] = None) -> None:
        if coords is None:
            coords = [0, 0]
        if len(coords) < 2:
            coords.append(0)
        self.name = name
        self.weight = weight
        self.coords = coords

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
    def __init__(self,
                 name: str,
                 weight: int,
                 coords: list[int] = None) -> None:
        if coords is None:
            coords = [0, 0, 0]
        while len(coords) < 3:
            coords.append(0)
        z = coords.pop(2)
        super().__init__(name, weight, coords)
        if len(self.coords) == 2:
            self.coords.append(z)

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(self,
                 name: str,
                 weight: int,
                 coords: list[int] = None,
                 max_load_weight: int = None,
                 current_load: Cargo = None) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and self.max_load_weight >= cargo.weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
