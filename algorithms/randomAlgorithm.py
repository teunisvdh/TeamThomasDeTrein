import random
import csv
import sys
import os
from data import *
from classes import lineClass
from classes import trajectoryClass
from classes import railAndStationClass
from classes import helpers
directory = os.path.dirname(os.getcwd())
sys.path.append(directory + '/TeamThomasDeTrein/classes')

def randomTrajectory(trajectory, amountOfRails):
    """A random algorithm which adds a random number between zero and a
    given number of rails to a given trajectory

    Args:
        trajectory (Trajectory): A Trajectory element which you want to update
        amountOfRails (int): Amount of rails which you want to add. The amount
        of rails added will be a random number between zero and this number

    Returns:
        The updated trajectory element
    """

    # check if trajectory is empty
    if len(trajectory.Raillist) == 0:

        # add random start rail
        trajectory.addRail()

    # if trajectory was not empty make connected rails
    if len(trajectory.Raillist) > 1:
        trajectory.addConnections(amountOfRails)

    # if trajectory was empty make connected rails minus one
    if len(trajectory.Raillist) == 1:
        trajectory.addConnections(amountOfRails - 1)

    return trajectory

def randomLine(line, amountOfTrajectories, amountOfRails):
    """A random algorithm adds to a line a given amount of trajectories by
    the randomTrajectory function

    Args:
        line (Line): A Line element which you want to update.
        amountOfTrajectories (int): Amount of trajectories which you want to add.
        iterarations (int): Amount of rails you want to add
        amountOfRails (int): Amount of rails you want to add per trajectory

    Returns:
        A updated line of trajectories.
    """
    # check if amount of trajectories is not exceeded
    if amountOfTrajectories + len(line.TrajectoryList) > helpers.Files.maxTrajectories:
        raise ValueError('Too many trajectories')

    # iterate over all trajectories
    for traject in range(amountOfTrajectories):

        # update empty trajectory randomly
        trajectoryFinal = emptyRandom(line, amountOfRails)

        # add updated trajectory to line
        line.addTrajectByTrajectory(trajectoryFinal)

    return line

def emptyRandom(line, amountOfRails):
    """A function that adds to an empty line a random number between 0 and 10 of
    trajectories

    Args:
        line (Line): A Line element which you want to update.
        amountOfRails (int): Amount of rails you want to add per trajectory

    Returns:
        A random trajectory.
    """

    # make empty trajectory to put random rails in
    emptyTrajectory = trajectoryClass.Trajectory([], line.RailwayList)

    # put random rails in empty trajectory
    replaceTrajectory = randomTrajectory(emptyTrajectory, amountOfRails)

    return replaceTrajectory
