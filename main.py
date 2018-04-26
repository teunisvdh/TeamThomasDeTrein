import csv
import sys
import os
from data import *
from classes import classes
from classes import helpers
from classes import make

def main():
    # open the files including critical data
    stationList, criticalstationList = helpers.openFile.file1("data/StationsHolland.csv")
    RailwayList, criticalRailwayList = helpers.openFile.file2("data/ConnectiesHolland.csv", criticalstationList)

    # make line of trajectories
    line1 = make.makeLine1(RailwayList)

    #print calculated score
    helpers.show.printScore(line1, criticalRailwayList)



if __name__ == "__main__":
    main()
