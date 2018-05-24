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
from algorithms import Annealclimber
from visualisation import visualisation
import data


def main():
    helpers.Files.setVariables("holland")
    # put "holland" or "nationaal"

    # open the files including critical data
    stationList, criticalStationList = helpers.Files.fileStations()
    RailwayList, criticalRailwayList, inverseDict = helpers.Files.fileConnections(criticalStationList)
    # print(len(criticalRailwayList))
    # for i in criticalRailwayList:
    #     print(i.stationBeginning, " - ", i.stationEnd)
    #     print(" ------ ")

    #
    # scoreList = []
    # for i in range(10):
    #     score = SimulatedAnnealing.snakeTrajectory(emptyLine, 4, 100)
    #     scoreList.append(score)
    #
    # print(max(scoreList))

    scoreList = []
    highestLine = None
    highestScore = 0
    scoreTotal = 0
    scoreAverage = 0

    for i in range(2):
        emptyLine = lineClass.Line([], RailwayList, criticalRailwayList, inverseDict)
        emptyTrajectory = trajectoryClass.Trajectory([], RailwayList)
        snake = SimulatedAnnealing.snakeLine(emptyLine, 7, 5, 15, "random")
        score = snake.SLine()
        scoreList.append(score)
        scoreTotal = scoreTotal + score
        if score > highestScore:
            highestScore = score
            highestLine = snake

    print("highscore", highestScore)
    print("averagescore", scoreTotal / len(scoreList))
    visualisation.visualize(highestLine, stationList, RailwayList)
    visualisation.printTest(highestLine)


    # emptyLine = classes.Line([], RailwayList, criticalRailwayList, inverseDict)
    # randomListOfTrajectories = randomAlgorithm.randomLine(emptyLine, 20)
    #
    # railHill = hillClimber.hillClimber(randomListOfTrajectories, 100, "random")
    #
    # print(railHill.SLine())

    # for traject in railHill.TrajectoryList:
        # print(traject.minutesTrajectory())

    # visualisation.visualize(railHill, stationList, RailwayList)

    list0 = []
    list1000 = []
    list2000 = []
    list3000 = []
    list4000 = []
    list5000 = []
    list6000 = []
    list7000 = []
    list8000 = []
    list9000 = []
    list10000 = []
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    list8 = []
    list9 = []
    list10 = []


    for i in scoreList:
        if i >= 0 and i < 1000:
            list1000.append(i)
        elif i >= 1000 and i < 2000:
            list2000.append(i)
        elif i >= 2000 and i < 3000:
            list3000.append(i)
        elif i >= 3000 and i < 4000:
            list4000.append(i)
        elif i >= 4000 and i < 5000:
            list5000.append(i)
        elif i >= 5000 and i < 6000:
            list6000.append(i)
        elif i >= 6000 and i < 7000:
            list7000.append(i)
        elif i >= 7000 and i < 8000:
            list8000.append(i)
        elif i >= 8000 and i < 9000:
            list9000.append(i)
        elif i >= 9000:
            list10000.append(i)
        else:
            list0.append(i)

    for i in list10000:
        if i >= 9000 and i < 9100:
            list1.append(i)
        elif i >= 9100 and i < 9200:
            list2.append(i)
        elif i >= 9200 and i < 9300:
            list3.append(i)
        elif i >= 9300 and i < 9400:
            list4.append(i)
        elif i >= 9400 and i < 9500:
            list5.append(i)
        elif i >= 9500 and i < 9600:
            list6.append(i)
        elif i >= 9600 and i < 9700:
            list7.append(i)
        elif i >= 9700 and i < 9800:
            list8.append(i)
        elif i >= 9800 and i < 9900:
            list9.append(i)
        elif i >= 9900:
            list10.append(i)


    print('iterations: ', len(scoreList))
    print('<0', len(list0))
    print('0-1000', len(list1000))
    print('1000-2000', len(list2000))
    print('2000-3000', len(list3000))
    print('3000-4000', len(list4000))
    print('4000-5000', len(list5000))
    print('5000-6000', len(list6000))
    print('6000-7000', len(list7000))
    print('7000-8000', len(list8000))
    print('8000-9000', len(list9000))
    print('>9000', len(list10000))

    print('9000-9100', len(list1))
    print('9100-9200', len(list2))
    print('9200-9300', len(list3))
    print('9300-9400', len(list4))
    print('9400-9500', len(list5))
    print('9500-9600', len(list6))
    print('9600-9700', len(list7))
    print('9700-9800', len(list8))
    print('9800-9900', len(list9))
    print('>9900', len(list10))



if __name__ == "__main__":
    main()
