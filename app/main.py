class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
            self,
            name: str,
            weight: int,
            coords: None = None
    ) -> None:
        if coords is None:
            coords = [0, 0]
        self.name = name
        self.weight = weight
        self.coords = coords

    def change_coords(self, coord: int, num: int) -> None:
        self.coords[coord] += num

    def go_forward(self, num: int = 1) -> None:
        self.change_coords(1, num)

    def go_back(self, num: int = 1) -> None:
        self.change_coords(1, -num)

    def go_right(self, num: int = 1) -> None:
        self.change_coords(0, num)

    def go_left(self, num: int = 1) -> None:
        self.change_coords(0, -num)

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: None = None
    ) -> None:
        super().__init__(name, weight, coords)
        if coords is None:
            self.coords = [0, 0, 0]

    def go_up(self, num: int = 1) -> None:
        self.change_coords(2, num)

    def go_down(self, num: int = 1) -> None:
        self.change_coords(2, -num)


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            max_load_weight: int,
            current_load: None | int,
            name: str, weight: int,
            coords: None = None
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and self.max_load_weight >= cargo.weight:
            self.current_load = cargo
        else:
            print(
                f"Didn't hook {cargo}, "
                f"{self.current_load} "
                f"already in current load"
            )

    def unhook_load(self) -> None:
        self.current_load = None
