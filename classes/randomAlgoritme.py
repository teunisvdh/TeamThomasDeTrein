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
        for i in range(random.randint(1,10)):
            corresponding = []
            for railll in RailwayList:
                minutes = 0
                if (raill[-1].stationBeginning == railll.stationBeginning
                    or raill[-1].stationBeginning == railll.stationEnd
                    or raill[-1].stationEnd == railll.stationBeginning
                    or raill[-1].stationEnd == railll.stationEnd):
                        corresponding.append(railll)

            rand_3 = random.randint(0, len(corresponding) - 1)
            raill.append(corresponding[rand_3])

            for rails in raill:
                minutes += rails.minutes
                print(minutes)
                if minutes > 120:
                    print(raill)
                    print(raill[-1])
                    raill.remove(raill[-1])
                    print(raill)


        trajectorry = classes.Trajectory(raill)
        rail.append(trajectorry)

    return rail
