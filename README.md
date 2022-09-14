# Delivery drone

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start

Let's implement 3 classes with inheritance

**BaseRobot**

- constructor takes `name`, `weight`, `coords`, 
and saves them
- `coords` is list with `x` and `y` coordinates, set to [0, 0] by default.
It is not a good practice to use mutable object as a default parameter,
set it to `None` by default, and use condition.
- `go_forward`, `go_back`, `go_right` and `go_left` methods 
take a `step` argument (1 by default) and move the robot by
`step` in the appropriate direction.
Positive Y axis is forward, positive X axis is right.
- `get_info` method returns a string in the next format `Robot: {name}, Weight: {weight}`
```python
robot = BaseRobot(name="Walle", weight=34, coords=[3, -2])
robot.go_forward()
robot.coords == [3, -1]
robot.go_right(5)
robot.coords == [8, -1]
```

**FlyingRobot**

- inherits from `BaseRobot`
- takes the same args as BaseRobot and passes them to the 
parent's constructor (use super)
- can work with z coordinate, coords by default should be [0, 0, 0], 
use condition to send right coords to parent's constructor
- has methods `go_up` and `go_down` changing `z`, positive Z axis is up
```python
flying_robot = FlyingRobot(name="Mike", weight=11)
flying_robot.go_up(10)
flying_robot.coords = [0, 0, 10]
```

**DeliveryDrone**

- inherits from `FlyingRobot`
- takes the same args as `FlyingRobot` and passes them 
to the parent's constructor. 
- constructor also takes and stores `max_load_weight` and `current_load`.
- has `hook_load` method taking `Cargo` object and saves it to
`current_load` if `current_load` is `None` and `cargo.weight` not greater than
`max_load_weight` of the drone
- has `unhook_load` method, that set `current_load` to None
```python
cargo = Cargo(14)
drone = DeliveryDrone(name="Jim", weight=18, coords=[11, -4, 16], 
                      max_load_weight=20, current_load=None)
drone.hook_load(cargo)
drone.current_load is cargo

cargo2 = Cargo(2)
drone.hook_load(cargo2)
drone.current_load is cargo  
# didn't hook cargo2, cargo already in current load
```
```python
drone = DeliveryDrone(name="Jack", 
                      weight=9, 
                      max_weight_load=30, 
                      current_load=Cargo(20))
drone.unhook_load()
drone.current_load is None
```
