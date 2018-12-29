from inventory import Inventory


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
        self.rooms = None
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


