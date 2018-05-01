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

with open('data/ConnectiesHolland.csv') as csvfile:
    connectioninfo = csv.reader(csvfile, delimiter=',')
    connectionList = []
    for connection in connectioninfo:
        connectionList.append(classes.Rail(connection[0], connection[1], connection[2]))

# stationTrajectory = [stationList[0], stationList[1], stationList[2], stationList[3]]

# print(connectionList[0].stationBeginning)
# if (connectionList[0].stationBeginning == stationList[0].name):
#     print("yessss")
# else:
#     print("noooo")

for station in stationList:
    x = float(station.y)
    y = float(station.x)
    plt.plot(x, y, 'ro-')
    plt.annotate(station.name, xy=(x,y))

# def connect(begin, end):
#     x1 = float(stationList[begin].y)
#     y1 = float(stationList[begin].x)
#     x2 = float(stationList[end].y)
#     y2 = float(stationList[end].x)
#     plt.plot([x1, x2], [y1, y2], 'r--', linewidth=0.3)
#
# connect(18, 10);

def connect(begin, end):
    nameBegin = begin
    nameEnd = end
    for i in range(len(stationList)):
        if (stationList[i].name == nameBegin):
            x1=float(stationList[i].y)
            y1=float(stationList[i].x)
            break
    for i in range(len(stationList)):
        if (stationList[i].name == nameEnd):
            x2=float(stationList[i].y)
            y2=float(stationList[i].x)
            break
    plt.plot([x1, x2], [y1, y2], 'r--', linewidth=0.3)


#
for connection in connectionList:
    connect(connection.stationBeginning, connection.stationEnd)

# for station in stationTrajectory:
#     print(station.name)
#     # connect(station, station+1)

plt.xlabel("longitude")
plt.ylabel("latitude")
plt.title("Visualisation")
plt.axis('equal')
plt.show()
