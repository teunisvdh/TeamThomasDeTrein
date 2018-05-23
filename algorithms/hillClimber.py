import random
import csv
import sys
import os
import data
from visualisation import visualisation
from classes import classes
from classes import helpers
from algorithms import randomAlgorithm
sys.path.append('C:/TeamThomasDeTrein/classes')
sys.path.append('C:/TeamThomasDeTrein/visualisation')

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

        # select a random trajectory
        RandomTrajectory = line.selectRandomTrajectory()

        score, score_2 = line.scoreWithAndWithoutTrajectory(RandomTrajectory)

        replaceTrajectory = randomAlgorithm.emptyRandom(line)

        score_3 = line.scoreWithTrajectory(replaceTrajectory)

        # if first score was the highest replace first trajectory for replacement
        if score_3 < score and score_2 < score:
            line.removeTrajectByTrajectory(replaceTrajectory)
            line.addTrajectByTrajectory(RandomTrajectory)

        # if second score was the highest keep no trajectory
        elif score_3 < score_2 and score < score_2:
            line.removeTrajectByTrajectory(replaceTrajectory)

        line.addToUnfullLine(20)

    # determine final score
    finalscore = line.SLine()

    # print(finalscore)
    # print(line.lenLine())

    return(line)
