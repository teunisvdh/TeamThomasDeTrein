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


# alkmaar = classes.Station('Alkmaar',52.63777924,4.739722252,'Kritiek')

# x = alkmaar.x
# y = alkmaar.y

with open('data/StationsHolland.csv') as csvfile:
    stationsinfo = csv.reader(csvfile, delimiter=',')
    stationList = []
    for station in stationsinfo:
        stationList.append(classes.Station(station[0], station[1], station[2], station[3]))

# print(station.name)
for station in stationList:
    x = float(station.y)
    y = float(station.x)
    # lin.line(x, y, 'ro-')
    plt.plot(x, y, 'ro-')
    plt.annotate(station.name, xy=(x,y))

print(stationList[0].name)

# plt.plot([52.3, 52.5], [3.6, 3.7], 'k-')
# plt.plot([stationList[0].x,stationList[1].x], [stationList[0].y,stationList[1].y], 'k-')
plt.xlabel("longitude")
plt.ylabel("latitude")
plt.title("Visualisation")
plt.axis('equal')
plt.show()

print(stationList[0].name)
