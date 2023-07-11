from app.constants import X_INDEX, Y_INDEX, BASE_ROBOT_STEP


def list_isinstance(checking: list | None, value: int) -> int:
    return checking[value] if isinstance(checking, list) else 0


class BaseRobot:

    def __init__(self, name: str, weight: int,
                 coords: list | None = None) -> None:
        self.name = name
        self.weight = weight
        self.x_pos = list_isinstance(coords, X_INDEX)
        self.y_pos = list_isinstance(coords, Y_INDEX)
        self.coords = [self.x_pos, self.y_pos]

    def move(self, coord_name: str, step: int,
             simbl: str, coord_index: int) -> None:
        value = eval(f"self.{coord_name} {simbl} {step}")
        setattr(self, coord_name, value)
        self.coords[coord_index] = value

    def go_forward(self, step: int = BASE_ROBOT_STEP) -> None:
        self.move("y_pos", step, "+", Y_INDEX)

    def go_back(self, step: int = BASE_ROBOT_STEP) -> None:
        self.move("y_pos", step, "-", Y_INDEX)

    def go_right(self, step: int = BASE_ROBOT_STEP) -> None:
        self.move("x_pos", step, "+", X_INDEX)

    def go_left(self, step: int = BASE_ROBOT_STEP) -> None:
        self.move("x_pos", step, "-", X_INDEX)

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"
