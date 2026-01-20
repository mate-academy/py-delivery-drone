class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list = (0, 0)
    ) -> None:
        self.name = name
        self.weight = weight
        self.coords = list(coords)

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step
        return

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step
        return

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step
        return

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step
        return

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list = (0, 0, 0)
    ) -> None:
        super().__init__(name=name, weight=weight, coords=coords)

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step
        return

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step
        return


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list = (0, 0, 0),
            max_load_weight: int = 0,
            current_load: Cargo = None
    ) -> None:
        super().__init__(name=name, weight=weight, coords=coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if (
                self.current_load is None
                and self.max_load_weight >= cargo.weight
        ):
            self.current_load = cargo
        return

    def unhook_load(self) -> None:
        self.current_load = None
        return
