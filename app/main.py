from typing import Any


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
            self,
            name: str,
            weight: int | float,
            coords: list | Any = None
    ) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords or [0, 0]

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step
        return self.coords

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step
        return self.coords

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step
        return self.coords

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step
        return self.coords

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: int | float,
            coords: list | Any = None
    ) -> None:
        coords = coords or [0, 0, 0]
        super().__init__(name, weight, coords)

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step
        return self.coords

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step
        return self.coords


class DeliveryDrone(FlyingRobot):
    def __init__(self,
                 name: str,
                 weight: int | float,
                 max_load_weight: int,
                 coords: list | Any = None,
                 current_load: int | Any = None,
                 ) -> None:
        coords = coords or [0, 0, 0]
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if (self.current_load is None
                and cargo.weight <= self.max_load_weight):
            self.current_load = cargo
            return self.current_load

    def unhook_load(self) -> None:
        self.current_load = None


if __name__ == "__main__":
    robot = BaseRobot(name="Walle", weight=34, coords=[3, -2])
    print(robot.get_info())
    print(robot.go_forward())
    print(robot.go_right(5))

    flying_robot = FlyingRobot(name="Mike", weight=11)
    print(flying_robot.get_info())
    print(flying_robot.go_up(10))

    cargo = Cargo(14)
    drone = DeliveryDrone(
        name="Jim",
        weight=18,
        coords=[11, -4, 16],
        max_load_weight=20,
        current_load=None,
    )
    print(drone.hook_load(cargo))
    print(drone.coords)
