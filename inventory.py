class Inventory:
    __slots__ = ['nitrogen', 'insects', 'bolts', 'nuts', 'power_cores',
                 'citizens', 'morale_points']

    def __init__(self, nitrogen, insects, nuts, bolts, power_cores,
                 citizens, morale_points):
        self.nitrogen = nitrogen
        self.insects = insects
        self.nuts = nuts
        self.bolts = bolts
        self.power_cores = power_cores
        self.citizens = citizens
        self.morale_points = morale_points

    def trade_insect_for_nitro(self, n_items=1):
        self.insects = self.insects - n_items
        self.nitrogen = self.nitrogen + n_items

    def trade_nitro_for_insect(self, n_items=1):
        self.nitrogen = self.nitrogen - n_items
        self.insects = self.insects + n_items

    def trade_nitro_for_bolt(self, n_items=1):
        self.nitrogen = self.nitrogen - n_items
        self.bolts = self.bolts + n_items

    def trade_insect_for_bolt(self, n_items=1):
        self.insects = self.insects - n_items
        self.bolts = self.bolts + n_items

    def trade_nitro_and_insect_for_nut(self, n_items=1):
        self.insects = self.insects - n_items
        self.nitrogen = self.nitrogen - n_items
