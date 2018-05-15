import random
import csv
import sys
import os
from data import *
from classes import classes
from classes import helpers
from algorithms import randomAlgorithm
sys.path.append('C:/TeamThomasDeTrein/classes')

def hillClimber(RailwayList, criticalRailwayList, amount):
    """A function which changes, adds and removes trajectories from a
    random trajectory as long as the score increases

    Args:
        RailwayList (list): list of all  rails.
        criticalRailwayList (list): list of all critical rails.

    Returns:
        The final score of the line
    """

    # start with a random line
    randomStartLine = randomAlgorithm.randomLine(RailwayList, criticalRailwayList)

    for i in range(amount):
        # determine score
        score = helpers.calculate.score(randomStartLine, criticalRailwayList)

        # remove a random trajectory
        chooseRandomTrajectory = random.randint(0,len(randomStartLine) - 1)
        randomTrajectoryRemove = randomStartLine[chooseRandomTrajectory]
        randomStartLine.remove(randomTrajectoryRemove)

        # determine score again
        score_2 = helpers.calculate.score(randomStartLine, criticalRailwayList)

        # add a random trajectory
        replaceTrajectory = randomAlgorithm.randomTrajectory(RailwayList)
        randomStartLine.append(replaceTrajectory)

        # determine score again
        score_3 = helpers.calculate.score(randomStartLine, criticalRailwayList)

        # if first score was the highest replace first trajectory for replacement
        if score_3 < score and score_2 < score:
            randomStartLine.remove(replaceTrajectory)
            randomStartLine.append(randomTrajectoryRemove)

        # if second score was the highest keep no trajectory
        elif score_3 < score_2 and score < score_2:
            randomStartLine.remove(replaceTrajectory)

        # check if line is full
        if len(randomStartLine) < len(randomStartLine):

            # determine score
            score_4 = helpers.calculate.score(randomStartLine, criticalRailwayList)

            # add a new random trajectory
            newTrajectory = randomAlgorithm.randomTrajectory(RailwayList)
            randomStartLine.append(newTrajectory)

            # determine score
            score_5 = helpers.calculate.score(randomStartLine, criticalRailwayList)

            # if score is not higher, remove trajectory
            if score_4 > score_5:
                randomStartLine.remove(newTrajectory)

    # determine final score
    finalscore = helpers.calculate.score(randomStartLine, criticalRailwayList)

    # print final score
    print(finalscore)
