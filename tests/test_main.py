import pytest
import ast
import inspect
import typing
from typing import Callable

from app.main import BaseRobot, FlyingRobot, DeliveryDrone, Cargo


@pytest.mark.parametrize(
    "args,result",
    [
        (("John", 50), ("John", 50, [0, 0])),
        (("Michael", 30, [10, 1]), ("Michael", 30, [10, 1]))
    ]
)
def test_base_robot_has_attrs(args, result):
    robot = BaseRobot(*args)
    assert all([hasattr(robot, attr) for attr in ["name", "weight", "coords"]])
    assert (robot.name, robot.weight, robot.coords) == result


def test_base_robot_go():
    robot = BaseRobot("Michael", 40)
    robot.go_forward(4)
    assert robot.coords == [0, 4]
    robot.go_forward()
    assert robot.coords == [0, 5]
    robot.go_back(5)
    assert robot.coords == [0, 0]
    robot.go_back()
    assert robot.coords == [0, -1]
    robot.go_right(3)
    assert robot.coords == [3, -1]
    robot.go_right()
    assert robot.coords == [4, -1]
    robot.go_left(7)
    assert robot.coords == [-3, -1]
    robot.go_left()
    assert robot.coords == [-4, -1]


def test_base_robot_do_not_use_mutable_as_default():
    robot_1 = BaseRobot("", 1)
    robot_2 = BaseRobot("", 1)
    robot_1.go_forward(1)
    assert robot_2.coords == [0, 0]


def test_base_robot_get_info_method():
    robot = BaseRobot("Michael", 40)
    assert robot.get_info() == "Robot: Michael, Weight: 40"


def test_flying_robot_go():
    robot = FlyingRobot("Michael", 40)
    robot.go_forward(4)
    assert robot.coords == [0, 4, 0]
    robot.go_forward()
    assert robot.coords == [0, 5, 0]
    robot.go_back(5)
    assert robot.coords == [0, 0, 0]
    robot.go_back()
    assert robot.coords == [0, -1, 0]
    robot.go_right(3)
    assert robot.coords == [3, -1, 0]
    robot.go_right()
    assert robot.coords == [4, -1, 0]
    robot.go_left(7)
    assert robot.coords == [-3, -1, 0]
    robot.go_left()
    assert robot.coords == [-4, -1, 0]
    robot.go_up(3)
    assert robot.coords == [-4, -1, 3]
    robot.go_up()
    assert robot.coords == [-4, -1, 4]
    robot.go_down(4)
    assert robot.coords == [-4, -1, 0]
    robot.go_down()
    assert robot.coords == [-4, -1, -1]


@pytest.mark.parametrize(
    "args,result",
    [
        (("John", 50), ("John", 50, [0, 0, 0])),
        (("Michael", 30, [10, 1, 100]), ("Michael", 30, [10, 1, 100]))
    ]
)
def test_flying_robot_has_attrs(args, result):
    robot = FlyingRobot(*args)
    assert all([hasattr(robot, attr) for attr in ["name", "weight", "coords"]])
    assert (robot.name, robot.weight, robot.coords) == result


def test_flying_robot_do_not_use_mutable_as_default():
    robot_1 = FlyingRobot("", 1)
    robot_2 = FlyingRobot("", 1)
    robot_1.go_up(1)
    assert robot_2.coords == [0, 0, 0]


@pytest.mark.parametrize(
    "kwargs,result",
    [
        (
