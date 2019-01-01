class RoomInventory:
    __slots__ = ['starting_defence_rooms', 'starting_rooms',
                 'defence_rooms', 'rooms']

    def __init__(self, starting_defence_rooms,
                 starting_rooms):
        self.starting_rooms = starting_rooms
        self.starting_defence_rooms = starting_defence_rooms
        self.defence_rooms = self._init_defence_rooms()
        self.rooms = self._init_rooms()

    def _init_rooms(self):
        rooms = dict(room_1=None,
                     room_2=None,
                     room_3=None,
                     room_4=None,
                     room_5=None,
                     room_6=None,
                     room_7=None,
                     room_8=None)

        if self.starting_rooms:
            rooms.update(self.starting_rooms)

        return rooms

    def _init_defence_rooms(self):
        defence_rooms = dict(defence_room_1=None,
                             defence_room_2=None)

        if self.starting_defence_rooms:
            defence_rooms.update(self.starting_defence_rooms)

        return defence_rooms

    def add_room(self, room, build_over_room=None):
        if not build_over_room:
            if not room.defense:
                empty_room_key = self._choose_empty_room()
                self.rooms[empty_room_key] = room
            else:
                empty_room_key = self._choose_empty_defence_room()
                self.rooms[empty_room_key] = room
        else:
            self.rooms[build_over_room] = room

    def produce_resources(self):
        produced_resources = {}
        occupied_rooms = [room for room in self.rooms.values() if room is not None]
        for room in occupied_rooms:
            if room.resource_production:
                produced_resources.update(room.round_end_production())

        return produced_resources

    def _choose_empty_room(self):
        empty_rooms = [k for k, v in self.rooms.items() if v is None]
        if not empty_rooms:
            raise ValueError("No empty rooms found")
        first_empty_room = empty_rooms[0]
        return first_empty_room

    def _choose_empty_defence_room(self):
        empty_rooms = [k for k, v in self.defence_rooms.items() if v is None]
        if not empty_rooms:
            raise ValueError("No empty defence rooms found")
        first_empty_defence_room = empty_rooms[0]
        return first_empty_defence_room
