import random


class RoomStockpile:
    __slots__ = ['game_stage', 'room_deck', 'available_room_1',
                 'available_room_2', 'available_room_3']

    def __init__(self):
        self.game_stage = 1
        self.room_deck = []
        self.available_room_1 = None
        self.available_room_2 = None
        self.available_room_3 = None

    def increase_game_stage(self):
        self.game_stage += 1

    def get_available_room(self, room_number):
        attr_name = 'available_room_' + str(room_number)
        current_room = getattr(self, attr_name)
        new_room = self._get_room_from_deck()
        setattr(self, attr_name, new_room)

        return current_room

    def _get_room_from_deck(self):
        if not self._cards_are_available():
            raise ValueError("no room cards available")
        elif self.game_stage == 1:
            random_room = random.choice([room for room in self.room_deck if room.stage == 1])
        elif self.game_stage == 2:
            random_room = random.choice([room for room in self.room_deck if room.stage != 3])
        else:
            random_room = random.choice(self.room_deck)

        random_room_index = self.room_deck.index(random_room)

        return self.room_deck.pop(random_room_index)

    def _cards_are_available(self):
        return any([room.stage <= self.game_stage for room in self.room_deck])

