import csv
import sys
import os
import random
import numpy as np
import numpy.random as rn
from classes import classes
from classes import helpers
from algorithms import randomAlgorithm
from algorithms import hillClimber
from algorithms import snakeAlgorithm
from visualisation import visualisation
import data


def main():
    # open the files including critical data
    stationList, criticalStationList = helpers.openFile.fileStations("data/StationsNationaal.csv")
    RailwayList, criticalRailwayList, inverseDict = helpers.openFile.fileConnections("data/ConnectiesNationaal.csv", criticalStationList)
    # print(len(criticalRailwayList))
    # for i in criticalRailwayList:
    #     print(i.stationBeginning, " - ", i.stationEnd)
    #     print(" ------ ")

    #
    # scoreList = []
    # for i in range(10):
    #     score = snakeAlgorithm.snakeTrajectory(emptyLine, 4, 100)
    #     scoreList.append(score)
    #
    # print(max(scoreList))

    scoreList = []
    highestLine = None
    highestScore = 0
    scoreTotal = 0
    scoreAverage = 0

    for i in range(10):
        emptyLine = classes.Line([], RailwayList, criticalRailwayList, inverseDict)
        emptyTrajectory = classes.Trajectory([], RailwayList)
        snake = snakeAlgorithm.snakeLine(emptyLine, 12, 5)
        score = snake.SLine()
        scoreList.append(score)
        scoreTotal = scoreTotal + score
        if score > highestScore:
            highestScore = score
            highestLine = snake

    print("highscore", highestScore)
    print("averagescore", scoreTotal / len(scoreList))
    visualisation.visualize(highestLine, stationList, RailwayList)
    visualisation.printLine(highestLine)


    # emptyLine = classes.Line([], RailwayList, criticalRailwayList, inverseDict)
    # randomListOfTrajectories = randomAlgorithm.randomLine(emptyLine, 20)
    #
    #
    # railHill = hillClimber.hillClimber(randomListOfTrajectories, 1000)
    #
    # print(railHill.SLine())

    # for traject in railHill.TrajectoryList:
        # print(traject.minutesTrajectory())

    # visualisation.visualize(railHill, stationList, RailwayList)



if __name__ == "__main__":
    main()
