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

def snakeTrajectory(line, amountOfTrajectories, stepSize):
    for amount in range(amountOfTrajectories):
        emptyTrajectory = classes.Trajectory([], line.RailwayList)
        startTrajectory = makeTrajectory(line, emptyTrajectory, stepSize)

        line.addTrajectByTrajectory(startTrajectory)

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
    return line


def makeTrajectory(line, startTrajectory, stepSize):

    # startTrajectory = randomAlgorithm.randomTrajectory(emptyTrajectory, 20)
    if len(startTrajectory.Raillist) == 0:
        listOfScores = {}

        for rail in startTrajectory.RailwayList:
            # if rail is connected at beginning traject, beginTraject wil be stationEnd of new rail
            startTrajectory.addRailbyRailBeginning(rail)
            line.addTrajectByTrajectory(startTrajectory)
            score = line.SLine()
            listOfScores[rail] = score
            line.removeTrajectByTrajectory(startTrajectory)
            startTrajectory.removeRailbyRailBeginning()

            highestRail = (max(listOfScores.items(), key=operator.itemgetter(1))[0])
            highestScore = (max(listOfScores.items(), key=operator.itemgetter(1))[1])

        startTrajectory.addRailbyRailEnd(highestRail)

    for steps in range(stepSize):
        fraction = steps / float(stepSize)
        T = temperature(fraction)

        line.addTrajectByTrajectory(startTrajectory)
        # visualisation.printLine(line)
        # print(line.SLine())
        score = line.SLine()
        listOfScoresEnd = {}
        listOfScoresBeginning = {}
        line.removeTrajectByTrajectory(startTrajectory)
        possibleRails = startTrajectory.correspondingRails()

        for rail in possibleRails:
            # if rail is connected at beginning traject, beginTraject wil be stationEnd of new rail
            if startTrajectory.trajectBeginStation == rail.stationBeginning:
                startTrajectory.addRailbyRailBeginning(rail)
                line.addTrajectByTrajectory(startTrajectory)
                score_2 = line.SLine()
                listOfScoresBeginning[rail] = score_2
                line.removeTrajectByTrajectory(startTrajectory)
                startTrajectory.removeRailbyRailBeginning()

            if startTrajectory.trajectEndStation == rail.stationBeginning:
                startTrajectory.addRailbyRailEnd(rail)
                line.addTrajectByTrajectory(startTrajectory)
                score_2 = line.SLine()
                listOfScoresEnd[rail] = score_2
                line.removeTrajectByTrajectory(startTrajectory)
                startTrajectory.removeRailbyRailEnd()

        listOfDicts = []
        listOfDicts.append(listOfScoresBeginning)
        listOfDicts.append(listOfScoresEnd)

        selectedDict = random.choice(listOfDicts)

        if selectedDict == listOfScoresBeginning:
            var = "begin"

        if selectedDict == listOfScoresEnd:
            var = "end"

        randomRail, randomScore = random.choice(list(selectedDict.items()))

        if acceptance(score, randomScore, 10*T) > rn.random():
            if var == "begin":
                startTrajectory.addRailbyRailBeginning(randomRail)
            if var == "end":
                startTrajectory.addRailbyRailEnd(randomRail)

        if len(startTrajectory.Raillist) > 1:
            line.addTrajectByTrajectory(startTrajectory)
            scoreZonderAfhak = line.SLine()
            line.removeTrajectByTrajectory(startTrajectory)

            startRail = startTrajectory.Raillist[0]
            startTrajectory.removeRailbyRailBeginning()

            line.addTrajectByTrajectory(startTrajectory)
            scoreMetAfhak = line.SLine()
            line.removeTrajectByTrajectory(startTrajectory)

            startTrajectory.addRailbyRailBeginning(startRail)

            if acceptance(scoreZonderAfhak, scoreMetAfhak,  10 * T) > rn.random():
                startTrajectory.removeRailbyRailBeginning()


        # highestRailBeginning = (max(listOfScoresBeginning.items(), key=operator.itemgetter(1))[0])
        # highestScoreBeginning = (max(listOfScoresBeginning.items(), key=operator.itemgetter(1))[1])
        #
        # highestRailEnd= (max(listOfScoresEnd.items(), key=operator.itemgetter(1))[0])
        # highestScoreEnd = (max(listOfScoresEnd.items(), key=operator.itemgetter(1))[1])
        #
        # highestTotal = max(highestScoreBeginning, highestScoreEnd)
        #
        # if highestTotal == highestScoreEnd:
        #     startTrajectory.addRailbyRailEnd(highestRailEnd)
        #
        #     minutes = startTrajectory.minutesTrajectory()
        #     if minutes > 120:
        #         startTrajectory.removeRailbyRailEnd()
        #
        # elif highestTotal == highestScoreBeginning:
        #     startTrajectory.addRailbyRailBeginning(highestRailBeginning)
        #
        #     minutes = startTrajectory.minutesTrajectory()
        #     if minutes > 120:
        #         startTrajectory.removeRailbyRailBeginning()

        # if len(startTrajectory.Raillist) > 3:
        #     line.addTrajectByTrajectory(startTrajectory)
        #     score_3 = line.SLine()
        #     line.removeTrajectByTrajectory(startTrajectory)
        #
        #     beginRail = startTrajectory.Raillist[0]
        #     startTrajectory.removeRailbyRailBeginning()
        #
        #     line.addTrajectByTrajectory(startTrajectory)
        #     score_4 = line.SLine()
        #     line.removeTrajectByTrajectory(startTrajectory)
        #
        #     if score_3 > score_4 - 50:
        #         startTrajectory.addRailbyRailBeginning(beginRail)

    return startTrajectory

def acceptance(oldScore, newScore, temperature):
    if newScore < oldScore:
        p = np.exp(- (oldScore - newScore) / temperature)
        return p
    else:
        return 1

def temperature(fraction):
    return max(0.01, min(1, 1 - fraction))
