from vehicle import Vehicle


class Truck(Vehicle):
    def __init__(self):
        super().__init__()
        self.carry_limit = None
        self.current_carriage_weight = None

    def has_carriage(self):
        return self.current_carriage_weight is not None

    def attach_carriage(self, weight):
        return weight <= self.carry_limit

    def detach_carriage(self):
        self.current_carriage_weight = None
