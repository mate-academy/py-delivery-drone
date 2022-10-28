class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot(Cargo):
    def __init__(self, name: str, weight: int, coords: list = (0, 0)) -> None:
        super().__init__(weight)
        self.name = name
        self.coords = coords

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step
        tuple(self.coords)

    def go_back(self, step: int = 1) -> None:
        list(self.coords)
        self.coords[1] -= step
        tuple(self.coords)

    def go_right(self, step: int = 1) -> None:
        list(self.coords)
        self.coords[0] += step
        tuple(self.coords)

    def go_left(self, step: int = 1) -> None:
        list(self.coords)
        self.coords[0] -= step
        tuple(self.coords)

class FlyingRobot(Cargo):
    def __init__(self):
robot = BaseRobot(name="Walle", weight=34, coords=[3, -2])
robot.go_forward()
print(robot.coords)
robot.go_right(5)
print(robot.coords)
robot.go_left(1)
print(robot.coords)
robot.go_back()
print(robot.coords)