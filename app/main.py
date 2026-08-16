class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list = None):
        if coords is None:
            coords = [0, 0]
        self.name = name
        self.weight = weight
        self.coords = coords

    def go_forward(self, step: int = 1):
        self.step = step
        self.coords[1] += self.step

    def go_back(self, step: int = 1):
        self.step = step
        self.coords[1] -= self.step

    def go_right(self, step: int = 1):
        self.step = step
        self.coords[0] += self.step

    def go_left(self, step: int = 1):
        self.step = step
        self.coords[0] -= self.step

    def get_info(self) -> str:
        return (f"Robot: {self.name}, Weight: {self.weight}")


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list = None):
        if coords is None:
            coords = [0, 0, 0]
        elif len(coords) == 2:
            coords.append(0)
        super().__init__(
            name,
            weight,
            coords
        )
        self.name = name
        self.weight = weight
        self.coords = coords

    def go_up(self, step: int = 1) -> None:
        self.step = step
        self.coords[2] += self.step

    def go_down(self, step: int = 1) -> None:
        self.step = step
        self.coords[2] -= self.step


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            max_load_weight: int,
            coords: list = None,
            current_load: "Cargo" = None):
        if coords is None:
            coords = [0, 0, 0]
        super().__init__(
            name,
            weight,
            coords,)
        self.name = name
        self.weight = weight
        self.coords = coords
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo):
        if (
            self.current_load is None
            and self.max_load_weight >= cargo.weight
        ):
            self.current_load = cargo
        else:
            return

    def unhook_load(self):
        self.current_load = None
