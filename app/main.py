class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = [0, 0]) -> None:
        self.name = name
        self.weight = weight
        self.coords = [] + coords

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
    def __init__(self, name: str,
                 weight: int,
                 coords: list = [0, 0, 0]) -> None:
        super().__init__(name, weight, [coords[0], coords[1]])
        self.coords.append(coords[2])

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(self,
                 name: str,
                 weight: int,
                 max_load_weight: int,
                 current_load: Cargo = None,
                 **kwargs) -> None:
        coords = None
        for value in kwargs.values():
            if isinstance(value, list):
                coords = value
                break
        if coords is not None:
            super().__init__(name, weight, coords)
        else:
            super().__init__(name, weight)
        self.max_load_weight = max_load_weight
        self.current_load = None
        if current_load is not None:
            self.hook_load(current_load)

    def hook_load(self, current: Cargo) -> None:
        if (self.current_load is None
                and current.weight <= self.max_load_weight):
            self.current_load = current

    def unhook_load(self) -> None:
        self.current_load = None
