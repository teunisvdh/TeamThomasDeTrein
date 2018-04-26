import csv
import sys
import os
from data import *
from classes import classes
from classes import helpers

def main():
    # opens file of stations and puts it in a list
    # also creates list of all critical stations
    with open('data/StationsHolland.csv') as csvfile:
        stationsinfo = csv.reader(csvfile, delimiter=',')
        stationList = []
        criticalstationList = []
        for station in stationsinfo:
            stationList.append(classes.Station(station[0], station[1], station[2], station[3]))
            if station[-1] == 'Kritiek':
                criticalstationList.append(station[0])

    # opens file of all connections and puts them in a list
    # also creates list of all critical railways
    with open('data/ConnectiesHolland.csv') as csvfile:
        stationConnections = csv.reader(csvfile, delimiter=',')
        railwayList = []
        criticalRailwayList = []
        for lijn in stationConnections:
            railwayList.append(classes.Rail(lijn[0], lijn[1], lijn[2]))
        for lijn in railwayList:
            if (lijn.stationBeginning in criticalstationList
                or lijn.stationEnd in criticalstationList
                and lijn not in criticalRailwayList):
                    criticalRailwayList.append(lijn)

    raillist_1 = [railwayList[1], railwayList[0], railwayList[27], railwayList[25], railwayList[10]]
    trajectory_1 = classes.Trajectory(raillist_1)

    raillist_2 = [railwayList[3], railwayList[4], railwayList[5], railwayList[17]]
    trajectory_2 = classes.Trajectory(raillist_2)

    raillist_3 = [railwayList[12], railwayList[21], railwayList[23]]
    trajectory_3 = classes.Trajectory(raillist_3)

    raillist_4 = [railwayList[15], railwayList[19], railwayList[13]]
    trajectory_4 = classes.Trajectory(raillist_4)

    raillist_5 = [railwayList[16], railwayList[26], railwayList[27]]
    trajectory_5 = classes.Trajectory(raillist_5)

    raillist_6 = [railwayList[14], railwayList[22], railwayList[24], railwayList[11]]
    trajectory_6 = classes.Trajectory(raillist_6)

    raillist_7 = [railwayList[6]]
    trajectory_7 = classes.Trajectory(raillist_7)

    lijn_1 = [trajectory_1, trajectory_2, trajectory_3, trajectory_4, trajectory_5, trajectory_6, trajectory_7]

    print(classes.Line(lijn_1).SLine(criticalRailwayList))
    print(helpers.printList(railwayList))


if __name__ == "__main__":
    main()
