import random
import csv
import sys
import os
from data import *
from classes import classes
from classes import helpers
from algorithms import randomAlgorithm
sys.path.append('C:/TeamThomasDeTrein/classes')

def hillClimber(line, iterations):
    """A function which changes, adds and removes trajectories from given
    trajectory as long as the score increases

    Args:
        line (Line): Line element which you want to improve
        iterations: Amount of iterations which you want to use

    Returns:
        The final score of the line
    """
    for i in range(iterations):

        # determine score
        score = line.SLine()

        # select a random trajectory
        RandomTrajectory = line.selectRandomTrajectory()

        # remove random trajectory
        line.removeTrajectByTrajectory(RandomTrajectory)

        # determine score again
        score_2 = line.SLine()

        # make empty trajectory to put random rails in
        emptyTrajectory = classes.Trajectory([], line.RailwayList)

        # put random rails in empty trajectory
        replaceTrajectory = randomAlgorithm.randomTrajectory(emptyTrajectory, 20)

        # add trajectory to line
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

        maxAmountOfTrajectories = 7

        # check if line is full
        if line.lenLine() < maxAmountOfTrajectories:

            # determine score
            score_4 = line.SLine()

            # add a new random trajectory
            newTrajectory = randomAlgorithm.randomTrajectory(emptyTrajectory, 10)
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
