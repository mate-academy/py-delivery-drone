class Cargo:
    def __init__(self, weight: float) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
            self,
            name: str,
            weight: float,
            coords: list = None
    ) -> None:
        self.name = name
        self.weight = weight
        self.coords = [0, 0] if coords is None else coords

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"

    def go_forward(self, step: int = 1) -> list:
        one_step_move = self.coords
        one_step_move[1] += 1 if step is None else step
        return one_step_move

    def go_back(self, step: int = 1) -> list:
        one_step_move = self.coords
        one_step_move[1] -= 1 if step is None else step
        return one_step_move

    def go_right(self, step: int = 1) -> list:
        one_step_move = self.coords
        one_step_move[0] += 1 if step is None else step
        return one_step_move

    def go_left(self, step: int = 1) -> list:
        one_step_move = self.coords
        one_step_move[0] -= 1 if step is None else step
        return one_step_move


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: float,
            coords: list = None
    ) -> None:
        super().__init__(name, weight)
        self.coords = [0, 0, 0] if coords is None else coords

    def go_up(self, step: int = 1) -> list:
        one_step_move = self.coords
        one_step_move[2] += 1 if step is None else step
        return one_step_move

    def go_down(self, step: int = 1) -> list:
        one_step_move = self.coords
        one_step_move[2] -= 1 if step is None else step
        return one_step_move


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: float,
            coords: list = None,
            max_load_weight: int = None,
            current_load: int = None
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, argument: Cargo) -> None:
        if self.current_load is None and argument.weight <= self.max_load_weight:
            self.current_load = argument

    def unhook_load(self) -> None:
        self.current_load = None
