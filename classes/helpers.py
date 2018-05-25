import csv
import sys
import os
import data
from classes import lineClass
from classes import trajectoryClass
from classes import railAndStationClass
from classes import helpers


class Files:
    """Class contains functions to open the files containing
    stations and connections and to set the right variables
    based on the map
    """

    def initializeVariables(self):
        """Updates all variables to match the used map.
        Variables in the project files (helpers.py and classes.py and algorithms) are updated.

        Args:
            Map(String, "holland" or "nationaal"):stating which map is used.
        """

        global file
        global criticalMap
        global maxTrajectories
        global maxMinutes
        global usedfileStations
        global usedfileConnections
        global multiplicationAdd
        global multiplicationChop


        file = "init"
        critical = "init"
        maxTrajectories = 0
        maxMinutes = 0
        usedfileStations = "init"
        usedfileConnections = "init"
        multiplicationAdd = 0
        multiplicationChop = 0

        helpers.Files.file = self
        if self != "holland" and self != "nationaal":
            raise ValueError("file must be 'holland' or 'nationaal'")

    def setCritical(self):
        """Set the global map files.If 'citical' is used as input the critical station map is used.
            When 'normal' is used as input, the normal station map is used.

        Args:
            Map(String, "critical" or "normal"):stating which map is used.
        """
        helpers.Files.criticalMap = self
        if self != "normal" and self != "critical":
            raise ValueError("critical value must be 'normal' or 'critical'")

        if helpers.Files.file == "holland":
            helpers.Files.maxTrajectories = 7
            helpers.Files.maxMinutes = 120
            helpers.Files.usedfileConnections = "data/ConnectiesHolland.csv"

            if self == "normal":
                helpers.Files.usedfileStations = "data/StationsHolland.csv"
            elif self == "critical":
                helpers.Files.usedfileStations = "data/StationsHollandCritical.csv"

        elif helpers.Files.file == "nationaal":
            helpers.Files.maxTrajectories = 20
            helpers.Files.maxMinutes = 180
            helpers.Files.usedfileConnections = "data/ConnectiesNationaal.csv"

            if self == "normal":
                helpers.Files.usedfileStations = "data/StationsNationaal.csv"
            elif self == "critical":
                helpers.Files.usedfileStations = "data/StationsNationaalCritical.csv"

    def setMulitplicationAdd(self):
        """Sets the multiplication for temperature for adding rails.
        """
        helpers.Files.multiplicationAdd = self

    def setMulitplicationChop(self):
        """Sets the multiplication for temperature for chopping off rails.
        """
        helpers.Files.multiplicationChop = self


    def fileStations():
        """Opens the needed file containing a list of stations (stations)

        Returns:
            stationsList(name, x, y, critical): list of all stations.
            criticalstationList(name, x, y, critical): list of all critical stations.
        """

        with open(helpers.Files.usedfileStations) as csvfile:
            stationsinfo = csv.reader(csvfile, delimiter=',')
            stationList = []
            criticalStationList = []
            for station in stationsinfo:
                stationList.append(railAndStationClass.Station(station[0], station[1], station[2], station[3]))
                if station[-1] == 'Kritiek':
                    criticalStationList.append(station[0])
            return stationList, criticalStationList

    def fileConnections(criticalStationList):
        """Opens the needed file containing a list of connections (rails)

        Args:
            criticalStationList: list of all critical stations (from fileStations).

        Returns:
            RailwayList(StationBeginning, StationEnd, minutes): list of all railways .
            criticalRailwayList(StationBeginning, StationEnd, minutes): list of all critical railways.
        """
        with open(helpers.Files.usedfileConnections) as csvfile:
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
