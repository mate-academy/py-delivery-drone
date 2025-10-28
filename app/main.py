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
        self.name = name
        self.weight = weight
        self.coords = coords if coords is not None else [0, 0]

    def go_forward(self, distance: int = 1) -> None:
        self.coords[1] += distance

    def go_back(self, distance: int = 1) -> None:
        self.coords[1] -= distance

    def go_right(self, distance: int = 1) -> None:
        self.coords[0] += distance

    def go_left(self, distance: int = 1) -> None:
        self.coords[0] -= distance

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list[int] | None = None
    ) -> None:
        super().__init__(
            name,
            weight,
            coords=[0, 0, 0] if coords is None else coords
        )

    def go_up(self, distance: int = 1) -> None:
        self.coords[2] += distance

    def go_down(self, distance: int = 1) -> None:
        self.coords[2] -= distance


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            max_load_weight: int,
            coords: list[int] | None = None,
            current_load: Cargo | None = None
    ) -> None:
        super().__init__(
            name,
            weight,
            coords=[0, 0, 0] if coords is None else coords
        )
        self.max_load_weight = max_load_weight
        self.current_load = None
        if current_load is not None:
            self.hook_load(current_load)

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None


"""

cargo = Cargo(20)
cargo2 = Cargo(12)
drone = DeliveryDrone(
        name="Mike",
        weight=12,
        max_load_weight=30,
        current_load=cargo,
    )
drone.hook_load(cargo)
print(cargo)
print(cargo2)
print(drone.current_load is cargo)
print(drone.current_load is cargo2)
"""
