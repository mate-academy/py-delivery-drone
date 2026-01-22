from typing import Union, List


class BaseRobot:
    def __init__(
            self,
            name: str,
            weight: Union[int, float],
            coords: List[int] = [0, 0]
    ) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"

    def go_forward(self, step: int = 1) -> None:
        """
        Positive Y axis is forward
        """

        x, y, *c = self.coords
        y += step

        self.coords = [x, y, *c]

    def go_back(self, step: int = 1) -> None:
        """
        Negative Y axis is back
        """

        x, y, *c = self.coords
        y -= step

        self.coords = [x, y, *c]

    def go_right(self, step: int = 1) -> None:
        """
        Positive X axis is right
        """
        x, y, *c = self.coords
        x += step

        self.coords = [x, y, *c]

    def go_left(self, step: int = 1) -> None:
        """
        Negative X axis is left
        """
        x, y, *c = self.coords
        x -= step

        self.coords = [x, y, *c]
