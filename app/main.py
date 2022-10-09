from __future__ import annotations

if __name__ == "__main__":
    from robot import Cargo, BaseRobot, FlyingRobot, DeliveryDrone
else:
    from .robot import Cargo, BaseRobot, FlyingRobot, DeliveryDrone


# Code test block
if __name__ == "__main__":
    # Test 1
    robot = BaseRobot(name="Walle", weight=34, coords=[3, -2])
    robot.go_forward()
    print(robot.coords == [3, -1])
    robot.go_right(5)
    print(robot.coords == [8, -1])

    # Test 2 (very interesting test)
    robot_1 = BaseRobot("", 1)
    robot_2 = BaseRobot("", 1)
    robot_1.go_forward(1)
    print(robot_2.coords == [0, 0])

    # Test 3
    flying_robot = FlyingRobot(name="Mike", weight=11)
    flying_robot.go_up(10)
    print(flying_robot.coords == [0, 0, 10])

    # Test 4
    cargo = Cargo(14)
    drone = DeliveryDrone(name="Jim", weight=18, coords=[11, -4, 16],
                          max_load_weight=20, current_load=None)
    drone.hook_load(cargo)
    print(drone.current_load is cargo)

    cargo2 = Cargo(2)
    drone.hook_load(cargo2)
    # Didn't hook cargo2, cargo already in current load
    print(drone.current_load is cargo)
