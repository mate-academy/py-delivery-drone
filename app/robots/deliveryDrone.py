from typing import Union, Optional, List
from .flyingRobot import FlyingRobot
from .cargo import Cargo


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: Union[int, float],
            max_load_weight: Union[int, float],
            current_load: Optional[Cargo] = None,
            coords: List[int] = [0, 0, 0],
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

        if current_load is not None:
            self.hook_load(current_load)

    def hook_load(self, cargo: Cargo) -> None:
        if cargo.weight <= self.max_load_weight and self.current_load is None:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
