from app.robot.base.robot import BaseRobot
from app.robot.delivery_drone import DeliveryDrone
from app.robot.flying_robot import FlyingRobot
from app.cargo.base.cargo import Cargo


if __name__ == "__main__":
    base_robot = BaseRobot("mike", 1)
    flying_robot = FlyingRobot("john", 1)
    delivery_drone = DeliveryDrone("jim", 1)
    print(base_robot.get_info())
    print(flying_robot.get_info())
    print(delivery_drone.get_info())
    cargo = Cargo(10)
    delivery_drone.hook_load(cargo)
    print(delivery_drone.get_info())
    delivery_drone.unhook_load()
    print(delivery_drone.get_info())
