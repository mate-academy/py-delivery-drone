from __future__ import annotations


class BaseRobot:
    def __init__(self, name: str, weight: int, coords=None) -> None:
        if coords is None:
            coords = [0, 0]
        self.name = name
        self.weight = weight
        self.coords = coords
    # go_forward, go_back, go_right and go_left methods take a step argument (1 by default)
    # and move the robot by step in the appropriate direction. Positive Y axis is forward, positive X axis is right.
    # These functions should not return anything.
    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step


    # get_info method returns a string in the next format Robot: {name}, Weight: {weight}
    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"

    def __repr__(self) -> str:
        return f"Robot '{self.name}' at Coordinates: [{self.coords[0]}, {self.coords[1]}]"

    def __call__(self) -> str:
        return f"{self.name} at [{self.coords[0]}, {self.coords[1]}]"

class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords=None) -> None:
        if coords is None:
            coords = [0, 0, 0]
        super().__init__(name=name, weight=weight, coords=coords)

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step

class Cargo:
    def __init__(self, weight: int | None = None) -> None:
        self.weight = weight

class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str, weight: int, max_load_weight: int, current_load: Cargo | None, coords=None) -> None:
        super().__init__(name=name, weight=weight, coords=coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo
            if self.current_load:
                print(f"Current load is {self.current_load.weight}.")
        else:
            print(f"Didn't hook cargo with weight {cargo.weight}, cargo with weight {self.current_load.weight} already in current load")

    def unhook_load(self) -> None:
        if self.current_load is not None:
            print(f"Unhooking cargo with weight {self.current_load.weight}.")
            self.current_load = None
        else:
            print("No cargo to unhook.")
