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


class BasicFoodRoom(ResourceRoomBase):
    def __init__(self):
        super().__init__()
        self.stage = 1
        self.price = {ResourceType.BOLT: 1}
        self.produced_resources = {ResourceType.INSECT: 2}

    def round_end_production(self):
        return self.produced_resources


class AdvancedFoodRoom(ResourceRoomBase):
    def __init__(self):
        super().__init__()
        self.stage = 2
        self.price = {ResourceType.BOLT: 2,
                      ResourceType.NUT: 1}
        self.produced_resources = {ResourceType.INSECT: 3}

    def round_end_production(self):
        return self.produced_resources


class SuperAdvancedFoodRoom(ResourceRoomBase):
    def __init__(self):
        super().__init__()
        self.stage = 3
        self.price = {ResourceType.BOLT: 3,
                      ResourceType.NUT: 2}
        self.produced_resources = {ResourceType.INSECT: 4}

    def round_end_production(self):
        return self.produced_resources


class BasicNitrogrenRoom(ResourceRoomBase):
    def __init__(self):
        super().__init__()
        self.stage = 1
        self.price = {ResourceType.BOLT: 1}
        self.produced_resources = {ResourceType.NITROGREN: 2}

    def round_end_production(self):
        return self.produced_resources


class AdvancedNitrogrenRoom(ResourceRoomBase):
    def __init__(self):
        super().__init__()
        self.stage = 2
        self.price = {ResourceType.BOLT: 2,
                      ResourceType.NUT: 1}
        self.produced_resources = {ResourceType.NITROGREN: 3}

    def round_end_production(self):
        return self.produced_resources


class SuperAdvancedNitrogrenRoom(ResourceRoomBase):
    def __init__(self):
        super().__init__()
        self.stage = 3
        self.price = {ResourceType.BOLT: 3,
                      ResourceType.NUT: 2}
        self.produced_resources = {ResourceType.NITROGREN: 4}

    def round_end_production(self):
        return self.produced_resources


class BasicMoraleRoom(ResourceRoomBase):
    def __init__(self):
        super().__init__()
        self.stage = 1
        self.price = None
        self.ability = 'increase morale by 1'


class AdvancedMoraleRoom(ResourceRoomBase):
    def __init__(self):
        super().__init__()
        self.stage = 2
        self.price = {ResourceType.BOLT: 1}
        self.ability = 'increase morale by 2'


class SuperAdvancedMoraleRoom(ResourceRoomBase):
    def __init__(self):
        super().__init__()
        self.stage = 3
        self.price = {ResourceType.BOLT: 3,
                      ResourceType.NUT: 2}
        self.ability = 'increase morale by 3'


class PowerCoreGeneratorRoom(ResourceRoomBase):
    def __init__(self):
        super().__init__()
        self.stage = 2
        self.price = {ResourceType.BOLT: 3,
                      ResourceType.NUT: 1}
        self.produced_resources = {ResourceType.POWER_CORE: 1}


class BasicReputationRoom(ReputationRoomBase):
    def __init__(self):
        super().__init__()
        self.stage = 2
        self.price = {ResourceType.BOLT: 3,
                      ResourceType.NUT: 1}
        self.ability = 'plus 1 reputation'


class AdvancedReputationRoom(ReputationRoomBase):
    def __init__(self):
        super().__init__()
        self.stage = 3
        self.price = {ResourceType.BOLT: 3,
                      ResourceType.NUT: 1}
        self.ability = 'plus 2 reputation'


class BasicScrapRoom(ResourceRoomBase):
    def __init__(self):
        super().__init__()
        self.price = {ResourceType.BOLT: 1}
        self.produced_resources = {ResourceType.BOLT: 1}


class AdvancedScrapRoom(ResourceRoomBase):
    def __init__(self):
        super().__init__()
        self.stage = 2
        self.price = {ResourceType.BOLT: 2,
                      ResourceType.NUT: 2}
        self.produced_resources = {ResourceType.BOLT: 1,
                                   ResourceType.NUT: 1}


class AdvancedInfirmary(MedicalRoomBase):
    def __init__(self):
        super().__init__()
        self.ability = None
