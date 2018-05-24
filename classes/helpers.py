import csv
import sys
import os
import data
from classes import classes
from classes import settings


class openFile:
    """
    Class contains functions to open the files containing
    stations and connections.

    Functions:
        fileStations(self).
        fileConnections(self, criticalstationList).
    """
    def fileStations():
        """
        Opens inserted file.

        Args:
            File containing a list with all stations on the map.
            One station contains a: name of the station, cheograpical coordinates, critical boolean.

        Returns:
            stationsList(name, x, y, critical): list of all stations.
            criticalstationList(name, x, y, critical): list of all critical stations.
        """
        if settings.file == "holland":
            usedfile = "data/StationsHolland.csv"
        if settings.file == "nationaal":
            usedfile = "data/StationsNationaal.csv"

        with open(usedfile) as csvfile:
            stationsinfo = csv.reader(csvfile, delimiter=',')
            stationList = []
            criticalStationList = []
            for station in stationsinfo:
                stationList.append(classes.Station(station[0], station[1], station[2], station[3]))
                if station[-1] == 'Kritiek':
                    criticalStationList.append(station[0])
            return stationList, criticalStationList

    def fileConnections(criticalStationList):
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
        if settings.file == "holland":
            usedfile = "data/ConnectiesHolland.csv"
        elif settings.file == "nationaal":
            usedfile = "data/ConnectiesNationaal.csv"

        with open(usedfile) as csvfile:
            stationConnections = csv.reader(csvfile, delimiter=',')
            RailwayList = []
            criticalRailwayList = []
            inverseDict = {}
            for lijn in stationConnections:
                railValue = classes.Rail(lijn[0], lijn[1], lijn[2])
                RailwayList.append(railValue)
                # change list and append in temp
                lijn[0], lijn[1] = lijn[1], lijn[0]
                railKey = classes.Rail(lijn[0], lijn[1], lijn[2])
                RailwayList.append(railKey)

                inverseDict[railValue] = railKey
                inverseDict[railKey] = railValue

            for lijn in RailwayList:
                if (lijn.stationBeginning in criticalStationList
                or lijn.stationEnd in criticalStationList
                and lijn not in criticalRailwayList):
                    criticalRailwayList.append(lijn)

            return RailwayList, criticalRailwayList, inverseDict
