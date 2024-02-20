class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self,
                 name: str,
                 weight: int,
                 coords: list = None) -> None:
        self.name = name
        self.weight = weight
        self.coords = [coords[0], coords[1]]

    def go_forward(self, step: int = 1):
        self.coords[1] += step

    def go_back(self, step: int = 1):
        self.coords[1] -= step

    def go_right(self, step: int = 1):
        self.coords[0] += step

    def go_left(self, step: int = 1):
        self.coords[0] -= step


class FlyingRobot(BaseRobot):
    def __init__(self,
                 name: str,
                 weight: int,
                 coords: list = None) -> None:
        super().__init__(name, weight, coords)
        self.coords.append(coords[2])

    def go_up(self, step: int = 1):
        self.coords[2] += step

    def go_down(self, step: int = 1):
        self.coords[2] -= step

class DeliveryDrone(FlyingRobot):
    def __init__(self,
                 name: str,
                 weight: int,
                 current_load: Cargo,
                 coords: list = None,
                 max_load_weight: int = 0) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, inst:Cargo):
        if (self.current_load is None) and (inst.weight < self.max_load_weight):
            self.current_load = inst

    def unhook_load(self):
        self.current_load = None
