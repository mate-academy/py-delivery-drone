from app.drone.base_robot import BaseRobot


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list[int] | None = None) -> None:
        if coords is None:
            coords = [0, 0, 0]
            x = coords[1]
            y = coords[0]
            z = coords[2]
            self.coords = [x, y, z]
        if len(coords) <= 2:
            x = coords[1]
            y = coords[0]
            z=0
            self.coords = [x, y, z]
        x = coords[1]
        y = coords[0]
        z = coords[2]
        self.coords = [x, y, z]

        super().__init__(name, weight, [x, y])

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] = self.coords[2] - step