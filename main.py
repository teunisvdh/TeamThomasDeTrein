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

    for i in range(100000):
        rail = randomAlgorithm.randomAlgorithm(RailwayList)
        listofs.append(helpers.show.printScore(rail, criticalRailwayList))

    # for traject in rail:
    #     print("!!!!!!!!!!!!!!stop!!!!!!!!!!!!!!!!!")
    #     for station in traject.__dict__.items():
    #         print(station)
    #         for stationecht in station[1]:
    #             print(stationecht.stationBeginning)
    #             print("to")
    #             print(stationecht.stationEnd)

    print(max(listofs))
    #helpers.show.printScore(rail, criticalRailwayList)

if __name__ == "__main__":
    main()
