import random

class RoomStockpile:
    __slots__ = ['game_stage', 'room_deck', 'available_room_1',
                 'available_room_2','available_room_3']

    def __init__(self):
        self.game_stage = 1
        self.room_deck = []
        self.available_room_1 = None
        self.available_room_2 = None
        self.available_room_3 = None

    def increase_game_stage(self):
        self.game_stage += 1

    def get_available_room_1(self):
        room = self.available_room_1
        return room

    def get_available_room_2(self):
        pass

    def get_available_room_3(self):
        pass

    def get_room_from_deck(self):
        if self.game_stage == 1:
            filtered_deck = [room for room in self.room_deck if room.stage == 1]
            return random