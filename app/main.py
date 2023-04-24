class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self,
                 name,
                 weight,
                 coords=None):
        self.name = name
        self.weight = weight

        self.coords = [0, 0] if coords is None else coords  # [x, y]

        print(f"{self.coords} when init")

    def go_forward(self, step=1):  # [x, +y]
        self.coords[1] += step

    def go_back(self, step=1):  # [x, -y]
        self.coords[1] -= step

    def go_right(self, step=1):  # [+x, y]
        self.coords[0] += step

    def go_left(self, step=1):  # [-x, y]
        self.coords[0] -= step

    def get_info(self):
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name, weight, coords=None):
        super().__init__(name, weight, coords=None)
        self.coords = [0, 0, 0] if coords is None else coords  # [x, y, z]

    def go_up(self, step=1):
        self.coords[2] += step  # [x,y,+z]

    def go_down(self, step=1):
        self.coords[2] -= step  # [x,y,-z]


class DeliveryDrone(FlyingRobot):
    def __init__(self, name, weight, coords=None, max_load_weight=None,
                 current_load=None):
        super().__init__(name, weight, coords=None)
        self.coords = [0, 0, 0] if coords is None else coords  # [x, y, z]
        self.current_load = current_load
        self.max_load_weight = max_load_weight

    def hook_load(self, cargo_obj):
        if self.current_load is None:
            #print(f"self current load is {self.current_load}")
            if cargo_obj.weight <= self.max_load_weight:
                #print(f"cargo_obj.weight is {cargo_obj.weight} <= self.max_load_weight is {self.max_load_weight} ")
                self.current_load = cargo_obj.weight
                #print(f"so self.current_load ({self.current_load}) = cargo_obj.weight ({self.current_load})")

    def unhook_load(self):
        #print(f"was {self.current_load}")
        self.current_load = None
        #print(f"and now is {self.current_load}")
