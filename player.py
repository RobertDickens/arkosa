from room_inventory import RoomInventory
from resource_types import ResourceType
from room import InsectRoomOne, NitrogrenRoomOne, MedicalRoomOne


class Player:
    def __init__(self):
        self.reputation = 10
        self.inventory = {ResourceType.NITROGREN: 6,
                          ResourceType.INSECT: 6,
                          ResourceType.NUT: 0,
                          ResourceType.BOLT: 2,
                          ResourceType.POWER_CORE: 5}
        self.citizens = 0
        self.morale_bonus_state = 0
        self.rooms = RoomInventory(starting_rooms={'room_1': InsectRoomOne(),
                                                   'room_2': NitrogrenRoomOne(),
                                                   'room_3': MedicalRoomOne()},
                                   starting_defence_rooms={})
        self.people = []

    def trade_resources(self, input_resources, output_resource, n_items):
        for resource in input_resources:
            self.inventory[resource] -= n_items

        self.inventory[output_resource] += n_items

    def trade_insect_for_nitro(self, n_items=1):
        self.trade_resources([ResourceType.INSECT], ResourceType.NITROGREN, n_items)

    def trade_nitro_for_insect(self, n_items=1):
        self.trade_resources([ResourceType.NITROGREN], ResourceType.INSECT, n_items)

    def trade_nitro_for_bolt(self, n_items=1):
        self.trade_resources([ResourceType.NITROGREN], ResourceType.BOLT, n_items)

    def trade_insect_for_bolt(self, n_items=1):
        self.trade_resources([ResourceType.INSECT], ResourceType.BOLT, n_items)

    def trade_nitro_and_insect_for_nut(self, n_items=1):
        self.trade_resources([ResourceType.NITROGREN, ResourceType.INSECT],
                             ResourceType.NUT,
                             n_items)

    def get_room(self, room_stockpile, room_number):
        new_room = room_stockpile.get_available_room(room_number)
        self.rooms.add_room(new_room)

    def round_end_update(self):
        pass