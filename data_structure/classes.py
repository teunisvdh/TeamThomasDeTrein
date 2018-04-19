class Lijnvoering:
    def __init__(self):
        pass

class Traject(Spoor):
    def __init__(self):

    def minutenTraject(self):

class Spoor:
    def __init__(self, stationBegin, stationEind, minuten):
        self.stationBegin = stationBegin
        self.stationEind = stationEind
        self.minuten = minuten

class Station:
    def __init__(self, x, y, kritiek):
        self.x = x
        self.y = y
        self.kritiek = kritiek
