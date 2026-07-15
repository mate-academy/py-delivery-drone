class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, cords: list[int] | None = None) -> None:
        self.name = name
        self.weight = weight
        self.cords = cords or [0, 0]

    def go_forward(self, step: int = 1) -> None:
        self.cords[1] += step

    def go_back(self, step: int = 1) -> None:
        self.cords[1] -= step

    def go_right(self, step: int = 1) -> None:
        self.cords[0] += step

    def go_left(self, step: int = 1) -> None:
        self.cords[0] -= step


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, cords: list[int] = [0, 0, 0]) -> None:
        super().__init__(name, weight, cords)

    def go_up(self, step: int = 1) -> None:
        self.cords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.cords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(self,
                 name: str,
                 weight: int,
                 max_load_weight: int,
                 current_load: Cargo | None = None,
                 cords: list[int] = [0, 0, 0]
    ) -> None:
        super().__init__(name, weight, cords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, load: Cargo) -> None:
        if self.current_load is None and load.weight <= self.max_load_weight:
            self.current_load = load

    def unhook_load(self, step: int = 1) -> None:
        self.current_load = None