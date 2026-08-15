class Cargo:
    # """Represents cargo with a specific weight."""

    def __init__(self, weight: int) -> None:
        """Initialize cargo weight.

        Args:
            weight: The weight of the cargo.
        """

        self.weight = weight


class BaseRobot:
    # """Base ground robot with coordinate movement."""

    def __init__(
        self, name: str, weight: int, coords: list[int] | None = None
    ) -> None:
        """Initialize robot attributes and starting coordinates.

        Args:
            name: The name of the robot.
            weight: The weight of the robot.
            coords: Starting 2D coordinates [x, y].
        """
        if coords is None:
            coords = [0, 0]
        self.coords = coords
        self.weight = weight
        self.name = name

    def go_forward(self, step: int = 1) -> None:
        """Move forward along the Y-axis.

        Args:
            step: Distance to move.
        """

        self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        """Move backward along the Y-axis.

        Args:
            step: Distance to move.
        """

        self.coords[1] -= step

    def go_left(self, step: int = 1) -> None:
        """Move left along the X-axis.

        Args:
            step: Distance to move.
        """

        self.coords[0] -= step

    def go_right(self, step: int = 1) -> None:
        """Move right along the X-axis.

        Args:
            step: Distance to move.
        """

        self.coords[0] += step

    def get_info(self) -> str:
        """Return basic robot info string."""

        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    # """Robot capable of 3D flight movement."""

    def __init__(
        self, name: str, weight: int, coords: list[int] | None = None
    ) -> None:
        """Initialize flying robot with 3D coordinates.

        Args:
            name: The name of the robot.
            weight: The weight of the robot.
            coords: Starting 3D coordinates [x, y, z].
        """

        if coords is None:
            coords = [0, 0, 0]
        super().__init__(name, weight, coords)

    def go_up(self, step: int = 1) -> None:
        """Move up along the Z-axis.

        Args:
            step: Distance to move.
        """

        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        """Move down along the Z-axis.

        Args:
            step: Distance to move.
        """

        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    # """Flying drone capable of loading and delivering cargo."""

    def __init__(
        self,
        name: str,
        max_load_weight: int,
        weight: int,
        coords: list[int] | None = None,
        current_load: Cargo | None = None,
    ) -> None:
        """Initialize delivery drone with load capacity and current cargo.

        Args:
            name: The name of the drone.
            max_load_weight: Maximum weight capacity the drone can carry.
            weight: The weight of the drone itself.
            coords: Starting 3D coordinates [x, y, z].
            current_load: Initial Cargo instance, if any.
        """

        super().__init__(name, weight, coords)
        self.current_load = None
        self.max_load_weight = max_load_weight
        if current_load:
            self.hook_load(current_load)

    def hook_load(self, cargo: Cargo) -> None:
        """Attach cargo if capacity allows and no current load exists.

        Args:
            cargo: The Cargo instance to hook.
        """

        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        """Remove currently attached cargo."""
        self.current_load = None
