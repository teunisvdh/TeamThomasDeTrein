import csv
import sys
import os
import matplotlib.pyplot as plt
import matplotlib.lines as lin
import numpy as np
from data import *
from classes import classes
from classes import helpers
from classes import randomAlgoritme

with open('data/StationsHolland.csv') as csvfile:
    stationsinfo = csv.reader(csvfile, delimiter=',')
    stationList = []
    for station in stationsinfo:
        stationList.append(classes.Station(station[0], station[1], station[2], station[3]))

stationTrajectory = [stationList[0], stationList[1], stationList[2], stationList[3]]

for station in stationList:
    x = float(station.y)
    y = float(station.x)
    plt.plot(x, y, 'ro-')
    plt.annotate(station.name, xy=(x,y))

def connect(begin, eind):
    x1 = float(stationList[begin].y)
    y1 = float(stationList[begin].x)
    x2 = float(stationList[eind].y)
    y2 = float(stationList[eind].x)
    plt.plot([x1, x2], [y1, y2], 'k-')

connect(18, 10);

for station in stationTrajectory:
    print(station.name)
    # connect(station, station+1)

plt.xlabel("longitude")
plt.ylabel("latitude")
plt.title("Visualisation")
plt.axis('equal')
plt.show()
