class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        self.name = name
        self.weight = weight
        if coords is None:
            coords = [0, 0]
        self.coords = coords

    def go_forward(self, move: int = 1) -> None:
        self.coords[1] += move

    def go_back(self, move: int = 1) -> None:
        self.coords[1] -= move

    def go_right(self, move: int = 1) -> None:
        self.coords[0] += move

    def go_left(self, move: int = 1) -> None:
        self.coords[0] -= move

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        if coords is None:
            coords = [0, 0, 0]
        super().__init__(name, weight, coords=coords)

    def go_up(self, move: int = 1) -> None:
        self.coords[2] += move

    def go_down(self, move: int = 1) -> None:
        self.coords[2] -= move


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            max_load_weight: int,
            coords: list = None,
            current_load: Cargo = None
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = None
        if current_load is not None:
            self.hook_load(current_load)

    def hook_load(self, cargo: Cargo) -> None:
        if not isinstance(cargo, Cargo):
            raise TypeError("The cargo must be an object of class Cargo")

        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo
        else:
            print(
                f"❌ Unable to lift the load {cargo.weight} kg "
                f"(max. {self.max_load_weight} kg)"
            )

    def unhook_load(self) -> None:
        self.current_load = None
