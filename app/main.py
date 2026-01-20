class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight
# **BaseRobot**
#
# - the `__init__` method takes `name`, `weight`, `coords`,
# and saves them
# - `coords` is list with `x` and `y` coordinates, set to [0, 0] by default.
# - `go_forward`, `go_back`, `go_right` and `go_left` methods
# take a `step` argument (1 by default) and move the robot by
# `step` in the appropriate direction.
# Positive Y axis is forward, positive X axis is right.
# These functions should not return anything.
#
# - `get_info` method returns a string in
# the next format `Robot: {name}, Weight: {weight}`
# ```python
# robot = BaseRobot(name="Walle", weight=34, coords=[3, -2])
# robot.go_forward()
# # robot.coords == [3, -1]
# robot.go_right(5)
# # robot.coords == [8, -1]


class BaseRobot:
    def __init__(self, name: str, weight: int,
                 coords: list | None = None) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords.copy() if coords is not None else [0, 0]

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"
# **FlyingRobot**
#
# - inherits from `BaseRobot`
# - takes the same args as BaseRobot and passes them to the
# parent's `__init__` method (use super)
# - can work with z coordinate, coords by default should be [0, 0, 0],
# use condition to send right coords to parent's `__init__` method
# - has methods `go_up` and `go_down` changing `z`, positive Z axis is up
# ```python
# flying_robot = FlyingRobot(name="Mike", weight=11)
# flying_robot.go_up(10)
# # flying_robot.coords = [0, 0, 10]


class FlyingRobot(BaseRobot):

    def __init__(self, name: str, weight: int,
                 coords: list | None = None) -> None:
        initial_coords = coords.copy() if coords is not None else [0, 0, 0]
        super().__init__(name, weight, initial_coords[:3])
        if len(initial_coords) < 3:
            initial_coords.append(0)
        elif len(initial_coords) > 3:
            initial_coords = initial_coords[:3]
        self.coords = initial_coords

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step
# **DeliveryDrone**
#
# - inherits from `FlyingRobot`
# - takes the same args as `FlyingRobot` and passes them
# to the parent's `__init__` method.
# - the `__init__` method also takes and
# stores `max_load_weight` and `current_load`.
#   - `max_load_weight` purpose is to store the robot's load capacity;
#   - `current_load` purpose is to store the
#   `Cargo` instance, which can be None by default.
#   If `Cargo` object was passed to function,
#   use method `hook_load` to check if it can be hooked.
# - has `hook_load` method taking `Cargo` object and saves it to
# `current_load` if two conditions are True:
# `current_load` is set to `None` and `cargo.weight` is
# not greater than `max_load_weight` of the drone. Otherwise, do nothing.
# - has `unhook_load` method, that sets
# `current_load` to None without any additional logic.


class DeliveryDrone(FlyingRobot):

    def __init__(self, name: str, weight: int, max_load_weight: int,
                 coords: list | None = None,
                 current_load: Cargo | None = None) -> None:
        initial_coords = coords.copy() if coords is not None else [0, 0, 0]
        super().__init__(name, weight, initial_coords[:3])
        self.max_load_weight = max_load_weight
        self.current_load = current_load
        self.coords = initial_coords

    def hook_load(self, cargo: Cargo,) -> None:

        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
