from app.drone.flying_robot import FlyingRobot
from app.drone.cargo import Cargo

class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            max_load_weight: int,
            current_load: Cargo | None = None,
            coords: list[int] | None = None
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = None
        self.hook_load(current_load)

    def hook_load(self, other: Cargo) -> None:
        if self.current_load is None:
            if self.max_load_weight >= other.weight:
                self.current_load = other
        return

    def unhook_load(self) -> None:
        self.current_load = None