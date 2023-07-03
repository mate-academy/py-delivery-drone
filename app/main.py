class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, *args, **kwargs) -> None:
        self.name = ""
        self.weight = 0
        self.coords = [0, 0]

        if len(args) != 0:
            for index, values_args in enumerate(args):
                if index == 0:
                    self.name = values_args
                if index == 1:
                    self.weight = values_args
                if index == 2 and values_args is not None:
                    self.coords = values_args

        for key, values in kwargs.items():
            if key == "name":
                self.name = values
            if key == "weight":
                self.weight = values
            if key == "coords":
                if values is None:
                    self.coords = [0, 0]
                else:
                    self.coords = values

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        if len(args) < 3 and "coords" not in kwargs:
            self.coords.append(0)

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if "max_load_weight" not in kwargs:
            self.max_load_weight = 0
        else:
            self.max_load_weight = kwargs["max_load_weight"]
        if "current_load" not in kwargs:
            self.current_load = None
        else:
            self.current_load = kwargs["current_load"]

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None:
            if cargo.weight <= self.max_load_weight:
                self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
