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
    chooseRandomTrajectory = random.randint(0,6)
    randomStartLine.remove(randomStartLine[chooseRandomTrajectory])

    print(randomStartLine)
