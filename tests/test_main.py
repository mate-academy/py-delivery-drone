import pytest
import ast
import inspect

from app.reference_delievery_drone import BaseRobot, FlyingRobot, DeliveryDrone, Cargo


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


def test_deliver_robot_hook_load_cargo_is_not_heavy():
    cargo = Cargo(20)
    drone = DeliveryDrone("Mike", 12, 30, None)
    drone.hook_load(cargo)
    assert isinstance(drone.current_load, Cargo)


def test_deliver_robot_hook_load_cargo_is_too_heavy():
    cargo = Cargo(50)
    drone = DeliveryDrone("Mike", 12, 30, None)
    drone.hook_load(cargo)
    assert drone.current_load is None


def test_deliver_robot_hook_load_cargo_current_load_isnt_none():
    cargo = Cargo(20)
    cargo2 = Cargo(12)
    drone = DeliveryDrone("Mike", 12, 30, cargo2)
    drone.hook_load(cargo)
    assert drone.current_load is cargo2


def test_deliver_robot_unhook_load():
    drone = DeliveryDrone("Mike", 12, 30, Cargo(12))
    drone.unhook_load()
    assert drone.current_load is None


@pytest.mark.parametrize(
    "class_,parent",
    [
        (FlyingRobot, "BaseRobot"),
        (DeliveryDrone, "FlyingRobot"),
    ],
)
def test_inheritance_of_flying_and_delivery(
    class_, parent
):
    class_source = inspect.getsource(class_)
    parsed_class = ast.parse(class_source)
    assert [name.id for name in parsed_class.body[0].bases] == [
        parent
    ], f"'{class_.__name__}' should be inherited from {parent.__name__}'"


@pytest.mark.parametrize(
    "class_,methods,length",
    [
        (FlyingRobot, ["__init__", "go_up", "go_down"], 3),
        (DeliveryDrone, ["__init__", "hook_load", "unhook_load"], 3)
    ]
)
def test_methods_declared_in_inherited_classes(class_, methods, length):
    class_source = inspect.getsource(class_)
    parsed_class = ast.parse(class_source)
    assert (
            len(parsed_class.body[0].body) == length
    ), f"Only {length} methods should be defined inside class '{class_.__name__}'"
    assert (
            [parsed_class.body[0].body[it].name for it in range(length)] == methods
    ), f"Only {methods} should be defined inside class '{class_.__name__}'"
