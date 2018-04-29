import random
import csv
import sys
import os
from data import *
from classes import classes

# deze functie is nog niet helemaal af, comments komen later

def randomAlgoritme(RailwayList):
    rail = []
    for i in range(7):
        raill = []
        rand_2 = random.randint(0, len(RailwayList) - 1)
        raill.append(RailwayList[rand_2])
        for i in range(random.randint(1,7)):
            for railll in RailwayList:
                if railll.stationEnd == raill[-1].stationBeginning:
                    raill.append(railll)
                    break
        trajectorry = classes.Trajectory(raill)
        rail.append(trajectorry)

    return rail
