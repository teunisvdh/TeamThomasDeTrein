import csv
import sys
import os
from data import *
from classes import classes

class calculate:
    def score(self, criticalRailwayList):
        score = classes.Line(self).SLine(criticalRailwayList)
        return score

    def minutesTrajectory(self):
        minutes = 0
        for station in self:
                minutes += station.minutes
        if minutes > 120:
            print("to much minutes!")
        return minutes

class show:
    """Class contains functions to show information.

    Functions:
        printList.
    """
    def printList(RailwayList):
        """Prints list indexed list of all railway connections.

        Args:
            RailwayList (list): List of railways that you want to print.

        Returns:
            Printed list of indexed railways.
        """
        for i in range(len(RailwayList)):
            print('{}:{},{},{}'.format(i, RailwayList[i].stationBeginning,
                RailwayList[i].stationEnd,
                RailwayList[i].minutes))

class openFile:
    """
    Class contains functions to open files

    Functions:
        file1(self).
        file2(self, criticalstationList).
    """
    def file1(self):
        """
        Opens inserted file.

        Args:
            file1 (stationsHolland.csv).

        Returns:
            stationsList: list of all stations.
            criticalstationList: list of all critical stations.
        """
        with open(self) as csvfile:
            stationsinfo = csv.reader(csvfile, delimiter=',')
            stationList = []
            criticalstationList = []
            for station in stationsinfo:
                stationList.append(classes.Station(station[0], station[1], station[2], station[3]))
                if station[-1] == 'Kritiek':
                    criticalstationList.append(station[0])
            return stationList, criticalstationList

    def file2(self, criticalstationList):
        """
        Opens inserted file.

        Args:
            file2 (ConnectiesHolland.csv).
            criticalStationList: list of all critical stations.

        Returns:
            RailwayList: list of all railways.
            criticalRailwayList: list of all critical railways.
        """
        with open(self) as csvfile:
            stationConnections = csv.reader(csvfile, delimiter=',')
            RailwayList = []
            criticalRailwayList = []
            for lijn in stationConnections:
                RailwayList.append(classes.Rail(lijn[0], lijn[1], lijn[2]))
            for lijn in RailwayList:
                if (lijn.stationBeginning in criticalstationList or lijn.stationEnd in criticalstationList
                and lijn not in criticalRailwayList):
                    criticalRailwayList.append(lijn)
            return RailwayList, criticalRailwayList
