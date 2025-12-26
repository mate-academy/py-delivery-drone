class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        if coords is None:
            coords = [0, 0]
        self.name = name
        self.weight = weight
        self.coords = coords

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
        elif len(coords) == 2:
            coords.append(0)
        super().__init__(name, weight, coords)

    def go_up(self, zet: int = 1) -> None:
        self.coords[2] += zet

    def go_down(self, zet: int = 1) -> None:
        self.coords[2] -= zet


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str, weight: int, coords: list = None,
                 max_load_weight: int = 0, current_load: int = None) -> None:
        super(). __init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo = None) -> None:
        if (cargo is not None and self.current_load is None
                and cargo.weight <= self.max_load_weight):
            self.current_load = cargo
        else:
            print("Груз не может быть загружен")
            if cargo is None:
                print("Нет груза")
            elif self.current_load is not None:
                print("Уже есть загруженный груз")
            elif cargo.weight > self.max_load_weight:
                print("Груз слишком тяжёлый")

    def unhook_load(self) -> None:
        self.current_load = None
