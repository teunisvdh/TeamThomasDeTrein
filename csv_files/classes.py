import csv

class Lijnvoering:
    def __init__(self):
        pass

class Traject:
    def __init__(self):
        pass

    def minutenTraject(self):
        pass

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

with open('StationsHolland.csv') as csvfile:
    stationsinfo = csv.reader(csvfile, delimiter=',')
    for i in range(len(stationsinfo)):
        spoor_i = Station(stationsinfo[i][1], stationsinfo[i][2],stationsinfo[i][3])

spoor_1 = Spoor('amsterdam', 'haarlem', 5)

print(spoor_1.stationBegin)
