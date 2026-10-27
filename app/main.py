class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
            self,
            name: str,
            weight: float,
            coords: list | None = None
    ) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords or [0, 0]

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


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: float,
            coords: list | None = None
    ) -> None:
        # Use condition to determine the right default 3D coordinates
        actual_coords = coords if coords is not None else [0, 0, 0]
        super().__init__(
            name=name,
            weight=weight,
            coords=actual_coords
        )

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(
        self,
        name: str,
        weight: float,
        max_load_weight: int,
        coords: list | None = None,
        current_load: Cargo | None = None,
    ) -> None:
        super().__init__(name=name, weight=weight, coords=coords)
        self.max_load_weight = max_load_weight

        # Save the cargo instance using the hook_load method rule
        self.current_load = None
        if current_load is not None:
            self.hook_load(current_load)

    def hook_load(self, cargo: Cargo) -> None:
        # Check conditions: 1) drone is empty AND 2) cargo isn't too heavy
        if (
            self.current_load is None
            and cargo.weight <= self.max_load_weight
        ):
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None


# README.md 21-25
robot = BaseRobot(name="Walle", weight=34, coords=[3, -2])
robot.go_forward()
print(robot.coords)  # robot.coords == [3, -1]
robot.go_right(5)
print(robot.coords)  # robot.coords == [8, -1]


# README.md 37-39
flying_robot = FlyingRobot(name="Mike", weight=11)
flying_robot.go_up(10)
print(flying_robot.coords)  # flying_robot.coords = [0, 0, 10]


# README.md 56-70
cargo = Cargo(14)
drone = DeliveryDrone(
    name="Jim",
    weight=18,
    coords=[11, -4, 16],
    max_load_weight=20,
    current_load=None,
)
drone.hook_load(cargo)
print(drone.current_load is cargo)  # drone.current_load is cargo

cargo2 = Cargo(2)
drone.hook_load(cargo2)
print(drone.current_load is cargo)  # drone.current_load is cargo
# didn't hook cargo2, cargo already in current load

# README.md 73-80
drone = DeliveryDrone(
    name="Jack",
    weight=9,
    max_load_weight=30,
    current_load=Cargo(20),
)
drone.unhook_load()
print(drone.current_load is None)  # drone.current_load is None
