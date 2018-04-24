def printList(sporenLijst):
    for i in range(len(sporenLijst)):
        print('{}:{},{},{}'.format(i, sporenLijst[i].stationBegin,
            sporenLijst[i].stationEind,
            sporenLijst[i].minuten))
