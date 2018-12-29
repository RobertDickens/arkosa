class RoomInventory:
    __slots__ = ['defence_room_1', 'defence_room_2',
                 'room_1', 'room_2', 'room_3', 'room_4',
                 'room_5', 'room_6', 'room_7', 'room_8']

    def __init__(self, defence_room_1, defence_room_2,
                 room_1, room_2, room_3, room_4, room_5,
                 room_6, room_7, room_8):
        self.defence_room_1 = defence_room_1
        self.defence_room_2 = defence_room_2
        self.room_1 = room_1
        self.room_2 = room_2
        self.room_3 = room_3
        self.room_4 = room_4
        self.room_5 = room_5
        self.room_6 = room_6
        self.room_7 = room_7
        self.room_8 = room_8

    def add_room(self, roomtype, build_over_room=None):
        pass

    def _choose_empty_room(self):
        pass

    def _choose_empty_defence_room(self):
        pass