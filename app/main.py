from __future__ import annotations


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
        self,
        name: str,
        weight: int,
        coords: list[int] | None = None,
    ) -> None:
        coords = coords or [0, 0]
        self.name = name
        self.weight = weight
        self.pos_x, self.pos_y = coords
        # initialize once; mutate in place later
        self.coords = [self.pos_x, self.pos_y]

    def _sync(self) -> None:
        # mutate existing list in place
        self.coords[0] = self.pos_x
        self.coords[1] = self.pos_y
        if hasattr(self, "pos_z"):
            if len(self.coords) == 2:
                # extend once if 3D
                self.coords.append(self.pos_z)  # type: ignore[attr-defined]
            else:
                self.coords[2] = self.pos_z  # type: ignore[attr-defined]

    def go_forward(self, dist: int = 1) -> None:
        self.pos_y += dist
        self._sync()

    def go_back(self, dist: int = 1) -> None:
        self.pos_y -= dist
        self._sync()

    def go_right(self, dist: int = 1) -> None:
        self.pos_x += dist
        self._sync()

    def go_left(self, dist: int = 1) -> None:
        self.pos_x -= dist
        self._sync()

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        coords: list[int] | None = None,
    ) -> None:
        # Accept None / [x, y] / [x, y, z]; treat 2D as z=0
        if coords is None:
            start_x, start_y, start_z = 0, 0, 0
        elif len(coords) == 3:
            start_x, start_y, start_z = coords
        elif len(coords) == 2:
            start_x, start_y = coords
            start_z = 0
        else:
            raise ValueError("coords must be length 2 or 3")

        super().__init__(name, weight, [start_x, start_y])
        self.pos_z = start_z
        # ensure coords is 3D, mutate in place
        if len(self.coords) == 2:
            self.coords.append(self.pos_z)
        else:
            self.coords[2] = self.pos_z

    def go_up(self, dist: int = 1) -> None:
        self.pos_z += dist
        self._sync()

    def go_down(self, dist: int = 1) -> None:
        self.pos_z -= dist
        self._sync()


class DeliveryDrone(FlyingRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        max_load_weight: int,
        current_load: Cargo | None = None,
        coords: list[int] | None = None,
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        # must not bypass capacity checks
        self.current_load: Cargo | None = None
        if current_load is not None:
            self.hook_load(current_load)

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
