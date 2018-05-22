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

<<<<<<< HEAD
    for i in range(3):
        trajectoryList = line.updateTrajectoryList()
        for trajectory in trajectoryList:
            line.replaceTrajectoryBySnake(trajectory, stepSize)

=======
    for i in range(10):
        trajectoryList = []
        for traject in line.TrajectoryList:
            trajectoryList.append(traject)
        for trajectory in trajectoryList:
                score = line.SLine()
                tempTrajectory = classes.Trajectory([], line.RailwayList)
                for rail in trajectory.Raillist:
                    tempTrajectory.addRailbyRailEnd(rail)
                line.removeTrajectByTrajectory(trajectory)
                replaceTrajectory = makeTrajectory(line, tempTrajectory, stepSize)
                line.addTrajectByTrajectory(replaceTrajectory)
                score_2 = line.SLine()
                line.removeTrajectByTrajectory(replaceTrajectory)

                if score_2 > score:
                    line.addTrajectByTrajectory(replaceTrajectory)

                else:
                    line.addTrajectByTrajectory(trajectory)
    print(line.SLine())
>>>>>>> f51be71b414710b444d531a1f262aa8d5fcc5372
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

        if acceptance(score, randomScore, 10*T) > rn.random():
            if var == "begin":
                startTrajectory.addRailbyRailBeginning(randomRail)
            if var == "end":
                startTrajectory.addRailbyRailEnd(randomRail)

        if len(startTrajectory.Raillist) > 1:
            score, choppedScore = line.checkScoreAndChoppedScore(startTrajectory)

            if acceptance(score, choppedScore,  10 * T) > rn.random():
                startTrajectory.removeRailbyRailBeginning()

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
