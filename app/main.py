from typing import List, Optional


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
            self,
            name: str,
            weight: int,
            coords: Optional[List[int]] = None
    ) -> None:
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
    def __init__(
            self,
            name: str,
            weight: int,
            coords: Optional[List[int]] = None
    ) -> None:
        if coords is None:
            coords = [0, 0, 0]
        else:
            if len(coords) == 2:
                coords.append(0)
        super().__init__(name, weight, coords)

    def go_up(self, step: int = 1) -> None:
        if len(self.coords) < 3:
            self.coords.append(0)
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        if len(self.coords) < 3:
            self.coords.append(0)
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: Optional[List[int]] = None,
            max_load_weight: int = 0,
            current_load: Optional["Cargo"] = None
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: "Cargo") -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo
            print(f"Cargo loaded: {cargo.weight}kg")
        else:
            print(f"Cannot load cargo: {cargo.weight}kg")

    def unhook_load(self) -> None:
        if self.current_load is not None:
            print(f"Cargo unloaded: {self.current_load.weight}kg")
            self.current_load = None
        else:
            print("No cargo to unload")
