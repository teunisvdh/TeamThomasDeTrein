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
        RailwayList = []
        criticalRailwayList = []
        for lijn in stationConnections:
            RailwayList.append(classes.Rail(lijn[0], lijn[1], lijn[2]))
        for lijn in RailwayList:
            if (lijn.stationBeginning in criticalstationList
                or lijn.stationEnd in criticalstationList
                and lijn not in criticalRailwayList):
                    criticalRailwayList.append(lijn)

    Raillist_1 = [RailwayList[1], RailwayList[0], RailwayList[27], RailwayList[25], RailwayList[10]]
    Trajectory_1 = classes.Trajectory(Raillist_1)

    Raillist_2 = [RailwayList[3], RailwayList[4], RailwayList[5], RailwayList[17]]
    Trajectory_2 = classes.Trajectory(Raillist_2)

    Raillist_3 = [RailwayList[12], RailwayList[21], RailwayList[23]]
    Trajectory_3 = classes.Trajectory(Raillist_3)

    Raillist_4 = [RailwayList[15], RailwayList[19], RailwayList[13]]
    Trajectory_4 = classes.Trajectory(Raillist_4)

    Raillist_5 = [RailwayList[16], RailwayList[26], RailwayList[27]]
    Trajectory_5 = classes.Trajectory(Raillist_5)

    Raillist_6 = [RailwayList[14], RailwayList[22], RailwayList[24], RailwayList[11]]
    Trajectory_6 = classes.Trajectory(Raillist_6)

    Raillist_7 = [RailwayList[6]]
    Trajectory_7 = classes.Trajectory(Raillist_7)

    lijn_1 = [Trajectory_1, Trajectory_2, Trajectory_3, Trajectory_4, Trajectory_5, Trajectory_6, Trajectory_7]

    print(classes.Line(lijn_1).SLine(criticalRailwayList))


if __name__ == "__main__":
    main()
