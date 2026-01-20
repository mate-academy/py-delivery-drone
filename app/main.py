class Cargo:
    def __init__(self, weight: int) -> None:
        """
        Represents a cargo item that can be carried by a DeliveryDrone.
        """
        self.weight = weight


class BaseRobot:
    """
    A basic ground robot operating in a 2D coordinate system.

    Attributes:
        name: The robot's name.
        weight: The robot's weight.
        coords: A list containing the robot's [x, y] position.
    """

    def __init__(
            self,
            name: str,
            weight: int,
            coords: list[int] | None = None
    ) -> None:

        self.coords = coords or [0, 0]
        self.name = name
        self.weight = weight

    def go_right(self, step: int = 1) -> None:
        """
        Moves the robot to the right along the X axis.
        When called, the method:
            - increases the robot's x-coordinate by `step`
            - returns nothing

        :param step: Number of steps to move. Defaults to 1.
        """
        self.coords[0] += step

    def go_left(self, step: int = 1) -> None:
        """
        Moves the robot to the left along the X axis.
        When called, the method:
            - decreases the robot's x-coordinate by `step`
            - returns nothing

        :param step: Number of steps to move. Defaults to 1.
        """
        self.coords[0] -= step

    def go_forward(self, step: int = 1) -> None:
        """
        Moves the robot forward along the Y axis.
        When called, the method:
            - increases the robot's y-coordinate by `step`
            - returns nothing

        :param step: Number of steps to move. Defaults to 1.
        """
        self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        """
        Moves the robot backward along the Y axis.
        When called, the method:
            - decreases the robot's y-coordinate by `step`
            - returns nothing

        :param step: Number of steps to move. Defaults to 1.
        """
        self.coords[1] -= step

    def get_info(self) -> str:
        """
        Returns a summary of the robot.

        :return: A formatted string containing robot name and weight.
        """
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):

    def __init__(
            self,
            name: str,
            weight: int,
            coords: list[int] | None = None
    ) -> None:

        if coords is None:
            coords_list = [0, 0, 0]
        elif len(coords) == 2:
            coords_list = [coords[0], coords[1], 0]
        else:
            coords_list = coords[:3]

        super().__init__(
            name=name,
            weight=weight,
            coords=coords_list[:2]
        )
        self.coords = coords_list

    def go_up(self, step: int = 1) -> None:
        """
        Moves the robot upward along the Z axis.
        When called, the method:
            - increases the robot's z-coordinate by `step`
            - returns nothing

        :param step: Number of steps to move upward. Defaults to 1.
        """
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        """
        Moves the robot downward along the Z axis.
        When called, the method:
            - decreases the robot's z-coordinate by `step`
            - returns nothing

        :param step: Number of steps to move downward. Defaults to 1.
        """
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):

    def __init__(
            self,
            name: str,
            weight: int,
            max_load_weight: int,
            coords: list[int] | None = None,
            current_load: Cargo | None = None
    ) -> None:

        super().__init__(name=name, weight=weight, coords=coords)

        self.max_load_weight = max_load_weight
        self.current_load = None

        if current_load is not None:
            self.hook_load(current_load)

    def hook_load(self, cargo: Cargo) -> None:
        """
        Attempts to attach the given cargo to the drone.
        When cargo can be hooked:
            - the drone has no current load
            - the cargo weight does not exceed load capacity
            - sets `current_load` to the cargo

        When cargo cannot be hooked:
            - does nothing

        :param cargo: Cargo to attempt attaching.
        """

        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        """
        Detaches any currently attached cargo from the drone.

        When called:
            - clears `current_load`
            - returns nothing
        """
        self.current_load = None
