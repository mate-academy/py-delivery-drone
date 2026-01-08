from app.robot.base.robot import BaseRobot


class FlyingRobot(BaseRobot):
    def __init__(
        self, name: str, weight: int, coords: list[int] | None = None
    ) -> None:
        super().__init__(name, weight, coords or [0, 0, 0])

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step
