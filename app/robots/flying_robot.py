from app.robots.base_robot import BaseRobot


class FlyingRobot(BaseRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        coords: list[int] | None = None,
    ) -> None:
        if coords is None:
            coords = [0, 0, 0]

        elif len(coords) == 2:
            coords.append(0)

        super().__init__(
            name=name,
            weight=weight,
            coords=coords,
        )

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step
