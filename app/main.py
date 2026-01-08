from app.robot.base.robot import BaseRobot
from app.robot.delivery_drone import DeliveryDrone
from app.robot.flying_robot import FlyingRobot
from app.cargo.base.cargo import Cargo


if __name__ == "__main__":
    robot_1 = BaseRobot("mike", 1)
    robot_2 = BaseRobot("john", 1)
    robot_1.go_forward(1)
    robot_2.go_forward(3)
    robot_2.go_forward(3)
    print(robot_1.coords)
    print(robot_2.coords)
