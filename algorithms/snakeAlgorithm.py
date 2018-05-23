import random
import csv
import sys
import os
import data
import operator
import copy
import numpy as np
import numpy.random as rn
from classes import classes
from classes import helpers
from algorithms import randomAlgorithm
from visualisation import visualisation
sys.path.append('C:/TeamThomasDeTrein/classes')
sys.path.append('C:/TeamThomasDeTrein/visualisation')

def snakeLine(line, amountOfTrajectories, stepSize):
    for amount in range(amountOfTrajectories):
        emptyTrajectory = classes.Trajectory([], line.RailwayList)
        startTrajectory = makeSnakeTrajectory(line, emptyTrajectory, stepSize)

        line.addTrajectByTrajectory(startTrajectory)

    for i in range(20):
        trajectoryList = line.updateTrajectoryList()
        for trajectory in trajectoryList:
            line.replaceTrajectoryBySnake(trajectory, stepSize)

    print(line.SLine())
    return line

def makeSnakeTrajectory(line, startTrajectory, stepSize):
    # startTrajectory = randomAlgorithm.randomTrajectory(emptyTrajectory, 20)
    if len(startTrajectory.Raillist) == 0:
        line.addHighestRailInTrajectory(startTrajectory)

    for steps in range(stepSize):
        fraction = steps / float(stepSize)
        T = temperature(fraction)

        score = line.determineScoreWithTrajectory(startTrajectory)

        begScores, endScores = line.addTrajectoryAndDetermineCorrespondingRails(startTrajectory)

        selectedDict, var = chooseDict(begScores, endScores)

        randomRail, randomScore = random.choice(list(selectedDict.items()))

        startTrajectory.simAnnhealingAdd(var, score, randomScore, T, randomRail)

        startTrajectory.simAnnhealingChop(line, T)

    return startTrajectory

def acceptance(oldScore, newScore, temperature):
    if newScore < oldScore:
        p = np.exp(- (oldScore - newScore) / temperature)
        return p
    else:
        return 1

def temperature(fraction):
    return max(0.01, min(1, 1 - fraction))

def chooseDict(begScores, endScores):
    listOfDicts = []
    listOfDicts.append(begScores)
    listOfDicts.append(endScores)
    selectedDict = random.choice(listOfDicts)

    if selectedDict == begScores:
        var = "begin"

    if selectedDict == endScores:
        var = "end"

    return selectedDict, var
