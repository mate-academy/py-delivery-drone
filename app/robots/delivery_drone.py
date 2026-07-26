from app.cargo import Cargo
from app.robots.flying_robot import FlyingRobot


class DeliveryDrone(FlyingRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        coords: list[int] | None = None,
        max_load_weight: int = 0,
        current_load: Cargo | None = None,
    ) -> None:
        super().__init__(
            name=name,
            weight=weight,
            coords=coords,
        )

        self.max_load_weight = max_load_weight
        self.current_load = None

        if current_load is not None:
            self.hook_load(current_load)

    def hook_load(self, cargo: Cargo) -> None:
        if (
            self.current_load is None
            and cargo.weight <= self.max_load_weight
        ):
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
