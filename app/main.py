from __future__ import annotations


class Cargo:
    """Represents a cargo with a specific weight."""
    def __init__(self, weight: int) -> None:
        """Initialize cargo with its weight."""
        self.weight = weight


class BaseRobot:
    """
    A base class for all robots, managing name, weight, and 2D coordinates.
    """
    def __init__(
            self,
            name: str,
            weight: int | float,
            coords: list | None = None
    ) -> None:
        """
        Initialize the robot. If coords are not provided, default [0, 0].
        """
        self.name = name
        self.weight = weight
        # If coordinates are not passed, set [0, 0] by default
        self.coords = (coords or [0, 0]).copy()

    def go_forward(self, step: int = 1) -> None:
        """Move the robot forward by increasing the Y coordinate."""
        self.coords[1] += step

    def go_right(self, step: int = 1) -> None:
        """Move the robot right by increasing the X coordinate."""
        self.coords[0] += step

    def go_left(self, step: int = 1) -> None:
        """Move the robot left by decreasing the X coordinate."""
        self.coords[0] -= step

    def go_back(self, step: int = 1) -> None:
        """Move the robot back by decreasing the Y coordinate."""
        self.coords[1] -= step

    def get_info(self) -> str:
        """Return a string with the robot's name and weight."""
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    # """
    # A robot capable of moving in 3D space (X, Y, Z).
    # """
    def __init__(
            self,
            name: str,
            weight: int | float,
            coords: list | None = None
    ) -> None:
        """
        Initialize a flying robot with 3D coordinates.
        Defaults to [0, 0, 0] if coords are None.
        """
        if coords is None:
            coords = [0, 0, 0]
        elif len(coords) == 2:
            coords = coords.copy()
            coords.append(0)
        super().__init__(name, weight, coords)

    def go_up(self, step: int = 1) -> None:
        """Move the robot up by increasing the Z coordinate."""
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        """Move the robot down by increasing the Z coordinate."""
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    # """
    # A drone that can fly and carry cargo within its weight limit.
    # """
    def __init__(
            self,
            name: str,
            weight: int | float,
            max_load_weight: int | float = 0,
            current_load: Cargo | None = None,
            coords: list | None = None
    ) -> None:
        """
        Initialize the drone with a maximum load capacity and current cargo.
        """
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = None
        if current_load:
            self.hook_load(current_load)

    def hook_load(self, cargo: Cargo) -> None:
        """
        Attach cargo to the drone if it's currently empty
        and the cargo weight is within limits.
        """
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        """Remove the current cargo from the drone."""
        self.current_load = None
