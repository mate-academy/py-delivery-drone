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
        self.coords = coords or [0, 0]

    def go_forward(self, step: int = 1) -> None:
        if step > 0:
            self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        if step > 0:
            self.coords[1] -= step

    def go_right(self, step: int = 1) -> None:
        if step > 0:
            self.coords[0] += step

    def go_left(self, step: int = 1) -> None:
        if step > 0:
            self.coords[0] -= step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        coords: list[int] | None = None
    ) -> None:
        # Якщо coords не передано — використати [0,0,0]
        if coords is None:
            normalized_coords = [0, 0, 0]
        else:
            # Якщо передано лише x і y — додати z = 0
            if len(coords) == 2:
                normalized_coords = [coords[0], coords[1], 0]
            else:
                # Припускаємо, що список вже має 3 елементи (або більше)
                # Можна взяти лише перші три, щоб бути безпечним
                normalized_coords = coords[:3]
        # Тепер передаємо нормалізовані coords у батьківський конструктор
        super().__init__(name, weight, normalized_coords)

    def go_up(self, step: int = 1) -> None:
        if step > 0:
            self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        if step > 0:
            self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        coords: list[int] | None = None,
        max_load_weight: int = 0,
        current_load: Cargo | None = None
    ) -> None:

        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = None
        if current_load is not None:
            self.hook_load(current_load)

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
