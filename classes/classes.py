class Lijnvoering:
    def __init__(self, trajectLijst, kritiekeSporenLijst):
        self.trajectLijst = trajectLijst
        self.kritiekeSporenLijst = kritiekeSporenLijst
    def SLijnvoering(self):
        minuten = 0
        treinen = 0
        kritiekeSporen = []
        for traject in self.trajectLijst:
            if traject is not '':
                minuten += Traject.minutenTraject(traject)
                treinen += 1
        for traject in self.trajectLijst:
            for spoor in traject.__dict__.items():
                for spoortje in spoor[1]:
                    if spoortje not in kritiekeSporen:
                        if spoortje in self.kritiekeSporenLijst:
                            kritiekeSporen.append(spoortje)

        p = len(kritiekeSporen) / len(self.kritiekeSporenLijst)

        return ['min = {}'.format(minuten),
            't = {}'.format(treinen), 'p = {}'.format(p),
            'S = {}'.format(10000 * p - (treinen * 20 + minuten / 10)) ]

class Traject:
    def __init__(self, spoorlist):
        self.spoorlist = spoorlist
        for i in range(len(self.spoorlist) - 1):
            if (self.spoorlist[i].stationBegin != self.spoorlist[i+1].stationBegin
                and self.spoorlist[i].stationEind != self.spoorlist[i+1].stationEind
                and self.spoorlist[i].stationBegin != self.spoorlist[i+1].stationEind
                and self.spoorlist[i].stationEind != self.spoorlist[i+1].stationBegin):
                    print('Error: cannot make traject')
                    print(self.spoorlist[i].stationBegin)
                    print(self.spoorlist[i+1].stationBegin)
                    break

    def minutenTraject(self):
        minuten = 0
        for station in self.spoorlist:
            if station is not '':
                minuten += station.minuten
        return minuten

class Spoor:
    def __init__(self, stationBegin, stationEind, minuten):
        self.stationBegin = stationBegin
        self.stationEind = stationEind
        self.minuten = int(minuten)

class Station:
    def __init__(self, name, x, y, kritiek):
        self.name = name
        self.x = x
        self.y = y
        self.kritiek = kritiek
