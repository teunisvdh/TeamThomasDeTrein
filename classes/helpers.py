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
            One station contains a: name of the station, cheograpical coordinates, critical boolean.

        Returns:
            stationsList(name, x, y, critical): list of all stations.
            criticalstationList(name, x, y, critical): list of all critical stations.
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
            Connection contains a: StationBeginning(name), StationEnd(name), minutes of the connection.
            criticalStationList: list of all critical stations (from fileStations).

        Returns:
            RailwayList(StationBeginning, StationEnd, minutes): list of all railways .
            criticalRailwayList(StationBeginning, StationEnd, minutes): list of all critical railways.
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
