class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords or [0, 0]

    def go_forward(self, coord_y: int = 1) -> None:
        self.coords[1] += coord_y

    def go_back(self, coord_y: int = 1) -> None:
        self.coords[1] -= coord_y

    def go_right(self, coord_x: int = 1) -> None:
        self.coords[0] += coord_x

    def go_left(self, coord_x: int = 1) -> None:
        self.coords[0] -= coord_x

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        super().__init__(name, weight, coords)

        self.coords = coords or [0, 0, 0]

    def go_up(self, coord_z: int = 1) -> None:
        print(self.coords)
        self.coords[2] += coord_z

    def go_down(self, coord_z: int = 1) -> None:
        self.coords[2] -= coord_z


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int, coords: list = None,
            max_load_weight: int = 0,
            current_load: classmethod = None) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cls: classmethod) -> Cargo:
        if cls.weight <= self.max_load_weight:
            if self.current_load is None:
                self.current_load = cls
            else:
                print("Sorry, but drone is busy")
        else:
            print("Sorry, but weight is so big")

    def unhook_load(self) -> None:
        self.current_load = None
