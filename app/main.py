class Cargo:
    def __init__(self, weight):
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords=None):
        self.name = name
        self.weight = weight
        if coords is None:
            self.coords = [0, 0]
        else:
            self.coords = coords

    def go_forward(self, step: int = 1):
        self.coords[1] += step

    def go_back(self, step: int = 1):
        self.coords[1] -= step

    def go_right(self, step: int = 1):
        self.coords[0] += step

    def go_left(self, step: int = 1):
        self.coords[0] -= step

    def get_info(self):
        return (f"Robot: {self.name}, Weight: {self.weight}")


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords=None):
        super().__init__(name, weight, coords)
        if coords is None:
            self.coords = [0, 0, 0]
        else:
            self.coords = coords

    def go_up(self, step=1):
        self.coords[2] += step

    def go_down(self, step=1):
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str, weight: int,
                 max_load_weight, coords=None, current_load=None):
        super().__init__(name, weight, coords)
        if coords is None:
            self.coords = [0, 0, 0]  # [X, Y, Z]
        else:
            self.coords = coords
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, load):
        if self.current_load is None\
                and self.max_load_weight.__gt__(load.weight):
            self.current_load = load

    def unhook_load(self):
        self.current_load = None


cargo = Cargo(14)
drone = DeliveryDrone(name="Jim", weight=18, coords=[11, -4, 16],
                      max_load_weight=20, current_load=None)
drone.hook_load(cargo)
print(drone.current_load)
# is cargo
print(drone.name)
print(drone.coords)
cargo2 = Cargo(2)
drone.hook_load(cargo2)
# drone.current_load is cargo

# didn't hook cargo2, cargo already in current load
# flying_robot = FlyingRobot(name="Mike", weight=11)
# flying_robot.go_up(10)
# print(flying_robot.go_forward())
# print(flying_robot.coords) # = [0, 0, 10]
# flying_robot.go_down(1)
# print(flying_robot.go_left(7))
# print(flying_robot.coords) # = [0, 0, 9]

# robot = BaseRobot(name="Walle", weight=34, coords=[3, -2])
# robot.go_forward()
# print(robot.coords) # == [3, -1]
# robot.go_right(5)
# print(robot.coords) # == [8, -1]
# # print(robot.get_info())
