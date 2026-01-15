from typing import Optional, List


class BaseRobot:
    """Base class for robots with 2D movement capabilities.

    Attributes:
        name: The name of the robot.
        weight: The weight of the robot in kilograms.
        coords: Current coordinates of the robot [x, y].
    """

    def __init__(
            self,
            name: str,
            weight: float,
            coords: Optional[List[float]] = None
    ) -> None:
        """Initializes a BaseRobot instance.

        Args:
            name: The name of the robot.
            weight: The weight of the robot in kilograms.
            coords: Starting coordinates [x, y]. Defaults to [0, 0].
        """
        self.name = name
        self.weight = weight
        self.coords = coords if coords is not None else [0, 0]

    def go_forward(self, step: int = 1) -> None:
        """Moves the robot forward along the positive Y axis.

        Args:
            step: Number of units to move. Defaults to 1.
        """
        self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        """Moves the robot backward along the negative Y axis.

        Args:
            step: Number of units to move. Defaults to 1.
        """
        self.coords[1] -= step

    def go_right(self, step: int = 1) -> None:
        """Moves the robot right along the positive X axis.

        Args:
            step: Number of units to move. Defaults to 1.
        """
        self.coords[0] += step

    def go_left(self, step: int = 1) -> None:
        """Moves the robot left along the negative X axis.

        Args:
            step: Number of units to move. Defaults to 1.
        """
        self.coords[0] -= step

    def get_info(self) -> str:
        """Returns formatted information about the robot.

        Returns:
            A string containing robot name and weight.
        """
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: float,
            coords: Optional[List[float]] = None
    ) -> None:
        """Initializes a FlyingRobot instance.

        Args:
            name: The name of the robot.
            weight: The weight of the robot in kilograms.
            coords: Starting coordinates [x, y, z].
                Defaults to [0, 0, 0].
        """
        if coords is None:
            coords = [0, 0, 0]
            parent_coords = [0, 0]
        elif len(coords) == 3:
            parent_coords = coords[:2]
        else:
            parent_coords = coords
            coords = coords + [0]

        super().__init__(name, weight, parent_coords)
        self.coords = coords

    def go_up(self, step: int = 1) -> None:
        """Moves the robot up along the positive Z axis.

        Args:
            step: Number of units to move. Defaults to 1.
        """
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        """Moves the robot down along the negative Z axis.

        Args:
            step: Number of units to move. Defaults to 1.
        """
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: float,
            coords: Optional[List[float]] = None,
            max_load_weight: float = 0,
            current_load: Optional["Cargo"] = None
    ) -> None:
        """Initializes a DeliveryDrone instance.

        Args:
            name: The name of the drone.
            weight: The weight of the drone in kilograms.
            coords: Starting coordinates [x, y, z].
                Defaults to [0, 0, 0].
            max_load_weight: Maximum cargo weight the drone can carry.
                Defaults to 0.
            current_load: Cargo to hook on initialization.
                Defaults to None.
        """
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load: Optional[Cargo] = None

        if current_load is not None:
            self.hook_load(current_load)

    def hook_load(self, cargo: "Cargo") -> None:
        """Hooks cargo to the drone if capacity allows and no cargo loaded.

        Cargo is only hooked if both conditions are met:
        - No cargo is currently loaded (current_load is None)
        - Cargo weight does not exceed max_load_weight

        Args:
            cargo: The Cargo object to hook to the drone.
        """
        if (self.current_load is None
                and cargo.weight <= self.max_load_weight):
            self.current_load = cargo

    def unhook_load(self) -> None:
        """Unhooks the current cargo from the drone.

        Sets current_load to None, releasing any loaded cargo.
        """
        self.current_load = None


class Cargo:
    """Represents cargo that can be transported by a delivery drone.

    Attributes:
        weight: The weight of the cargo in kilograms.
    """

    def __init__(self, weight: float) -> None:
        """Initializes a Cargo instance.

        Args:
            weight: The weight of the cargo in kilograms.
        """
        self.weight = weight
