import csv
import sys
import os
import data
from classes import classes

class openFile:
    """
    Class contains functions to open the files containing
    stations and connections.

    Functions:
        fileStations(self).
        fileConnections(self, criticalstationList).
    """
    def fileStations(self):
        """
        Opens inserted file.

        Args:
            File containing a list with all stations on the map.
            One station contains a: name, coordinates, critical boolean.

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

    def fileConnections(self, criticalstationList):
        """
        Opens inserted file.

        Args:
            File containing a list with all conections on the map.
            criticalStationList: list of all critical stations (from fileStations).

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
