import csv
import sys
import os
import random
from data import *
from classes import classes
from classes import helpers
from classes import make
from algorithms import randomAlgorithm
from algorithms import hillClimber

from visualisation import visualisation

def main():
    # open the files including critical data
    stationList, criticalstationList = helpers.openFile.file1("data/StationsHolland.csv")
    RailwayList, criticalRailwayList = helpers.openFile.file2("data/ConnectiesHolland.csv", criticalstationList)

    # make line of trajectories
    line1 = make.makeLine1(RailwayList)

    # helpers.show.printList(RailwayList)

    # print calculated score
    # helpers.show.printScore(line1, criticalRailwayList)

    slist = []
    highestScore = 0
    for i in range(1):
        rail = randomAlgorithm.randomLine(RailwayList, criticalRailwayList)
        score = helpers.calculate.score(rail, criticalRailwayList)
        slist.append(score)
        # if score > highestScore:
        #     highestScore = score
        #     highestRail = rail

<<<<<<< HEAD
    hillClimber.hillClimber(RailwayList, criticalRailwayList, 10000)
=======
    railHill = hillClimber.hillClimber(RailwayList, criticalRailwayList)
>>>>>>> e54fda058a63502dbbe3be923035de9e78a178cd

    # print(slist[0])

    visualisation.printLine(railHill)
    visualisation.visualize(railHill)


    # for i in range(len(highestRail)):
    #     print("Trajectory" + str(i))
    #     for k in range(len(highestRail[i].Raillist)):
    #         print("  " + "Rail " + str(k))
    #         print("    " + highestRail[i].Raillist[k].stationBeginning)
    #         print("    " + highestRail[i].Raillist[k].stationEnd)
    #
    # print(highestScore)
    # print(helpers.show.printScore(line1, criticalRailwayList))
if __name__ == "__main__":
    main()
