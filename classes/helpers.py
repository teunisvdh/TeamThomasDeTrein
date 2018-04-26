import csv
import sys
import os
from data import *
from classes import classes

class show:
    def printList(RailwayList):
        for i in range(len(RailwayList)):
            print('{}:{},{},{}'.format(i, RailwayList[i].stationBeginning,
                RailwayList[i].stationEnd,
                RailwayList[i].minutes))

    def printScore(self, criticalRailwayList):
        print(classes.Line(self).SLine(criticalRailwayList))

class openFile:
    def file1(self):
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
