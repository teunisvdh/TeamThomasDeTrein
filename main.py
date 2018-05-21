import csv
import sys
import os
import random
from data import *
from classes import classes
from classes import helpers
from algorithms import randomAlgorithm
from algorithms import hillClimber
from algorithms import snakeAlgorithm
from visualisation import visualisation


def main():
    # open the files including critical data
    stationList, criticalStationList = helpers.openFile.fileStations("data/StationsHolland.csv")
    RailwayList, criticalRailwayList = helpers.openFile.fileConnections("data/ConnectiesHolland.csv", criticalStationList)
    # print(len(criticalRailwayList))
    # for i in criticalRailwayList:
    #     print(i.stationBeginning, " - ", i.stationEnd)
    #     print(" ------ ")

    emptyLine = classes.Line([], RailwayList, criticalRailwayList)
    # emptyTrajectory = classes.Trajectory([], RailwayList)
    #
    snakeAlgorithm.snakeTrajectory(emptyLine, 1, 10)

    # randomListOfTrajectories = randomAlgorithm.randomLine(emptyLine, 7)
    #
    # print(visualisation.printLine(randomListOfTrajectories))
    # railHill = hillClimber.hillClimber(randomListOfTrajectories, 10000)

    # for traject in railHill.TrajectoryList:
    #     print(traject.minutesTrajectory())



if __name__ == "__main__":
    main()
