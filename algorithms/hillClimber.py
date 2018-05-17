import random
import csv
import sys
import os
from data import *
from classes import classes
from classes import helpers
from algorithms import randomAlgorithm
sys.path.append('C:/TeamThomasDeTrein/classes')

def hillClimber(line, amount):
    """A function which changes, adds and removes trajectories from a
    random trajectory as long as the score increases

    Args:
        RailwayList (list): list of all  rails.
        criticalRailwayList (list): list of all critical rails.

    Returns:
        The final score of the line
    """
    for i in range(amount):
        # determine score
        score = line.SLine()

        chooseRandomTrajectory = random.randint(0, line.lenLine() - 1)
        RandomTrajectory = line.translateTrajectByNumber(chooseRandomTrajectory)

        line.removeTrajectByTrajectory(RandomTrajectory)

        # determine score again
        score_2 = line.SLine()

        replaceTrajectory = randomAlgorithm.randomTrajectory(line.RailwayList)
        line.addTrajectByTrajectory(replaceTrajectory)

        # determine score again
        score_3 = line.SLine()

        # if first score was the highest replace first trajectory for replacement
        if score_3 < score and score_2 < score:
            line.removeTrajectByTrajectory(replaceTrajectory)
            line.addTrajectByTrajectory(RandomTrajectory)

        # if second score was the highest keep no trajectory
        elif score_3 < score_2 and score < score_2:
            line.removeTrajectByTrajectory(replaceTrajectory)

        # check if line is full
        if line.lenLine() < 7:

            # determine score
            score_4 = line.SLine()

            # add a new random trajectory
            newTrajectory = randomAlgorithm.randomTrajectory(line.RailwayList)
            line.addTrajectByTrajectory(newTrajectory)

            # determine score
            score_5 = line.SLine()

            # if score is not higher, remove trajectory
            if score_4 > score_5:
                line.removeTrajectByTrajectory(newTrajectory)

    # determine final score
    finalscore = line.SLine()

    print(finalscore)
    print(line.lenLine())

    return(line)
