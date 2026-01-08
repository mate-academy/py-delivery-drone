class BaseRobot:
    def __init__(
        self, name: str, weight: int, coords: list[int] | None = None
    ) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords or [0, 0]

    def __str__(self) -> str:
        return (
            f"Drone: {self.name}, Weight: {self.weight}, Coords: {self.coords}"
        )

    def go_forward(self, step: int = 1) -> None:
        print(self)
        self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"
