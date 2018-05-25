import csv
import sys
import os
import random
import numpy as np
import numpy.random as rn
from classes import lineClass
from classes import trajectoryClass
from classes import railAndStationClass
from classes import helpers
from algorithms import randomAlgorithm
from algorithms import hillClimber
from algorithms import SimulatedAnnealing
from visualisation import visualisation
import data


def main():
    # initialize file ('nationaal'/'holland')
    helpers.Files.initializeVariables("nationaal")

    # initialize critical value ('normal'/'critical')
    helpers.Files.setCritical("normal")

    # determine the values for multiplication in temperature
    helpers.Files.setMulitplicationAdd(20)
    helpers.Files.setMulitplicationChop(20)

    # open the files including critical data
    stationList, criticalStationList = helpers.Files.fileStations()
    RailwayList, criticalRailwayList, inverseDict = helpers.Files.fileConnections(criticalStationList)

    # make empty trajectory and line
    emptyTrajectory = trajectoryClass.Trajectory([], RailwayList)
    emptyLine = lineClass.Line([], RailwayList, criticalRailwayList, inverseDict)

    # call randomAlgorithm
    randomLine = randomAlgorithm.randomLine(emptyLine, 7, 10)

    # call hillClimber
    hillclimberLine = hillClimber.hillClimber(randomLine, 2000, "random", 20)

    # call SimulatedAnnealing
    simulatedannealingLine = SimulatedAnnealing.snakeLine(emptyLine, 1, 5, 15, "snake", 10)

    # call visualisation (choose algorithm randomline, hillclimberLine or simulatedannealingLine)
    algorithm = simulatedannealingLine
    visualisation.visualize(algorithm, stationList, RailwayList)
    visualisation.printLine(algorithm)

if __name__ == "__main__":
    main()
