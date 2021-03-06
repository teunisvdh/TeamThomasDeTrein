import random
import csv
import sys
import os
import data
from visualisation import visualisation
from classes import lineClass
from classes import trajectoryClass
from classes import railAndStationClass
from classes import helpers
from algorithms import randomAlgorithm
from algorithms import SimulatedAnnealing
directory = os.path.dirname(os.getcwd())
sys.path.append(directory + '/TeamThomasDeTrein/classes')
sys.path.append(directory + '/TeamThomasDeTrein/algorithms')

def hillClimber(line, iterations, replace, amountOfRails):
    """A function which changes, adds and removes trajectories from given
    trajectory as long as the score increases

    Args:
        line (Line): Line element which you want to improve
        iterations (int): Amount of iterations which you want to use
        replace (string): Input "random" when you want to replace for random
            trajectories, Input "snake" when you want to replace for snake
            trajectories
        amountOfRails (int): Amount of rails you want to add per trajectory

    Returns:
        The final line
    """
    for i in range(iterations):

        # select a random trajectory
        RandomTrajectory = line.selectRandomTrajectory()

        # determine score of trajectory and the score without a random trajectory
        score, score_2 = line.scoreWithAndWithoutTrajectory(RandomTrajectory)

        # make a replacement trajectory, either by snake or random
        replaceTrajectory = line.makeReplace(replace, amountOfRails)

        # add replaceTrajectory and determine score
        score_3 = line.scoreWithTrajectory(replaceTrajectory)

        # if first score was the highest replace first trajectory for replacement
        if score_3 < score and score_2 < score:
            line.removeTrajectByTrajectory(replaceTrajectory)
            line.addTrajectByTrajectory(RandomTrajectory)

        # if second score was the highest keep no trajectory
        elif score_3 < score_2 and score < score_2:
            line.removeTrajectByTrajectory(replaceTrajectory)

        line.addToUnfullLine(helpers.Files.maxTrajectories, replace, amountOfRails)

    return(line)
