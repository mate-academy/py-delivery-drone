from typing import Union, List
from .baseRobot import BaseRobot


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: Union[int, float],
            coords: List[int] = [0, 0, 0]
    ) -> None:
        super().__init__(name, weight, coords)

    def go_up(self, step: int = 1) -> None:
        """
        Changing z coordinate
        Positive Z axis is up
        """
        x, y, z = self.coords
        z += step

        self.coords = [x, y, z]

    def go_down(self, step: int = 1) -> None:
        """
        Changing z coordinate
        Negative Z axis is down
        """
        x, y, z = self.coords
        z -= step

        self.coords = [x, y, z]
