import random
import csv
import sys
import os
import data
from visualisation import visualisation
from classes import classes
from classes import helpers
from algorithms import SimulatedAnnealing
from algorithms import randomAlgorithm
sys.path.append('C:/TeamThomasDeTrein/classes')
sys.path.append('C:/TeamThomasDeTrein/visualisation')

def annealclimber(line, iterations, replace):
    """A function which changes, adds and removes trajectories from given
    trajectory as long as the score increases

    Args:
        line (Line): Line element which you want to improve
        iterations: Amount of iterations which you want to use

    Returns:
        The final score of the line
    """
    for i in range(iterations):
        fraction = i / float(iterations)
        T = SimulatedAnnealing.temperature(fraction)

        # select a random trajectory
        RandomTrajectory = line.selectRandomTrajectory()

        score, score_2 = line.scoreWithAndWithoutTrajectory(RandomTrajectory)

        if replace == "random":
            replaceTrajectory = randomAlgorithm.emptyRandom(line)

        if replace == "snake":
            emptyTrajectory = classes.Trajectory([], line.RailwayList)
            replaceTrajectory = SimulatedAnnealing.makeSnakeTrajectory(line, emptyTrajectory, 15)

        score_3 = line.scoreWithTrajectory(replaceTrajectory)

        line.removeTrajectByTrajectory(replaceTrajectory)
        line.addTrajectByTrajectory(RandomTrajectory)

        choice = random.choice([score_2, score_3])

        if choice == score_2:
            if SimulatedAnnealing.acceptance(score, score_2, 100000 * T) == True:
                line.removeTrajectByTrajectory(RandomTrajectory)

        if choice == score_3:
            if SimulatedAnnealing.acceptance(score, score_3, 100000 * T) == True:
                line.removeTrajectByTrajectory(RandomTrajectory)
                line.addTrajectByTrajectory(replaceTrajectory)

        line.addToUnfullLine(20)

    # determine final score
    finalscore = line.SLine()

    # print(finalscore)
    # print(line.lenLine())

    return(line)
