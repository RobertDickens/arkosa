class RoomBase:
    def __init__(self):
        self.powered = False
        self.produced_resource_type = None
        self.produced_resource_quantity = None
        self.ability = None


class InsectProductionRoomOne(RoomBase):
    def __init__(self):
        super().__init__()
        self.produced_resource_type = 'INSECT'
