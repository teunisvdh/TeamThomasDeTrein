import csv
import sys
import os
import random
import numpy as np
import numpy.random as rn
from data import *
from classes import classes
from classes import helpers
from algorithms import randomAlgorithm
from algorithms import hillClimber
from algorithms import snakeAlgorithm
from visualisation import visualisation


def main():
    # open the files including critical data
    stationList, criticalStationList = helpers.openFile.fileStations("data/StationsNationaal.csv")
    RailwayList, criticalRailwayList, inverseDict = helpers.openFile.fileConnections("data/ConnectiesNationaal.csv", criticalStationList)
    # print(len(criticalRailwayList))
    # for i in criticalRailwayList:
    #     print(i.stationBeginning, " - ", i.stationEnd)
    #     print(" ------ ")

    emptyLine = classes.Line([], RailwayList, criticalRailwayList, inverseDict)
    emptyTrajectory = classes.Trajectory([], RailwayList)
    #
    scoreList = []
    for i in range(1):
        score = snakeAlgorithm.snakeLine(emptyLine, 4, 100).SLine()
        scoreList.append(score)

    print(max(scoreList))

    # snake = snakeAlgorithm.snakeTrajectory(emptyLine, 15, 100)
    # visualisation.visualize(snake, stationList, RailwayList)

    randomListOfTrajectories = randomAlgorithm.randomLine(emptyLine, 20)

    # hillClimberScores = []
    # for i in range (1000):
    #     print(i)
    #     emptyLine = classes.Line([], RailwayList, criticalRailwayList, inverseDict)
    #     railHill = randomAlgorithm.randomLine(emptyLine, 12)
    #     score = railHill.SLine()
    #     hillClimberScores.append(score)
    #
    # print(max(hillClimberScores))
    # print(sum(hillClimberScores)/ float(len(hillClimberScores)))


    # print(len(criticalRailwayList))
    #
    # for traject in railHill.TrajectoryList:
    #     print(traject.minutesTrajectory())

    # visualisation.visualize(railHill, stationList, RailwayList)



if __name__ == "__main__":
    main()
