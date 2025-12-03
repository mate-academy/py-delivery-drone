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
        self.name: str = name
        self.weight: int = weight
        self.coords: List[int] = coords if coords is not None else [0, 0]

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
            coords_to_use = [0, 0, 0]

        else:
            # garantir número correto de coordenadas
            if len(coords) == 2:
                coords_to_use = [coords[0], coords[1], 0]  # adiciona Z padrão

            elif len(coords) == 3:
                coords_to_use = coords.copy()  # usa 3D normalmente

            else:
                raise ValueError("coords must have length 2 or 3")

        super().__init__(name, weight, coords_to_use)

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        coords: Optional[List[int]] = None,
        max_load_weight: int = 0,
        current_load: Optional[Cargo] = None,
    ) -> None:
        super().__init__(name, weight, coords)

        self.max_load_weight: int = max_load_weight
        self.current_load: Optional[Cargo] = None

        if current_load is not None:
            self.hook_load(current_load)

    def hook_load(self, cargo: Cargo) -> None:
        if (
            self.current_load is None
            and cargo.weight <= self.max_load_weight
        ):
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
