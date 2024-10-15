class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords if coords is not None else [0, 0]

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
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        if coords is None:
            coords = [0, 0, 0]
        super().__init__(name, weight, coords)

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str, weight: int,
                 max_load_weight: int, current_load: Cargo = None,
                 coords: list = None) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        current_load_weight = \
            (self.current_load.weight) if self.current_load else 0
        available_capacity = self.max_load_weight - current_load_weight

        if cargo.weight <= available_capacity:
            if self.current_load:
                self.current_load.weight += cargo.weight
            else:
                self.current_load = cargo
            print(f"Hooked load of weight {cargo.weight}"
                  f". Current load: {self.current_load.weight}")
        else:
            print("Cannot hook load. Exceeds max load weight.")

    def unhook_load(self) -> None:
        self.current_load = None
        print("Load unhooked. Current load is now None.")
