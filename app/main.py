class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list[int] = None
    ) -> None:
        self.name = name
        self.weight = weight
        if coords is None:
            self.coords = [0, 0]
        else:
            self.coords = coords

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step
        print(f"robot.coords == {self.coords}")

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step
        print(f"robot.coords == {self.coords}")

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step
        print(f"robot.coords == {self.coords}")

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step
        print(f"robot.coords == {self.coords}")

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list[int] = None
    ) -> None:
        super().__init__(name, weight, coords)
        if coords is None:
            self.coords = [0, 0, 0]

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step
        print(f"robot.coords == {self.coords}")

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step
        print(f"robot.coords == {self.coords}")


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            max_load_weight: int,
            current_load: Cargo = None,
            coords: list[int] = None
    ) -> None:
        super().__init__(name=name, weight=weight, coords=coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo
            print(f"{self.name}.current_load is {cargo}")

        if self.current_load is not None:
            print(f"didn't hook {cargo},"
                  f" {self.current_load} already in current load")

    def unhook_load(self) -> None:
        self.current_load = None
        print(f"{self.name}.current_load is {self.current_load}")


cargo = Cargo(14)
drone = DeliveryDrone(
    name="Jim",
    weight=18,
    coords=[11, -4, 16],
    max_load_weight=20,
    current_load=None,
)
drone.hook_load(cargo)
# drone.current_load is cargo

cargo2 = Cargo(2)
drone.hook_load(cargo2)
# drone.current_load is cargo
# didn't hook cargo2, cargo already in current load

drone = DeliveryDrone(
    name="Jack",
    weight=9,
    max_load_weight=30,
    current_load=Cargo(20),
)
drone.unhook_load()
# drone.current_load is None
