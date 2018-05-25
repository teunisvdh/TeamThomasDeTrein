import random
import csv
import sys
import os
import data
import operator
import copy
import numpy as np
import numpy.random as rn
from classes import lineClass
from classes import trajectoryClass
from classes import railAndStationClass
from classes import helpers
from algorithms import randomAlgorithm
from visualisation import visualisation
sys.path.append('C:/TeamThomasDeTrein/classes')
sys.path.append('C:/TeamThomasDeTrein/visualisation')

def snakeLine(line, amountOfTrajectories, stepSize, iterations, replace, amountOfRails):
    """A function that adds to a line a given amount of trajectories produced
    by either the makeSnakeTrajectory or random algorithm and then iterates over
    it's own trajectories 20 times and tries to improve its trajectories,
    again by either makeSnakeTrajectory or random algorithm.

    Args:
        line (Line): A Line element which you want to update.
        amountOfTrajectories (int): Amount of trajectories which you want to add
        stepSize (int): Amount of steps you want to take to make the trajectory
        iterations (int): Amount of times you want to try to improve all the the trajectories
        replace (string): Input "random" when you want to update trajectories
            with random algorithm and "snake" for the makeSnakeTrajectory function
        multiplicationAdd (float): Multiplication factor of T for adding rails
        multiplicationChop (float): Multiplication factor of T for chopping rails

    Returns:
        A updated line of trajectories.
    """
    # check if amount of trajectories is not exceeded
    if amountOfTrajectories + len(line.TrajectoryList) > helpers.Files.maxTrajectories:
        raise ValueError('Too many trajectories')

    for amount in range(amountOfTrajectories):

        # make a trajectory and add to line
        startTrajectory = line.makeReplace(replace, amountOfRails)
        line.addTrajectByTrajectory(startTrajectory)


    for i in range(iterations):

        # determine line's trajectories
        trajectoryList = line.updateTrajectoryList()

        # iterate over trajectories
        for trajectory in trajectoryList:

            # replace trajectory by a snake or random trajectory when improving
            line.replace(replace, trajectory, stepSize)

    return line

def makeSnakeTrajectory(line, startTrajectory, stepSize):
    """A function that make a trajectory by adding and deleting rails

    Args:
        line (Line): Line item in which you want to update trajectory
        startTrajectory (Trajectory): Trajectory item which you want to update
        stepSize (int): Amount of times you want to add or delete a rail

    Returns:
        An updated trajectory.
    """

    # startTrajectory = randomAlgorithm.randomTrajectory(emptyTrajectory, 20)
    if len(startTrajectory.Raillist) == 0:
        line.addHighestRailInTrajectory(startTrajectory)

    for steps in range(stepSize):

        # determine temperature for simmulated annealing
        fraction = steps / float(stepSize)
        T = temperature(fraction)

        # determine score with the current trajectory
        score = line.determineScoreWithTrajectory(startTrajectory)

        # determine all rails that can be added (at begin and end of trajectory)
        # and the corresponding scores
        begScores, endScores = line.determineRailsBeginEnd(startTrajectory)

        # choose if you want to add to begin or end of trajectory randomly
        selectedDict, var = chooseDict(begScores, endScores)

        # select a rail you want to add and it's corresponding score randomly
        randomRail, randomScore = random.choice(list(selectedDict.items()))

        # add the rail by simmulated annealing
        startTrajectory.simAnnealingAdd(var, score, randomScore, T, randomRail)

        # delete a rail by simmulated annealing
        startTrajectory.simAnnealingChop(line, T)

    return startTrajectory

def acceptance(oldScore, newScore, temperature):
    """A function that decides weather a negative change will be made

    Args:
        oldScore (int): The score without the change
        newScore (int): The score with the change
        temperature (int): The temperature of process

    Returns:
        A boolean: True when change will be made, False otherwise
    """

    if newScore < oldScore:
        p = np.exp(- (oldScore - newScore) / temperature)
        if p > rn.random():
            return True
        else:
            return False
    else:
        return True

def temperature(fraction):
    """A function that determines tempature based on the fraction of the iterations
    in which the proces is

    Args:
        fraction (float): Fraction of iterations where the proces is currently at

    Returns:
        The temperature
    """
    return max(0.01, min(1, 1 - fraction))

def chooseDict(begScores, endScores):
    """A function that chooses a dict given two dicts with a var either "begin" or "end:

    Args:
        begScores (dict): dict one with var "begin"
        endScores (dict): dict two with var "end"

    Returns:
        chosen dict and corresponding var
    """
    listOfDicts = []
    listOfDicts.append(begScores)
    listOfDicts.append(endScores)
    selectedDict = random.choice(listOfDicts)

    if selectedDict == begScores:
        var = "begin"

    if selectedDict == endScores:
        var = "end"

    return selectedDict, var
