import csv
import sys
import os
import data
from classes import lineClass
from classes import trajectoryClass
from classes import railAndStationClass
from classes import helpers


class Files:
    """
    Class contains functions to open the files containing
    stations and connections and to set the right variables
    based on the map

    Functions:
        setFiles(self.)
        fileStations(self).
        fileConnections(self, criticalstationList).
    """

    def setVariables(self):
        """
        Updates all variables to match the used map.
        Variables in the project files (helpers.py and classes.py) are updated.

        Args:
            Map(String, "holland" or "nationaal"):stating which map is used.
        """

        global file
        global maxTrajectories
        file = "init"
        maxTrajectories = 0
        helpers.Files.file = self
        if self == "holland":
            helpers.Files.maxTrajectories = 7
            helpers.Files.maxMinutes = 120
        elif self == "nationaal":
            helpers.Files.maxTrajectories = 20
            helpers.Files.maxMinutes = 180




    def fileStations():
        """
        Opens the needed file containing a list of stations (stations)

        Returns:
            stationsList(name, x, y, critical): list of all stations.
            criticalstationList(name, x, y, critical): list of all critical stations.
        """

        if helpers.Files.file == "holland":
            usedfile = "data/StationsHolland.csv"
        if helpers.Files.file == "nationaal":
            usedfile = "data/StationsNationaal.csv"

        with open(usedfile) as csvfile:
            stationsinfo = csv.reader(csvfile, delimiter=',')
            stationList = []
            criticalStationList = []
            for station in stationsinfo:
                stationList.append(railAndStationClass.Station(station[0], station[1], station[2], station[3]))
                if station[-1] == 'Kritiek':
                    criticalStationList.append(station[0])
            return stationList, criticalStationList

    def fileConnections(criticalStationList):
        """
        Opens the needed file containing a list of connections (rails)

        Args:
            criticalStationList: list of all critical stations (from fileStations).

        Returns:
            RailwayList(StationBeginning, StationEnd, minutes): list of all railways .
            criticalRailwayList(StationBeginning, StationEnd, minutes): list of all critical railways.
        """

        if helpers.Files.file == "holland":
            usedfile = "data/ConnectiesHolland.csv"
        elif helpers.Files.file == "nationaal":
            usedfile = "data/ConnectiesNationaal.csv"

        with open(usedfile) as csvfile:
            stationConnections = csv.reader(csvfile, delimiter=',')
            RailwayList = []
            criticalRailwayList = []
            inverseDict = {}
            for lijn in stationConnections:
                railValue = railAndStationClass.Rail(lijn[0], lijn[1], lijn[2])
                RailwayList.append(railValue)
                # change list and append in temp
                lijn[0], lijn[1] = lijn[1], lijn[0]
                railKey = railAndStationClass.Rail(lijn[0], lijn[1], lijn[2])
                RailwayList.append(railKey)

                inverseDict[railValue] = railKey
                inverseDict[railKey] = railValue

            for lijn in RailwayList:
                if (lijn.stationBeginning in criticalStationList
                or lijn.stationEnd in criticalStationList
                and lijn not in criticalRailwayList):
                    criticalRailwayList.append(lijn)

            return RailwayList, criticalRailwayList, inverseDict
