from typing import Optional


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list[int] | None = None
    ) -> None:
        """
        Representation of a common robot that can move along
        two cartesian axes.

        Attributes:
            name (str): name of the robot.
            weight (int | float): represents how many kg it weighs.
            coords (list | None): coordinates with two cartesian axes [x, y].
        """
        self.name = name
        self.weight = weight
        self.coords = coords or [0, 0]

    def go_forward(
        self,
        step: int = 1
    ) -> None:
        """
        Moves the robot forward by increasing the Y axis.

        Args:
            step (int): Number of steps to move. Defaults to 1.
        """
        self.coords[1] += step

    def go_back(
        self,
        step: int = 1
    ) -> None:
        """
        Moves the robot backward by decreasing the Y axis.

        Args:
            step (int): Number of steps to move. Defaults to 1.
        """
        self.coords[1] -= step

    def go_right(
        self,
        step: int = 1
    ) -> None:
        """
        Moves the robot to the right by increasing the X axis.

        Args:
            step (int): Number of steps to move. Defaults to 1.
        """
        self.coords[0] += step

    def go_left(
        self,
        step: int = 1
    ) -> None:
        """
        Moves the robot to the left by decreasing the X axis.

        Args:
            step (int): Number of steps to move. Defaults to 1.
        """
        self.coords[0] -= step

    def get_info(
        self
    ) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
        self,
        name: str,
        weight: int | float,
        coords: list[int] | None = None
    ) -> None:
        """
        It represents a robot with the ability to fly.

        Attributes:
            name (str): the robot's name.
            weight (int | float): the robot's weight.
            coords (list[int]): the cardinal position along the
                three axes [x, y, z].
        """
        super().__init__(name, weight, coords)
        if len(self.coords) == 2:
            self.coords.append(0)

    def go_up(
        self,
        step: int = 1
    ) -> None:
        """
        Move the robot upwards by incrementing the z-axis.

        Args:
            step (int): Number of steps to move. The default value is 1.
        """
        self.coords[2] += step

    def go_down(
        self,
        step: int = 1
    ) -> None:
        """
        Move the robot downwards by decreasing the z-axis.

        Args:
            step (int): Number of steps to move. The default value is 1.
        """
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        max_load_weight: int,
        coords: list[int] | None = None,
        current_load: Optional["Cargo"] | None = None
    ) -> None:
        """
        Represents a delivery robot that can fly.

        Attributes:
            name (str): Name of the robot.
            weight (int): The weight of the robot.
            coords (list[int]): The 3d position of the robot.
            max_load_weight (int): The total weight the robot can carry.
            current_load ("Cargo"): The load it is currently carrying.
        """
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = None
        if current_load is not None:
            self.hook_load(current_load)

    def hook_load(
        self,
        load: "Cargo"
    ) -> None:
        """
        Manages the robot's current load, which cannot be more than
        one instance of Cargo or exceed the robot's maximum load.

        Args:
            load ("Cargo"): Cargo instance that the robot would load if
            the requirements are met.
        """
        if (
            self.current_load is None
            and isinstance(load, Cargo)
            and load.weight <= self.max_load_weight
        ):
            self.current_load = load

    def unhook_load(
        self
    ) -> None:
        """
        Remove the load from the robot's hook.
        """
        self.current_load = None
