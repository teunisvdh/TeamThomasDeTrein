# makes indexed list of all railway connections
def printList(RailwayList):
    for i in range(len(RailwayList)):
        print('{}:{},{},{}'.format(i, RailwayList[i].stationBeginning,
            RailwayList[i].stationEnd,
            RailwayList[i].minutes))
