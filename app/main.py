from typing import List, Optional


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot(Cargo):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: List[int] = None
    ) -> None:
        super().__init__(weight)
        self.name = name
        if coords is None:
            self.coords = [0, 0]
        else:
            self.coords = coords

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


robot = BaseRobot(name="fry", weight=5, coords=[2, 3])
robot.go_forward(5)
print(robot.coords)  # [2, 8], тобто до 3(по осі У) додали 5
robot.go_left(6)
print(robot.coords)  # [-4, 8], тобто від 2(по осі Х) відняли 6
print(robot.get_info())  # Robot: fry, Weight: 5


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: List[int] = None):
        super().__init__(name, weight, coords)
        if coords is None:
            self.coords = [0, 0, 0]
        else:
            self.coords = coords

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step


flying_robot = FlyingRobot(name="Mike", weight=11)
flying_robot.go_up(10)  # [0, 0, 10]
print(flying_robot.coords)


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            max_load_weight: int,
            coords: List[int] = None,
            current_load: Optional[Cargo] = None
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> bool:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo
            return True
        return False

    def unhook_load(self) -> None:
        self.current_load = None
