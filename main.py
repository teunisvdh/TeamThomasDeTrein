import csv
import sys
import os
import random
from data import *
from classes import classes
from classes import helpers
from classes import make
from algorithms import randomAlgorithm
from algorithms import hillClimber

from visualisation import visualisation

def main():
    # open the files including critical data
    stationList, criticalstationList = helpers.openFile.file1("data/StationsHolland.csv")
    RailwayList, criticalRailwayList = helpers.openFile.file2("data/ConnectiesHolland.csv", criticalstationList)


    emptyLine = classes.Line([], RailwayList, criticalRailwayList)
    emptyTrajectory = classes.Trajectory([], RailwayList)

    randomListOfTrajectories = randomAlgorithm.randomLine(emptyLine, 7)

    railHill = hillClimber.hillClimber(randomListOfTrajectories, 10000)

    for traject in railHill.TrajectoryList:
        print(traject.minutesTrajectory())

    visualisation.visualize(railHill)

if __name__ == "__main__":
    main()
