from resource_types import ResourceType


class RoomBase:
    def __init__(self):
        self.powered = False
        self.ability = None
        self.price = None
        self.stage = 1
        self.resource_production = False


class ResourceRoomBase:
    def __init__(self):
        self.powered = False
        self.stage = 1
        self.room_type = 'resource production'


class MedicalRoomBase:
    def __init__(self):
        self.powered = False
        self.stage = 1
        self.room_type = 'medical'


class DefenceBase:
    def __init__(self):
        self.powered = False
        self.stage = 1
        self.room_type = 'defence'


class PointRoomBase:
    def __init__(self):
        self.powered = False
        self.stage = 1
        self.room_type = 'points'


# Default rooms
class InsectRoomOne(RoomBase):
    def __init__(self):
        super().__init__()
        self.resource_production = True
        self.produced_resources = {ResourceType.INSECT: 1}

    def round_end_production(self):
        return self.produced_resources


class NitrogrenRoomOne(RoomBase):
    def __init__(self):
        super().__init__()
        self.resource_production = True
        self.produced_resources = {ResourceType.NITROGREN: 1}


class MedicalRoomOne(RoomBase):
    def __init__(self):
        super().__init__()
        self.ability = None


# Stage 1 Rooms
class MoralRoomOne(RoomBase):
    def __init__(self):
        super().__init__()


class DefenceRoomOneFree(RoomBase):
    def __init__(self):
        super().__init__()
        self.defense = True


class NitrogrenRoomTwo(RoomBase):
    def __init__(self):
        super().__init__()
        self.resource_production = True
        self.price = '1 bolt'
        self.produced_resources = {ResourceType.NITROGREN: 1}


class InsectRoomTwo(RoomBase):
    def __init__(self):
        super().__init__()
        self.resource_production = True
        self.price = '1 bolt'
        self.produced_resources = {ResourceType.INSECT: 1}


class BoltRoomOne(RoomBase):
    def __init__(self):
        super().__init__()
        self.resource_production = True
        self.price = '1 bolt'
        self.produced_resources = {ResourceType.BOLT: 1}


# Stage 2 Rooms
class MedicalRoomTwo(RoomBase):
    def __init__(self):
        super().__init__()
        self.price = '2 bolt 1 nut'
        self.ability = 'heal 2'


class PointRoomOne(RoomBase):
    def __init__(self):
        super().__init__()
        self.price = '3 bolt 1 nut'
        self.ability = 'plus one point'


class NutAndBoltRoom(RoomBase):
    def __init__(self):
        super().__init__()
        self.resource_production = True
        self.price = '2 bolt 1 nut'
        self.produced_resources = {ResourceType.BOLT: 1,
                                   ResourceType.NUT: 1}


class PowerCoreRoom(RoomBase):
    def __init__(self):
        super().__init__()
        self.resource_production = True
        self.price = '3 bolt 1 nut'
        self.produced_resources = {ResourceType.POWER_CORE: 1}


class NitrogenRoomThree(RoomBase):
    def __init__(self):
        super().__init__()
        self.resource_production = True
        self.price = '2 bolt 1 nut'
        self.produced_resources = {ResourceType.NITROGREN: 3}


class MoraleRoomTwo(RoomBase):
    def __init__(self):
        super().__init__()
        self.ability = 'increase morale 2'


class DefenceRoomOne(RoomBase):
    def __init__(self):
        super().__init__()
        self.price = '1 bolt'
        self.ability = 'one defence'
        self.defense = True


class InsectRoomThree(RoomBase):
    def __init__(self):
        super().__init__()
        self.resource_production = True
        self.price = ' 2 bolt 1 nut'
        self.produced_resources = {ResourceType.INSECT: 3}


# Stage 3 Rooms
class InsectRoomFour(RoomBase):
    def __init__(self):
        super().__init__()
        self.resource_production = True
        self.price = ' 3 bolt 2 nut'
        self.produced_resources = {ResourceType.INSECT: 4}


class PointRoomTwo(RoomBase):
    def __init__(self):
        super().__init__()
        self.price = '3 bolt 1 nut'
        self.ability = 'gain two reputation points'


class DefenceRoomTwo(RoomBase):
    def __init__(self):
        super().__init__()
        self.price = '2 bolt 1 nut'
        self.ability = 'two defence'
        self.defense = True


class NitrogenRoomFour(RoomBase):
    def __init__(self):
        super().__init__()
        self.resource_production = True
        self.price = '3 bolt 2 nut'
        self.produced_resources = {ResourceType.NITROGREN: 4}


class MoraleRoomThree(RoomBase):
    def __init__(self):
        super().__init__()
        self.ability = 'increase morale 3'
