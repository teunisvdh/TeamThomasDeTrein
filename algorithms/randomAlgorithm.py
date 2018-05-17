import random
import csv
import sys
import os
from data import *
from classes import classes
from classes import helpers
sys.path.append('C:/TeamThomasDeTrein/classes')

def randomTrajectory(trajectory, amountOfRails):
    # listOfRails = classes.Trajectory([], RailwayList)

    if len(trajectory.Raillist) == 0:
        trajectory.addRail()

    if len(trajectory.Raillist) > 1:
        trajectory.addConnections(amountOfRails)

    if len(trajectory.Raillist) == 1:
        trajectory.addConnections(amountOfRails - 1)

    return trajectory

def randomLine(line, amountOfTrajectories):
    """A random algorithm which creates a line of 7 trajectories with a maximum of
    ten railway connection in each trajectory.

    Args:
        RailwayList (list): A list of all railway connections.

    Returns:
        A line of seven trajectories.
    """

    # iterate over all trajectories
    for traject in range(amountOfTrajectories):

        emptyTrajectory = classes.Trajectory([], line.RailwayList)

        trajectoryFinal = randomTrajectory(emptyTrajectory, 10)

        line.addTrajectByTrajectory(trajectoryFinal)

    return line
