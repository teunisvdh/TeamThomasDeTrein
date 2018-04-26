import csv
import sys
import os
import matplotlib.pyplot as plt
import matplotlib.lines as lin
import numpy as np
from data import *
from classes import classes
from classes import helpers


alkmaar = classes.Station('Alkmaar',52.63777924,4.739722252,'Kritiek')

x = alkmaar.x
y = alkmaar.y

# for i in range(20):
# plt.plot(x, y, 'ro-')
#
# plt.show()

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

plt.xlabel("longitude")
plt.ylabel("latitude")
plt.title("Visualisation")
plt.axis('equal')
plt.show()
