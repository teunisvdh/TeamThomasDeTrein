import random
import csv
import sys
import os
from data import *
from classes import classes
from classes import helpers
from algorithms import randomAlgorithm
sys.path.append('C:/TeamThomasDeTrein/classes')

def hillClimber(RailwayList, criticalRailwayList):

    randomStartLine = randomAlgorithm.randomLine(RailwayList, criticalRailwayList)

    for i in range(10000):
        score = helpers.calculate.score(randomStartLine, criticalRailwayList)

        chooseRandomTrajectory = random.randint(0,6)
        randomTrajectoryRemove = randomStartLine[chooseRandomTrajectory]
        randomStartLine.remove(randomTrajectoryRemove)

        replaceTrajectory = randomAlgorithm.randomTrajectory(RailwayList)

        randomStartLine.append(replaceTrajectory)
        score_3 = helpers.calculate.score(randomStartLine, criticalRailwayList)

        if score_3 < score:
            randomStartLine.remove(replaceTrajectory)
            randomStartLine.append(randomTrajectoryRemove)

        score_4 = helpers.calculate.score(randomStartLine, criticalRailwayList)

    print(score_4)

    return randomStartLine
