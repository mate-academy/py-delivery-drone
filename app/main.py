from typing import Optional


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


# Tworzenie klasy podstawowy robot z name weight coord = [0,,0]
class BaseRobot:

    def __init__(
            self,
            name: str,
            weight: int,
            coords: list[int] | None = None
    ) -> None:
        if coords is None:
            self.coords = [0, 0]
        else:
            self.coords = coords
        self.name = name
        self.weight = weight

# poruszanie sie do przodu
    def go_forward(self, step: int = 1) -> None:

        self.coords[1] += step

# poruszanie sie do tylu
    def go_back(self, step: int = 1) -> None:

        self.coords[1] -= step

# poruszanie sie w prawo
    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step

# poruszanei sie w lewo
    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step

# wyswietla info o robocie

    def get_info(self) -> str:

        return (f"Robot: {self.name}, Weight: {self.weight}")


# Tworzenie klasy FlyingRobot dziedziczenie po BaseRobot
class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list[int] | None = None
    ) -> None:
        if coords is None:
            coords = [0, 0, 0]
        elif len(coords) == 2:
            coords = coords + [0]
        else:
            coords = coords[:3]

        super().__init__(name, weight, coords[:2])
        self.coords = coords
# latanie w gore

    def go_up(self, step: int = 1) -> None:

        self.coords[2] += step
# latanie w dol

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step

# Tworznie klasy dostaraczanie ladunku


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list[int] | None = None,
            max_load_weight: int = 0,
            current_load: Optional["Cargo"] = None
    ) -> None:

        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = None
        if current_load is not None:
            self.hook_load(current_load)
# zaladunek

    def hook_load(self, cargo: "Cargo") -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo
# rozladunek

    def unhook_load(self,) -> None:
        self.current_load = None
