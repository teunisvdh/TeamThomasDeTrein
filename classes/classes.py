class Lijnvoering:
    def __init__(self, traject1, traject2 = '',
        traject3 = '', traject4 = '',traject5 = '',
        traject6 = '', traject7= '', traject8= '', traject9 = ''):
        self.traject1 = traject1
        self.traject2 = traject2
        self.traject3 = traject3
        self.traject4 = traject4
        self.traject5 = traject5
        self.traject6 = traject6
        self.traject7 = traject7
        self.traject8 = traject8
        self.traject9 = traject9

    def SLijnvoering(self, kritiekeSporenLijst):
        trajectLijst = [self.traject1, self.traject2,
            self.traject3, self.traject4,self.traject5,
            self.traject6, self.traject7, self.traject8,
            self.traject9]
        minuten = 0
        treinen = 0
        kritiekeSporen = []
        for traject in trajectLijst:
            if traject is not '':
                minuten += Traject.minutenTraject(traject)
                treinen += 1
        for traject in trajectLijst:
            if traject is not '':
                for spoor in traject.__dict__.items():
                    if spoor[1] is not '':
                        if spoor[1] in kritiekeSporenLijst:
                            if spoor[1] not in kritiekeSporen:
                                kritiekeSporen.append(spoor[1])

        p = len(kritiekeSporen) / len(kritiekeSporenLijst)

        return ['min = {}'.format(minuten),
            't = {}'.format(treinen), 'p = {}'.format(p),
            'S = {}'.format(10000 * p - (treinen * 20 + minuten / 10)) ]

class Traject:
    def __init__(self, spoor1, spoor2 = '', spoor3 = '', spoor4 = '',
    spoor5 = '', spoor6 = '', spoor7= '', spoor8= '', spoor9 = ''):
        self.spoor1 = spoor1
        self.spoor2 = spoor2
        self.spoor3 = spoor3
        self.spoor4 = spoor4
        self.spoor5 = spoor5
        self.spoor6 = spoor6
        self.spoor7 = spoor7
        self.spoor8 = spoor8
        self.spoor9 = spoor9
        spoorlist = [self.spoor1, self.spoor2,
            self.spoor3, self.spoor4, self.spoor5,
            self.spoor6, self.spoor7, self.spoor8, self.spoor9]
        for i in range(len(spoorlist) - 1):
            if spoorlist[i] != '' and spoorlist[i+1] != '':
                if (spoorlist[i].stationBegin != spoorlist[i+1].stationBegin
                    and spoorlist[i].stationEind != spoorlist[i+1].stationEind
                    and spoorlist[i].stationBegin != spoorlist[i+1].stationEind
                    and spoorlist[i].stationEind != spoorlist[i+1].stationBegin):
                        print('Error: cannot make traject')
                        print(spoorlist[i].stationBegin)
                        print(spoorlist[i+1].stationBegin)
                        break

    def minutenTraject(self):
        spoorlist = [self.spoor1, self.spoor2, self.spoor3,
            self.spoor4, self.spoor5,self.spoor6,
            self.spoor7, self.spoor8, self.spoor9]
        minuten = 0
        for station in spoorlist:
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
