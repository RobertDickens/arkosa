from resource_types import ResourceType
from room_types import RoomType


class ResourceRoomBase:
    def __init__(self):
        self.powered = False
        self.stage = 1
        self.room_type = RoomType.RESOURCE_PRODUCTION


class MedicalRoomBase:
    def __init__(self):
        self.powered = False
        self.stage = 1
        self.room_type = RoomType.MEDICAL


class DefenceBase:
    def __init__(self):
        self.powered = False
        self.stage = 1
        self.room_type = RoomType.DEFENCE


class ReputationRoomBase:
    def __init__(self):
        self.powered = False
        self.stage = 1
        self.room_type = RoomType.REPUTATION
        

class MoralRoomBase:
    def __init__(self):
        self.powered = False
        self.stage = 1
        self.room_type = RoomType.MORALE


# Default rooms
class InsectRoomOne(ResourceRoomBase):
    def __init__(self):
        super().__init__()
        self.produced_resources = {ResourceType.INSECT: 1}

    def round_end_production(self):
        return self.produced_resources


class NitrogrenRoomOne(ResourceRoomBase):
    def __init__(self):
        super().__init__()
        self.produced_resources = {ResourceType.NITROGREN: 1}


class MedicalRoomOne(MedicalRoomBase):
    def __init__(self):
        super().__init__()
        self.ability = None


# Stage 1 Rooms
class MoralRoomOne(MoralRoomBase):
    def __init__(self):
        super().__init__()


class DefenceRoomOneFree(DefenceBase):
    def __init__(self):
        super().__init__()


class NitrogrenRoomTwo(ResourceRoomBase):
    def __init__(self):
        super().__init__()
        self.price = {ResourceType.BOLT: 1}
        self.produced_resources = {ResourceType.NITROGREN: 1}


class InsectRoomTwo(ResourceRoomBase):
    def __init__(self):
        super().__init__()
        self.price = {ResourceType.BOLT: 1}
        self.produced_resources = {ResourceType.INSECT: 1}


class BoltRoomOne(ResourceRoomBase):
    def __init__(self):
        super().__init__()
        self.price = {ResourceType.BOLT: 1}
        self.produced_resources = {ResourceType.BOLT: 1}


# Stage 2 Rooms
class MedicalRoomTwo(MedicalRoomBase):
    def __init__(self):
        super().__init__()
        self.stage = 2
        self.price = {ResourceType.BOLT: 2,
                      ResourceType.NUT: 1}
        self.ability = 'heal 2'


class ReputationRoomOne(ReputationRoomBase):
    def __init__(self):
        super().__init__()
        self.stage = 2
        self.price = {ResourceType.BOLT: 3,
                      ResourceType.NUT: 1}
        self.ability = 'plus one Reputation'


class NutAndBoltRoom(ResourceRoomBase):
    def __init__(self):
        super().__init__()
        self.stage = 2
        self.price = {ResourceType.BOLT: 2,
                      ResourceType.NUT: 1}
        self.produced_resources = {ResourceType.BOLT: 1,
                                   ResourceType.NUT: 1}


class PowerCoreRoom(ResourceRoomBase):
    def __init__(self):
        super().__init__()
        self.stage = 2
        self.price = {ResourceType.BOLT: 3,
                      ResourceType.NUT: 1}
        self.produced_resources = {ResourceType.POWER_CORE: 1}


class NitrogenRoomThree(ResourceRoomBase):
    def __init__(self):
        super().__init__()
        self.stage = 2
        self.price = {ResourceType.BOLT: 2,
                      ResourceType.NUT: 1}
        self.produced_resources = {ResourceType.NITROGREN: 3}


class MoraleRoomTwo(MoralRoomBase):
    def __init__(self):
        super().__init__()
        self.stage = 2
        self.ability = 'increase morale 2'


class DefenceRoomOne(DefenceBase):
    def __init__(self):
        super().__init__()
        self.stage = 2
        self.price = {ResourceType.BOLT: 1}
        self.ability = 'one defence'


class InsectRoomThree(ResourceRoomBase):
    def __init__(self):
        super().__init__()
        self.stage = 2
        self.price = {ResourceType.BOLT: 2,
                      ResourceType.NUT: 1}
        self.produced_resources = {ResourceType.INSECT: 3}


# Stage 3 Rooms
class InsectRoomFour(ResourceRoomBase):
    def __init__(self):
        super().__init__()
        self.stage = 3
        self.price = {ResourceType.BOLT: 3,
                      ResourceType.NUT: 1}
        self.produced_resources = {ResourceType.INSECT: 4}


class ReputationRoomTwo(ReputationRoomBase):
    def __init__(self):
        super().__init__()
        self.stage = 3
        self.price = {ResourceType.BOLT: 3,
                      ResourceType.NUT: 1}
        self.ability = 'gain two reputation Reputations'


class DefenceRoomTwo(DefenceBase):
    def __init__(self):
        super().__init__()
        self.stage = 3
        self.price = {ResourceType.BOLT: 2,
                      ResourceType.NUT: 1}
        self.ability = 'two defence'


class NitrogenRoomFour(ResourceRoomBase):
    def __init__(self):
        super().__init__()
        self.stage = 3
        self.price = {ResourceType.BOLT: 3,
                      ResourceType.NUT: 2}
        self.produced_resources = {ResourceType.NITROGREN: 4}


class MoraleRoomThree(MoralRoomBase):
    def __init__(self):
        super().__init__()
        self.stage = 3
        self.ability = 'increase morale 3'
        self.price = {ResourceType.BOLT: 2,
                      ResourceType.NUT: 1}

