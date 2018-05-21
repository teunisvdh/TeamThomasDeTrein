import random
import csv
import sys
import os
import data
import operator
from classes import classes
from classes import helpers
from algorithms import randomAlgorithm
from visualisation import visualisation
sys.path.append('C:/TeamThomasDeTrein/classes')
sys.path.append('C:/TeamThomasDeTrein/visualisation')

def snakeTrajectory(line, amountOfTrajectories, stepSize):

    for amount in range(amountOfTrajectories):
        emptyTrajectory = classes.Trajectory([], line.RailwayList)
        startTrajectory = randomAlgorithm.randomTrajectory(emptyTrajectory, 20)
        if len(startTrajectory.Raillist) == 0:
            startTrajectory.addRail()

        for steps in range(stepSize):
            line.addTrajectByTrajectory(startTrajectory)
            visualisation.printLine(line)
            print(line.SLine())
            score = line.SLine()
            listOfScores = {}
            line.removeTrajectByTrajectory(startTrajectory)
            possibleRails = startTrajectory.correspondingRails()

            for rail in possibleRails:
                # if rail is connected at beginning traject, beginTraject wil be stationEnd of new rail
                if startTrajectory.trajectBeginStation == rail.stationBeginning:
                    minutes = startTrajectory.minutesTrajectory()
                    if minutes > 120:
                        startTrajectory.Pop()
                    else:
                        startTrajectory.trajectBeginStation = rail.stationEnd
                        startTrajectory.addRailbyRailBeginning(rail)
                        line.addTrajectByTrajectory(startTrajectory)
                        score_2 = line.SLine()
                        listOfScores[rail] = score_2  - score
                        line.removeTrajectByTrajectory(startTrajectory)
                        startTrajectory.removeRailbyRail(rail)


                elif startTrajectory.trajectEndStation == rail.stationBeginning:
                    minutes = startTrajectory.minutesTrajectory()
                    if minutes > 120:
                        startTrajectory.Pop()
                    else:
                        startTrajectory.trajectEndStation = rail.stationEnd
                        startTrajectory.addRailbyRailEnd(rail)
                        line.addTrajectByTrajectory(startTrajectory)
                        score_2 = line.SLine()
                        listOfScores[rail] = score_2  - score
                        line.removeTrajectByTrajectory(startTrajectory)
                        startTrajectory.removeRailbyRail(rail)

            highestRail = (max(listOfScores.items(), key=operator.itemgetter(1))[0])

            startTrajectory.addRailbyRailEnd(highestRail)
        line.addTrajectByTrajectory(startTrajectory)
