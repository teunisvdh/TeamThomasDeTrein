import random
import csv
import sys
import os
from data import *
from classes import classes
from classes import helpers
sys.path.append('C:/TeamThomasDeTrein/classes')

def randomTrajectory(trajectory, amountOfRails):
    """A random algorithm which adds a random number between zero and a
    given number of rails to a given trajectory

    Args:
        trajectory (Trajectory): A Trajectory element which you want to update
        amountOfRails: Maximum amount of rails which you want to add. The amount
        of rails added will be a random number between zero and this number.

    Returns:
        The updated trajectory element
    """

    if len(trajectory.Raillist) == 0:
        trajectory.addRail()

    if len(trajectory.Raillist) > 1:
        trajectory.addConnections(amountOfRails)

    if len(trajectory.Raillist) == 1:
        trajectory.addConnections(amountOfRails - 1)

    return trajectory

def randomLine(line, amountOfTrajectories):
    """A random algorithm adds to a line a given amount of trajectories by
    the randomTrajectory function

    Args:
        line (Line): A Line element which you want to update.
        amountOfTrajectories: Amount of trajectories which you want to add.

    Returns:
        A updated line of trajectories.
    """

    # iterate over all trajectories
    for traject in range(amountOfTrajectories):

        emptyTrajectory = classes.Trajectory([], line.RailwayList)

        trajectoryFinal = randomTrajectory(emptyTrajectory, 10)

        line.addTrajectByTrajectory(trajectoryFinal)

    return line
