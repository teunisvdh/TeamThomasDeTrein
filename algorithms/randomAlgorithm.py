import random
import csv
import sys
import os
from data import *
from classes import classes
from classes import helpers
sys.path.append('C:/TeamThomasDeTrein/classes')

def randomTrajectory(RailwayList):
    listOfRails = classes.Trajectory([], RailwayList)

    listOfRails.addRail()

    listOfRails.addConnections()

    return listOfRails

def randomLine(RailwayList, criticalRailwayList):
    """A random algorithm which creates a line of 7 trajectories with a maximum of
    ten railway connection in each trajectory.

    Args:
        RailwayList (list): A list of all railway connections.

    Returns:
        A line of seven trajectories.
    """
    amountofTrajectories = 7
    finalrail = []

    # iterate over all 7 trajectories
    for traject in range(amountofTrajectories):

        trajectoryFinal = randomTrajectory(RailwayList)

        finalrail.append(trajectoryFinal)

    return finalrail
