from resource_types import ResourceType


class RoomBase:
    def __init__(self):
        self.powered = False
        self.produced_resource_type = None
        self.produced_resource_quantity = None
        self.ability = None
        self.price = None
        self.stage = 1


# Default rooms
class InsectProductionRoomOne(RoomBase):
    def __init__(self):
        super().__init__()
        self.produced_resource_type = ResourceType.INSECT


class NitrogenProductionRoomOne(RoomBase):
    def __init__(self):
        super().__init__()
        self.produced_resource_type = ResourceType.NITROGREN
        self.produced_resource_quantity = 1


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


class NitrogrenRoomTwo(RoomBase):
    def __init__(self):
        super().__init__()
        self.price = '1 bolt'
        self.produced_resource_type = ResourceType.NITROGREN
        self.produced_resource_quantity = 2


class InsectRoomTwo(RoomBase):
    def __init__(self):
        super().__init__()
        self.price = '1 bolt'
        self.produced_resource_type = ResourceType.INSECT
        self.produced_resource_quantity = 2


class BoltRoomOne(RoomBase):
    def __init__(self):
        super().__init__()
        self.price = '1 bolt'
        self.produced_resource_type = ResourceType.BOLT
        self.produced_resource_quantity = 1


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
        self.price = '2 bolt 1 nut'
        self.produced_resource_type = (ResourceType.BOLT,
                                       ResourceType.NUT)
        self.produced_resource_quantity = (1,
                                           1)


class PowerCoreRoom(RoomBase):
    def __init__(self):
        super().__init__()
        self.price = '3 bolt 1 nut'
        self.produced_resource_type = ResourceType.POWER_CORE
        self.produced_resource_quantity = 1


class NitrogenRoomThree(RoomBase):
    def __init__(self):
        super().__init__()
        self.price = '2 bolt 1 nut'
        self.produced_resource_type = ResourceType.NITROGREN
        self.produced_resource_quantity = 3


class MoraleRoomTwo(RoomBase):
    def __init__(self):
        super().__init__()
        self.ability = 'increase morale 2'


class DefenceRoomOne(RoomBase):
    def __init__(self):
        super().__init__()
        self.price = '1 bolt'
        self.ability = 'one defence'


class InsectRoomThree(RoomBase):
    def __init__(self):
        super().__init__()
        self.price = ' 2 bolt 1 nut'
        self.produced_resource_type = ResourceType.INSECT
        self.produced_resource_quantity = 3


# Stage 3 Rooms
class InsectRoomFour(RoomBase):
    def __init__(self):
        super().__init__()
        self.price = ' 3 bolt 2 nut'
        self.produced_resource_type = ResourceType.INSECT
        self.produced_resource_quantity = 4


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


class NitrogenRoomFour(RoomBase):
    def __init__(self):
        super().__init__()
        self.price = '3 bolt 2 nut'
        self.produced_resource_type = ResourceType.NITROGREN
        self.produced_resource_quantity = 4


class MoraleRoomThree(RoomBase):
    def __init__(self):
        super().__init__()
        self.ability = 'increase morale 3'
