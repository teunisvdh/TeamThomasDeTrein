import random
import csv
import sys
import os
import data
from visualisation import visualisation
from classes import classes
from classes import helpers
from algorithms import randomAlgorithm
from algorithms import SimulatedAnnealing
sys.path.append('C:/TeamThomasDeTrein/classes')
sys.path.append('C:/TeamThomasDeTrein/visualisation')

def hillClimber(line, iterations, replace):
    """A function which changes, adds and removes trajectories from given
    trajectory as long as the score increases

    Args:
        line (Line): Line element which you want to improve
        iterations (int): Amount of iterations which you want to use
        replace (string): Input "random" when you want to replace for random
            trajectories, Input "snake" when you want to replace for snake
            trajectories

    Returns:
        The final line
    """
    for i in range(iterations):

        # select a random trajectory
        RandomTrajectory = line.selectRandomTrajectory()

        # determine score of trajectory and the score without a random trajectory
        score, score_2 = line.scoreWithAndWithoutTrajectory(RandomTrajectory)

        # make a replacement trajectory, either by snake or random
        replaceTrajectory = line.makeReplace(replace)

        # add replaceTrajectory and determine score
        score_3 = line.scoreWithTrajectory(replaceTrajectory)

        # if first score was the highest replace first trajectory for replacement
        if score_3 < score and score_2 < score:
            line.removeTrajectByTrajectory(replaceTrajectory)
            line.addTrajectByTrajectory(RandomTrajectory)

        # if second score was the highest keep no trajectory
        elif score_3 < score_2 and score < score_2:
            line.removeTrajectByTrajectory(replaceTrajectory)

        # try to add another trajectory and accept when score get higher
        if file == "nationaal":
            line.addToUnfullLine(20, replace)

        if file == "holland":
            line.addToUnfullLine(7, replace)

    return(line)
