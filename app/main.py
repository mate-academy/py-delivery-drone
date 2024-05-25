class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list = [0, 0]
    ) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords

    def go_forward(self, number: int = 1) -> None:
        if len(self.coords) == 3:
            self.coords = [
                self.coords[0],
                self.coords[1] + number,
                self.coords[2]
            ]
        else:
            self.coords = [self.coords[0], self.coords[1] + number]

    def go_back(self, number: int = 1) -> None:
        if len(self.coords) == 3:
            self.coords = [
                self.coords[0],
                self.coords[1] - number,
                self.coords[2]
            ]
        else:
            self.coords = [self.coords[0], self.coords[1] - number]

    def go_right(self, number: int = 1) -> None:
        if len(self.coords) == 3:
            self.coords = [
                self.coords[0] + number,
                self.coords[1],
                self.coords[2]
            ]
        else:
            self.coords = [self.coords[0] + number, self.coords[1]]

    def go_left(self, number: int = 1) -> None:
        if len(self.coords) == 3:
            self.coords = [
                self.coords[0] - number,
                self.coords[1],
                self.coords[2]
            ]
        else:
            self.coords = [self.coords[0] - number, self.coords[1]]

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list = [0, 0, 0]
    ) -> None:
        super().__init__(name, weight)
        self.coords = coords

    def go_up(self, number: int = 1) -> None:
        self.coords = [
            self.coords[0],
            self.coords[1],
            self.coords[2] + number
        ]

    def go_down(self, number: int = 1) -> None:
        self.coords = [
            self.coords[0],
            self.coords[1],
            self.coords[2] - number
        ]


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            max_load_weight: int,
            coords: list = [0, 0, 0],
            current_load: None = None
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, another: Cargo) -> None:
        if (
                self.current_load is None
                and another.weight <= self.max_load_weight
        ):
            self.current_load = another

    def unhook_load(self) -> None:
        self.current_load = None
