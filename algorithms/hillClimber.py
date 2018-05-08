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
    randomStartTrajectory = randomAlgorithm.randomAlgorithm(RailwayList, criticalRailwayList)

    print(randomStartTrajectory)
