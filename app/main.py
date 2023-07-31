from typing import Optional


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int,
                 coords: Optional[list] = None) -> None:
        """
        Initialize a BaseRobot.

        :param name: The name of the robot.
        :param weight: The weight of the robot.
        :param coords: The initial coordinates of the robot. Defaults to [0, 0, 0].
        """
        self.name = name
        self.weight = weight
        self.coords = coords if coords is not None else [0, 0, 0]

    def go_forward(self, step: int = 1) -> None:
        """Move the robot forward by the specified step."""
        self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        """Move the robot back by the specified step."""
        self.coords[1] -= step

    def go_right(self, step: int = 1) -> None:
        """Move the robot to the right by the specified step."""
        self.coords[0] += step

    def go_left(self, step: int = 1) -> None:
        """Move the robot to the left by the specified step."""
        self.coords[0] -= step

    def get_info(self) -> str:
        """Get information about the robot."""
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int,
                 coords: Optional[list] = None) -> None:
        """
        Initialize a FlyingRobot.

        :param name: The name of the flying robot.
        :param weight: The weight of the flying robot.
        :param coords: The initial coordinates of the flying robot. Defaults to [0, 0, 0].
        """
        super().__init__(name, weight, coords)

    def go_up(self, step: int = 1) -> None:
        """Move the flying robot up by the specified step."""
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        """Move the flying robot down by the specified step."""
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str, weight: int, max_load_weight: int,
                 current_load: Optional[Cargo] = None,
                 coords: Optional[list] = None) -> None:
        """
        Initialize a DeliveryDrone.

        :param name: The name of the delivery drone.
        :param weight: The weight of the delivery drone.
        :param max_load_weight: The maximum load weight the delivery drone can carry.
        :param current_load: The current cargo loaded on the delivery drone. Defaults to None.
        :param coords: The initial coordinates of the delivery drone. Defaults to [0, 0, 0].
        """
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        """Hook a cargo to the delivery drone, if the current load is None and the cargo weight is within the max load weight."""
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        """Unhook the current cargo from the delivery drone."""
        self.current_load = None
