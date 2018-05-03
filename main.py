import csv
import sys
import os
import random
from data import *
from classes import classes
from classes import helpers
from classes import make
from classes import randomAlgorithm

def main():
    # open the files including critical data
    stationList, criticalstationList = helpers.openFile.file1("data/StationsHolland.csv")
    RailwayList, criticalRailwayList = helpers.openFile.file2("data/ConnectiesHolland.csv", criticalstationList)

    # make line of trajectories
    line1 = make.makeLine1(RailwayList)

    # helpers.show.printList(RailwayList)

    # print calculated score
    # helpers.show.printScore(line1, criticalRailwayList)
    listofs = []

    highestScore = 0
    for i in range(100):
        rail = randomAlgorithm.randomAlgorithm(RailwayList, criticalRailwayList)
        score = helpers.show.printScore(rail, criticalRailwayList)
        if score > highestScore:
            highestScore = score
            highestRail = rail


    print(highestScore)
    print(highestRail[1].Raillist[1].stationBeginning)
    # print(helpers.show.printScore(line1, criticalRailwayList))
if __name__ == "__main__":
    main()
