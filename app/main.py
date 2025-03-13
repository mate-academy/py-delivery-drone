class Cargo:
    def __init__(self, weight: int, name: str = "Unnamed") -> None:
        if weight is None:
            raise ValueError("Weight cannot be None")
        self.name = name
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        self.weight = weight
        self.name = name
        self.coords = coords if coords is not None else [0, 0]

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step

    def __str__(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


robot = BaseRobot(name="Walle", weight=34, coords=[3, -2])
robot.go_forward(5)


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        if coords is None:
            coords = [0, 0, 0]
        super().__init__(name, weight, coords)

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step


robot1 = FlyingRobot(name="Robot", weight=14)
robot1.go_up(5)

flying_robot = FlyingRobot(name="Mike", weight=11)
flying_robot.go_up(10)


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str, weight: int,
                 coords: list = None,
                 max_load_weight: int = 100,
                 current_load: "Cargo" = None) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = None

        if current_load:
            self.hook_load(current_load)

    def hook_load(self, cargo: "Cargo") -> bool:
        if cargo.weight <= self.max_load_weight and self.current_load is None:
            self.current_load = cargo
            return True
        return False

    def unhook_load(self) -> None:
        self.current_load = None


cargo = Cargo(name="Box", weight=14)
drone = DeliveryDrone(name="Jim", weight=18, max_load_weight=20)
drone.hook_load(cargo)

drone.hook_load(cargo)
cargo2 = Cargo(2)
drone.hook_load(cargo2)

drone.unhook_load()
