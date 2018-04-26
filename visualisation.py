import csv
import sys
import os
from data import *
from classes import classes
from classes import helpers

with open('data/StationsHolland.csv') as csvfile:
    stationsinfo = csv.reader(csvfile, delimiter=',')
    stationList = []
    for station in stationsinfo:
        stationList.append(classes.Station(station[0], station[1], station[2], station[3]))

print("Dit is de lijst:")
print(stationList)

for station in stationList:
    print(station)

print("kjasdflkjbsdlfkjbsd")
