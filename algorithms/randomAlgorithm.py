import random
import csv
import sys
import os
from data import *
from classes import classes
from classes import helpers
sys.path.append('C:/TeamThomasDeTrein/classes')

def randomTrajectory(RailwayList):
    listOfRails = []

    # add a random connection
    randomRail = random.randint(0, len(RailwayList) - 1)
    listOfRails.append(RailwayList[randomRail])

    # if startingpoint is StationBeginning
    StationIsBeginning = True

    # add a random amount more connections
    amountOfRails = random.randint(1,10)

    for amount in range(amountOfRails):
        correspondingStations = []
        # make a list of all connections that can be added
        if StationIsBeginning == True:
            for rail in RailwayList:
                if listOfRails[-1].stationBeginning == rail.stationBeginning:
                    correspondingStations.append(rail)
                elif listOfRails[-1].stationBeginning == rail.stationEnd:
                    correspondingStations.append(rail)
            randomRailNext = random.randint(0, len(correspondingStations) - 1)
            if correspondingStations[randomRailNext].stationBeginning == listOfRails[-1].stationBeginning:
                StationIsBeginning = False
            else:
                StationIsBeginning = True
        elif StationIsBeginning == False:
            for rail in RailwayList:
                if listOfRails[-1].stationEnd == rail.stationBeginning:
                    correspondingStations.append(rail)
                elif listOfRails[-1].stationEnd == rail.stationEnd:
                    correspondingStations.append(rail)
            randomRailNext = random.randint(0, len(correspondingStations) - 1)
            if correspondingStations[randomRailNext].stationEnd == listOfRails[-1].stationEnd:
                StationIsBeginning = True
            else:
                StationIsBeginning = False

        listOfRails.append(correspondingStations[randomRailNext])

        minutesTrajectory = helpers.calculate.minutesTrajectory(listOfRails)

        if minutesTrajectory > 120:
            listOfRails.pop()

        # make trajectory object of the list of connections
        trajectoryFinal = classes.Trajectory(listOfRails)

    return trajectoryFinal

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
