class BaseRobot:
    def __init__(self,
                 name: str,
                 weight: float,
                 coords = None) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords or [0,0]
    
    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"
    
    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step
    
    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step



class FlyingRobot(BaseRobot):
    def __init__(self,
                 name: str,
                 weight: float,
                 coords: list = None,
                ) -> None:
        super().__init__(name, weight, coords or [0,0,0])
        
    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step
    
    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step

class DeliveryDrone(FlyingRobot):
    def __init__(self,
                 name: str,
                 weight: float,
                 coords: list = None,
                 max_load_weight: int = 20,
                 current_load: Cargo | None = None) -> None:
        super().__init__(name, weight, coords or [0,0,0])
        self.max_load_weight = max_load_weight
        self.current_load = current_load
    
    def hook_load(self, cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo
        
    def unhook_load(self):
        self.current_load = None

class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight