from inventory import Inventory
from room_inventory import RoomInventory
from room import InsectRoomOne, NitrogrenRoomOne, MedicalRoomOne


class Player:
    def __init__(self):
        self.reputation = 10
        self.inventory = Inventory(nitrogen=6,
                                   insects=6,
                                   nuts=0,
                                   bolts=2,
                                   power_cores=5,
                                   citizens=0,
                                   morale_points=0)
        self.rooms = RoomInventory(starting_rooms={'room_1': InsectRoomOne(),
                                                   'room_2': NitrogrenRoomOne(),
                                                   'room_3': MedicalRoomOne()},
                                   starting_defence_rooms={})
        self.people = []

    def trade_insect_for_nitro(self, n_items=1):
        self.inventory.trade_insect_for_nitro()

    def trade_nitro_for_insect(self, n_items=1):
        self.inventory.trade_nitro_for_insect()

    def trade_nitro_for_bolt(self, n_items=1):
        self.inventory.trade_nitro_for_bolt()

    def trade_insect_for_bolt(self, n_items=1):
        self.inventory.trade_insect_for_bolt()

    def trade_nitro_and_insect_for_nut(self, n_items=1):
        self.inventory.trade_nitro_and_insect_for_nut()

    def get_room(self, room_stockpile, room_number):
        new_room = room_stockpile.get_available_room(room_number)
        self.rooms.add_room(new_room)

    def round_end_update(self):
        self.inventory