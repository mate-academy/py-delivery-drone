class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight

class BaseRobot:
    def __init__(self, name, weight, coords=None):
        self.name = name
        self.weight = weight
        self.coords = coords or [0, 0]

    def go_forward(self, step=1):
        self.coords[1] += step

    def go_back(self, step=1):
        self.coords[1] -= step

    def go_right(self, step=1):
        self.coords[0] += step

    def go_left(self, step=1):
        self.coords[0] -= step

    def get_info(self):
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name, weight, coords=None):
        # Логіка обробки координат для 3D простору
        if coords is None:
            coords_to_pass = [0, 0, 0]
        elif len(coords) == 2:
            coords_to_pass = list(coords) + [0]
        else:
            coords_to_pass = list(coords)
            
        super().__init__(name, weight, coords_to_pass)

    def go_up(self, step=1):
        self.coords[2] += step

    def go_down(self, step=1):
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(self, name, weight, max_load_weight, coords=None, current_load=None):
        super().__init__(name, weight, coords)
        
        self.max_load_weight = max_load_weight
        self.current_load = None
        
        # Спроба завантажити вантаж при ініціалізації
        if current_load is not None:
            self.hook_load(current_load)

    def hook_load(self, cargo)
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo
            return True
        return False

    def unhook_load(self):
        self.current_load = None
