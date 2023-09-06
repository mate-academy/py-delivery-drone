class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        self.name = name
        self.weight = weight
        if coords is None:
            self.coords = [0, 0]
        else:
            self.coords = coords

    def go_forward(self, num: int = 1) -> None:
        if len(self.coords) == 3:
            self.coords = [
                self.coords[0],
                self.coords[1] + num,
                self.coords[2]
            ]
        else:
            self.coords = [self.coords[0], self.coords[1] + num]

    def go_back(self, num: int = 1) -> None:
        if len(self.coords) == 3:
            self.coords = [
                self.coords[0],
                self.coords[1] - num,
                self.coords[2]
            ]
        else:
            self.coords = [self.coords[0], self.coords[1] - num]

    def go_right(self, num: int = 1) -> None:
        if len(self.coords) == 3:
            self.coords = [
                self.coords[0] + num,
                self.coords[1],
                self.coords[2]
            ]
        else:
            self.coords = [self.coords[0] + num, self.coords[1]]

    def go_left(self, num: int = 1) -> None:
        if len(self.coords) == 3:
            self.coords = [
                self.coords[0] - num,
                self.coords[1],
                self.coords[2]
            ]
        else:
            self.coords = [self.coords[0] - num, self.coords[1]]

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        print("start coords", coords)
        if coords is None:
            super().__init__(name=name, weight=weight, coords=[0, 0, 0])
        else:
            super().__init__(name=name, weight=weight, coords=coords)
        print("coords", self.coords)

    def go_up(self, num: int = 1) -> None:
        self.coords = [self.coords[0], self.coords[1], self.coords[2] + num]

    def go_down(self, num: int = 1) -> None:
        self.coords = [self.coords[0], self.coords[1], self.coords[2] - num]


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            max_load_weight: int,
            current_load: object | None = None,
            coords: list | None = None
    ) -> None:
        if coords is None:
            super().__init__(name=name, weight=weight, coords=[0, 0, 0])
        else:
            super().__init__(name=name, weight=weight, coords=coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
