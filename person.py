class PersonBase:
    def __init__(self):
        self.produced_resource_type = None
        self.produced_resource_quantity = None
        self.can_explore = None

    def produce_resource(self):
        pass

    def explore(self):
        pass