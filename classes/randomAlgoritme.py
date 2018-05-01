import random
import csv
import sys
import os
from data import *
from classes import classes

# deze functie is nog niet helemaal af, comments komen later

def randomAlgorithm(RailwayList):
    aantalTrajecten = 7
    finalrail = []
    for traject in range(aantalTrajecten):
        listOfRails = []
        randomRail = random.randint(0, len(RailwayList) - 1)
        listOfRails.append(RailwayList[randomRail])

        amountOfRails = random.randint(1,10)
        for amount in range(amountOfRails):
            correspondingStations = []

            for rail in RailwayList:
                if (listOfRails[-1].stationBeginning == rail.stationBeginning
                    or listOfRails[-1].stationBeginning == rail.stationEnd
                    or listOfRails[-1].stationEnd == rail.stationBeginning
                    or listOfRails[-1].stationEnd == rail.stationEnd):
                        correspondingStations.append(rail)

            randomRailNext = random.randint(0, len(correspondingStations) - 1)
            listOfRails.append(correspondingStations[randomRailNext])

            minutesTrajectory = 0
            for rails in listOfRails:
                minutesTrajectory += rails.minutes
                if minutesTrajectory > 120:
                    listOfRails.pop()

        trajectoryFinal = classes.Trajectory(listOfRails)

        finalrail.append(trajectoryFinal)

    return finalrail
