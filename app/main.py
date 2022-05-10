class Cargo:
    def __init__(self, weight):
        self.weight = weight


# write your code here
class BaseRobot():
    def __init__(self, name: str, weight: int, coords: list = None):
        self.name = name
        self.weight = weight
        if coords:
            self.coords = coords
        else:
            self.coords = [0, 0]

    def go_forward(self, step=1):
        self.coords[1] += step

    def go_back(self, step=1):
        self.coords[1] -= step

    def go_left(self, step=1):
        self.coords[0] -= step

    def go_right(self, step=1):
        self.coords[0] += step

    def get_info(self):
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):

    def __init__(self, name: str, weight: int, coords: list = None):
        super().__init__(name, weight)
        if coords:
            self.coords = coords
        else:
            self.coords = [0, 0, 0]

    def go_up(self, step=1):
        self.coords[2] += step

    def go_down(self, step=1):
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):

    def __init__(self, name: str, weight: int,
                 max_weight_load, current_load, coords: list = None):
        super().__init__(name, weight, coords)
        self.max_weight_load = max_weight_load
        self.current_load = current_load

    def hook_load(self, obj):
        if self.current_load is None and obj.weight <= self.max_weight_load:
            self.current_load = obj

    def unhook_load(self):
        self.current_load = None


if __name__ == "__main__":
    cargo = Cargo(14)
    drone = DeliveryDrone(name="Jim", weight=18, coords=[11, -4, 16],
                          max_weight_load=20, current_load=None)
    drone.hook_load(cargo)
    print(drone.current_load is cargo)

    cargo2 = Cargo(2)
    drone.hook_load(cargo2)
    print(drone.current_load is cargo)

    drone = DeliveryDrone(name="Jack",
                          weight=9,
                          max_weight_load=30,
                          current_load=Cargo(20))
    drone.unhook_load()
    print(drone.current_load is None)
