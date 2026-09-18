class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int,
                 coords: list | None = None) -> None:

        self.name = name
        self.weight = weight

        if coords is None:
            self.coords = [0, 0]
        else:
            self.coords = coords

    def go_forward(self, steps: int = 1) -> None:
        self.coords[1] += steps

    def go_back(self, steps: int = 1) -> None:
        self.coords[1] -= steps

    def go_right(self, steps: int = 1) -> None:
        self.coords[0] += steps

    def go_left(self, steps: int = 1) -> None:
        self.coords[0] -= steps

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int,
                 coords: list | None = None) -> None:

        if coords is None:
            coord = [0, 0, 0]
            super().__init__(name, weight, coord[:2])
            self.coords.append(coord[2])
        else:
            super().__init__(name, weight, coords[:2])
            self.coords.append(coords[2])

    def go_up(self, steps: int = 1) -> None:
        self.coords[2] += steps

    def go_down(self, steps: int = 1) -> None:
        self.coords[2] -= steps


class DeliveryDrone(FlyingRobot):

    def __init__(self, name: str, weight: int, max_load_weight: int,
                 current_load: Cargo | None = None,
                 coords: list | None = None) -> None:

        if coords is None:
            coords = [0, 0, 0]
            super().__init__(name, weight, coords)
        super().__init__(name, weight, coords)

        self.current_load = current_load if current_load else None

        self.max_load_weight = max_load_weight

    def hook_load(self, cargo: Cargo) -> None:
        if not self.current_load and not cargo.weight > self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
