import random
import csv
import sys
import os
from data import *
from classes import classes

def randomAlgorithm(RailwayList, criticalRailwayList):
    """A random algorithm which creates a line of 7 trajectories with a maximum of
    ten railway connection in each trajectory.

    Args:
        RailwayList (list): A list of all railway connections.

    Returns:
        A line of seven trajectories.
    """
    aantalTrajecten = 7
    finalrail = []

    # iterate over all 7 trajectories
    for traject in range(aantalTrajecten):

        listOfRails = []

        # add a random connection
        randomRail = random.randint(0, len(RailwayList) - 1)
        listOfRails.append(RailwayList[randomRail])

        # add a random amount more connections
        amountOfRails = random.randint(1,15)
        for amount in range(amountOfRails):
            correspondingStations = []

            # make a list of all connections that can be added
            for rail in RailwayList:
                if (listOfRails[-1].stationBeginning == rail.stationBeginning
                    or listOfRails[-1].stationBeginning == rail.stationEnd
                    or listOfRails[-1].stationEnd == rail.stationBeginning
                    or listOfRails[-1].stationEnd == rail.stationEnd):
                        correspondingStations.append(rail)

            randomRailNext = random.randint(0, len(correspondingStations) - 1)
            var = 0
            # add one random connection from this list to the trajectory
            while(correspondingStations[randomRailNext] in listOfRails):
                var += 1
                randomRailNext = random.randint(0, len(correspondingStations) - 1)
                if var == 10:
                    break

            listOfRails.append(correspondingStations[randomRailNext])

            # check if amounts of minutes does not exceed
            minutesTrajectory = 0
            for rails in listOfRails:
                minutesTrajectory += rails.minutes

                # if so delete the last trajectory
                if minutesTrajectory > 120:
                    listOfRails.pop()

        # make trajectory object of the list of connections
        trajectoryFinal = classes.Trajectory(listOfRails)

        finalrail.append(trajectoryFinal)

    return finalrail
